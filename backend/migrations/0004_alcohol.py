# Generated by Django 5.0 on 2024-01-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_caffeine_time_alter_exercise_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinks', models.IntegerField(default=0)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
