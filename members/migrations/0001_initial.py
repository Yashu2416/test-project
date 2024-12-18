# Generated by Django 5.1.2 on 2024-11-07 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Citycode', models.CharField(max_length=255)),
                ('Cityname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Countrycode', models.CharField(max_length=255)),
                ('Countryname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statecode', models.CharField(max_length=255)),
                ('Statename', models.CharField(max_length=255)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.state'),
        ),
    ]