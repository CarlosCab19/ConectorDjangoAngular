# Generated by Django 5.0.3 on 2024-03-26 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0002_rename_fee_student_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='fee',
        ),
    ]