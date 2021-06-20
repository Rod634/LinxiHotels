# Generated by Django 2.2.24 on 2021-06-19 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0014_auto_20210617_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='issue_id',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='leave_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='ocupation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(limit_choices_to={'company': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Company')}, on_delete=django.db.models.deletion.CASCADE, to='adm.Room'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluida', 'Concluida'), ('Anulada', 'Anulada')], default='Pendente', max_length=20),
        ),
    ]