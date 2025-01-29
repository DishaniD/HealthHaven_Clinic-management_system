# Generated by Django 3.2.6 on 2022-06-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsample', '0005_auto_20220613_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
