# Generated by Django 3.2.6 on 2022-06-13 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsample', '0010_auto_20220613_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
    ]
