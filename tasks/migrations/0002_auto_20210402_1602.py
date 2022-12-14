# Generated by Django 3.1.7 on 2021-04-02 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
        migrations.AddField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='important',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='memo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
