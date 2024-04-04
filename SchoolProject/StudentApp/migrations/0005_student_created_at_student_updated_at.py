# Generated by Django 5.0.3 on 2024-04-02 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0004_student_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 4, 2, 15, 42, 29, 563464, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
