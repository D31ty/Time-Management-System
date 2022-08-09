# Generated by Django 3.1.7 on 2021-04-02 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_useraccount_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='role',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='adhar',
            field=models.IntegerField(default=10, unique=True, verbose_name='adhar number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='phone',
            field=models.IntegerField(verbose_name='phone number'),
        ),
    ]