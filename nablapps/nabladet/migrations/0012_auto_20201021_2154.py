# Generated by Django 3.0.7 on 2020-10-21 21:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabladet', '0011_protect_nablad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nablad',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='brødtekst'),
        ),
    ]
