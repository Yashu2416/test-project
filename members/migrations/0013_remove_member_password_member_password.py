# Generated by Django 5.1.2 on 2024-12-06 08:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_remove_member_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.AddField(
            model_name='member',
            name='Password',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='Password'),
            preserve_default=False,
        ),
    ]