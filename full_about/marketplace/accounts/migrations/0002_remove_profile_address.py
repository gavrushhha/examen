# Generated by Django 4.2.1 on 2024-05-01 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
    ]