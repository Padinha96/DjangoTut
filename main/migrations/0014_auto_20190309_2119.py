# Generated by Django 2.1.7 on 2019-03-09 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190309_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 9, 21, 19, 27, 303601), verbose_name='date published'),
        ),
    ]
