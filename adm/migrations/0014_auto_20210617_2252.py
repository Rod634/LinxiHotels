# Generated by Django 2.2.24 on 2021-06-18 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0013_auto_20210617_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Room'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Service'),
        ),
    ]
