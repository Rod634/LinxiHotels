# Generated by Django 2.2.24 on 2021-06-19 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0016_auto_20210618_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adm.Room'),
        ),
    ]