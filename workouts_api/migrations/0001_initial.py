# Generated by Django 4.0.4 on 2022-04-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('exercises', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=100)),
            ],
        ),
    ]