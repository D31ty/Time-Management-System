# Generated by Django 3.1.7 on 2021-04-03 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='datesubmitted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
