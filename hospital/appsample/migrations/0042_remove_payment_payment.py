# Generated by Django 3.2.6 on 2022-06-18 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsample', '0041_alter_invoiceservice_multiple'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment',
        ),
    ]
