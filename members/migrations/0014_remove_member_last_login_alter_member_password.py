# Generated by Django 5.1.2 on 2024-12-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_remove_member_password_member_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='member',
            name='Password',
            field=models.CharField(max_length=255),
        ),
    ]
