# Generated by Django 4.2.5 on 2023-09-27 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pr1_app', '0006_alter_member_addrs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='addrs',
        ),
    ]
