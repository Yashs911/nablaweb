# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-04 21:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bedpres', '0007_remove_bedpres_view_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedpres',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Vises kun i artikkelen. Man kan her bruke <a href="http://en.wikipedia.org/wiki/Markdown" target="_blank">markdown</a> for å formatere teksten.', verbose_name='brødtekst'),
        ),
        migrations.AlterField(
            model_name='bedpres',
            name='lead_paragraph',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Vises på forsiden og i artikkelen', verbose_name='ingress'),
        ),
    ]
