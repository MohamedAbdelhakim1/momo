# Generated by Django 5.1.4 on 2025-04-23 22:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="image",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="images/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
