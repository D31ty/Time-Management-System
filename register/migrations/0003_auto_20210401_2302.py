# Generated by Django 3.1.7 on 2021-04-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_useraccount_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]
