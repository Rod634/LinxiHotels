# Generated by Django 2.2.24 on 2021-06-17 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0003_auto_20210614_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
    ]
