# Generated by Django 4.2.5 on 2023-10-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr1_app', '0011_member_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='std',
            field=models.IntegerField(null=True),
        ),
    ]
