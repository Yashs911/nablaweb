# Generated by Django 3.0.7 on 2020-06-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("album", "0004_remove_album_view_counter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="level",
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="album",
            name="lft",
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="album",
            name="rght",
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
