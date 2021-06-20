from django.db.models.deletion import CASCADE
from linxihotels.settings import *
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

EMPLOYEE_ROLES = (
    ('Gerente','Gerente'),
    ('Recepcionista', 'Recepcionista'),
)

ROOM_STATUS = (
    ('Livre','Livre'),
    ('Ocupado', 'Ocupado'),
)

RESERVATION_STATUS = (
    ('Pendente','Pendente'),
    ('Concluida', 'Concluida'),
    ('Em andamento', 'Em andamento'),
    ('Anulada', 'Anulada'),
)

ABODE_STATUS = (
    ('Concluida', 'Concluida'),
    ('Em andamento', 'Em andamento'),
)

class Company(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    contactNumber = models.IntegerField()
    category = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    peopleCount = models.IntegerField()
    period = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        if self.peopleCount == 1:
            return self.name + ' - ' + self.period + ' - %s pessoa' %self.peopleCount
        else:
            return self.name + ' - ' + self.period + ' - %s pessoas' %self.peopleCount

class serviceCompany(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return " / Empresa: " + self.Company.name + "Serviço: " + self.service.name

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    category = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ROOM_STATUS, default='Livre')

    def __str__(self):
        return self.company.name + ' - Quarto: %s' %self.number 


class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=EMPLOYEE_ROLES, default='Recepcionista')

    def save(self):
        if self.role == 'Recepcionista':
            group = Group.objects.get(name='Recepcionista') 
            self.user.save()

        if self.role == 'Gerente':
            group = Group.objects.get(name='Gerente') 
            self.user.save()

        group.user_set.add(self.user)
        super().save()

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    birth_date = models.DateField()
    address = models.CharField(max_length=200)
    contact_number = models.IntegerField()
    number_id = models.IntegerField(blank=True, null=True)
    issue_id = models.DateField(blank=True, null=True)
    passport = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True, default=None)

    def save(self):

        group = Group.objects.get(name='Cliente')

        if self.email is not None:
            self.user = User.objects.create_user(self.name, self.email, '123.%s' %self.birth_date)
            self.user.first_name = self.name
            self.user.email = self.email
            self.user.password = User.objects.make_random_password()
            group.user_set.add(self.user)
            self.user.save()

            send_mail(
                'olá '+ self.name + ' Bem vindo ao linxiHotels',
                'Sua senha foi gerada aleatoriamente para: ' + self.user.password,
                EMAIL_HOST_USER,
                [self.email],
                fail_silently=False,
            )
        else:
           self.user = User.objects.create_user(self.name, 'n/a', '123.%s' %self.birth_date)
           group.user_set.add(self.user)
           self.user.save()
        
        if self.user != '':
            super().save()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    company =  models.ForeignKey(Company, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    people_count = models.IntegerField()
    ocupation_date = models.DateField()
    leave_date = models.DateField()
    card_number = models.IntegerField()
    card_code = models.IntegerField()
    status = models.CharField(max_length=20, choices=RESERVATION_STATUS)

    def save(self):
        if self.room.capacity >= self.people_count and self.room.status == 'Livre':
            super().save()


    def __str__(self):
        return "Cliente: " + self.customer.name + " / Empresa: " + self.company.name
    
class ReservationService(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return "Reserva: " + self.reservation + " / Serviço: " + self.service

class Abode(models.Model):
    Reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    chek_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=ABODE_STATUS)

    def save(self):
        if self.Reservation.room.status == 'Livre':
            self.Reservation.status = 'Em andamento'
            self.Reservation.room.status = 'Ocupado'
            self.Reservation.room.save()
            self.Reservation.save()
            super().save(self)

    def __str__(self):
        return "Reserva: " + self.Reservation.customer.name + " / Quarto: %s" %self.Reservation.room.number