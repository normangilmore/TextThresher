# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-11 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thresher', '0006_auto_20161202_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[(b'RADIO', b'Single answer - radio buttons'), (b'CHECKBOX', b'Multiple answer - checkboxes'), (b'DATETIME', b'Date and Time'), (b'DATE', b'Date only'), (b'TIME', b'Time only'), (b'TEXT', b'Text')], max_length=10),
        ),
    ]
