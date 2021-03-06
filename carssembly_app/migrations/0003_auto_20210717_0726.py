# Generated by Django 2.2 on 2021-07-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carssembly_app', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='interest',
            field=models.ManyToManyField(related_name='interests', to='carssembly_app.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='join',
            field=models.ManyToManyField(related_name='joins', to='carssembly_app.User'),
        ),
    ]
