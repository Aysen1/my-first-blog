# Generated by Django 2.0.7 on 2018-07-09 06:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180709_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 9, 6, 16, 9, 919319, tzinfo=utc)),
        ),
    ]
