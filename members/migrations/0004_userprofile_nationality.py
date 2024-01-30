# Generated by Django 4.2.7 on 2024-01-30 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_userprofile_id_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(blank=True, default='', max_length=50, validators=[django.core.validators.RegexValidator(message='Only alphabets are allowed.', regex='^[A-Za-z]*$')]),
        ),
    ]
