# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReCoffee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='rating',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=1),
        ),
    ]
