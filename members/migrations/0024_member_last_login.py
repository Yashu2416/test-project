# Generated by Django 5.1.2 on 2024-12-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0023_remove_member_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
