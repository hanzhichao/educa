# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import courses.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20181113_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
