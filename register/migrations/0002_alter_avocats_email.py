# Generated by Django 4.2.8 on 2024-01-27 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("register", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avocats",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
