# Generated by Django 4.2.3 on 2023-07-24 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realstate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='maintanance_charge_per_month',
        ),
    ]
