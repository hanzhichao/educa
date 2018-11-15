# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import courses.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20181113_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, null=True),
        ),
    ]
