# Generated by Django 5.1.2 on 2024-12-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_userdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserData',
        ),
        migrations.AddField(
            model_name='member',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='member',
            name='Password',
            field=models.CharField(max_length=128, verbose_name='Password'),
        ),
    ]
