# Generated by Django 3.2.6 on 2022-06-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsample', '0029_alter_news_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
