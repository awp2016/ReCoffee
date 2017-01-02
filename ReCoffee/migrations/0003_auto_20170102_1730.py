# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReCoffee', '0002_auto_20170102_1652'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shop',
            new_name='ShopProfile',
        ),
    ]
