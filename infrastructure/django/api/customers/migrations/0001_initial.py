# Generated by Django 4.1.4 on 2022-12-08 04:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("document", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("birth_date", models.DateTimeField()),
            ],
        ),
    ]
