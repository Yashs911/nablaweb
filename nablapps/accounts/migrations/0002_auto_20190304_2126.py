# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-04 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_squashed_0009_auto_20171004_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nablauser',
            name='ntnu_card_number',
            field=models.CharField(blank=True, help_text='Dette er et 7-10-sifret nummer på baksiden av kortet.På nye kort er dette sifrene etter EM.På gamle kort er dette sifrene nede til venstre.Det brukes blant annet for å komme inn på bedpresser.', max_length=10, verbose_name='NTNU kortnr'),
        ),
    ]