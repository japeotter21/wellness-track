# Generated by Django 5.0 on 2024-01-28 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alcohol'),
    ]

    operations = [
        migrations.AddField(
            model_name='alcohol',
            name='drankAt',
            field=models.DateTimeField(default='2024-01-27T05:02:06.387082Z'),
        ),
    ]
