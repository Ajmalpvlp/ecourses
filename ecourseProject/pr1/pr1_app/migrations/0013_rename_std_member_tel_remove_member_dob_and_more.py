# Generated by Django 4.2.5 on 2023-10-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr1_app', '0012_member_std'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='std',
            new_name='tel',
        ),
        migrations.RemoveField(
            model_name='member',
            name='dob',
        ),
        migrations.AddField(
            model_name='member',
            name='course',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
