# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Roll_No',
            field=models.CharField(max_length=50),
        ),
    ]
