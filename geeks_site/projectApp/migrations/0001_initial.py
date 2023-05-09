# Generated by Django 4.2.1 on 2023-05-03 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GeeksModel",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("last_modified", models.DateTimeField(auto_now_add=True)),
                ("img", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
