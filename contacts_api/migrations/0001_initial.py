# Generated by Django 4.0.4 on 2022-04-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excercises', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=100)),
            ],
        ),
    ]
