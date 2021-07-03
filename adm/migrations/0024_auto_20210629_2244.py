# Generated by Django 2.2.24 on 2021-06-30 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0023_auto_20210619_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecompany',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='servicecompany',
            name='service',
        ),
        migrations.AddField(
            model_name='service',
            name='company',
            field=models.ManyToManyField(to='adm.Company'),
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='service',
        ),
        migrations.AddField(
            model_name='reservation',
            name='service',
            field=models.ManyToManyField(to='adm.Service'),
        ),
        migrations.DeleteModel(
            name='ReservationService',
        ),
        migrations.DeleteModel(
            name='serviceCompany',
        ),
    ]
