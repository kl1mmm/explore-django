# Generated by Django 4.1.7 on 2023-04-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Arctiles",
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
                    "title",
                    models.CharField(
                        default="", max_length=50, verbose_name="Название"
                    ),
                ),
                (
                    "anounce",
                    models.CharField(default="", max_length=250, verbose_name="Анонс"),
                ),
                ("full_text", models.TextField(verbose_name="Статья")),
                ("date", models.DateTimeField(verbose_name="Дата публикации")),
            ],
        ),
    ]
