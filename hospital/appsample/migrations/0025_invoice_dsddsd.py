# Generated by Django 3.2.6 on 2022-06-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsample', '0024_rename_appointmentnumber_appointment_appo_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='dsddsd',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
