# Generated by Django 4.2.5 on 2023-09-15 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pr1_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='image',
        ),
    ]
