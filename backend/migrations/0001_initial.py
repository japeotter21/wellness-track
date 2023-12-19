# Generated by Django 5.0 on 2023-12-19 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caffeine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mg', models.IntegerField(default=0)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(default=0)),
                ('intensity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.FloatField()),
                ('quality', models.BooleanField()),
            ],
        ),
    ]
