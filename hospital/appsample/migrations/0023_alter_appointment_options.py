# Generated by Django 3.2.6 on 2022-06-14 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsample', '0022_alter_appointment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'permissions': [('view_all', 'Can view all appointments'), ('view_future', 'Can view all future appointments')]},
        ),
    ]
