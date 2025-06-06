# Generated by Django 5.2.1 on 2025-05-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Human",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="gender"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="last name"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=40,
                        null=True,
                        verbose_name="phone number",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="email"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(upload_to="avatar/", verbose_name="avatar"),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=80, null=True, verbose_name="street"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=60, null=True, verbose_name="city"
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=60, null=True, verbose_name="country"
                    ),
                ),
                (
                    "link_to_details",
                    models.URLField(blank=True, null=True, verbose_name="details"),
                ),
            ],
        ),
    ]
