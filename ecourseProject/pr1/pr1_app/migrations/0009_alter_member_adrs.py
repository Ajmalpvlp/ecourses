# Generated by Django 4.2.5 on 2023-09-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr1_app', '0008_member_adrs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='adrs',
            field=models.CharField(max_length=100, null=True),
        ),
    ]