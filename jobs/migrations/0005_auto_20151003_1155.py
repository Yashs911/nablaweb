# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20151003_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='edit_listeners',
            field=models.ManyToManyField(verbose_name='Lyttere', blank=True, help_text='Brukere som overvåker dette objektet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='view_counter',
            field=models.IntegerField(default=0, editable=False, verbose_name='Visninger'),
        ),
    ]
