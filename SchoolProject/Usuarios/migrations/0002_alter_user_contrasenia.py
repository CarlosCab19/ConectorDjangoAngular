# Generated by Django 5.0.3 on 2024-03-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contrasenia',
            field=models.CharField(max_length=128, verbose_name='contrasenia'),
        ),
    ]
