# Generated by Django 5.1.2 on 2024-12-03 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_member_last_login_member_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='Password',
        ),
    ]
