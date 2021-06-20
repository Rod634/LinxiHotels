# Generated by Django 2.2.24 on 2021-06-19 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0019_auto_20210618_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='abode',
            name='status',
            field=models.CharField(choices=[('Concluida', 'Concluida'), ('Em andamento', 'Em andamento')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='abode',
            name='Reservation',
            field=models.ForeignKey(limit_choices_to={'status': 'Pendente'}, on_delete=django.db.models.deletion.CASCADE, to='adm.Reservation'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluida', 'Concluida'), ('Anulada', 'Anulada')], max_length=20),
        ),
    ]
