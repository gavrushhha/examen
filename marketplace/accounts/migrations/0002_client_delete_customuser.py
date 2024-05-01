# Generated by Django 4.2.1 on 2024-05-01 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "client",
                "verbose_name_plural": "clients",
            },
        ),
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
