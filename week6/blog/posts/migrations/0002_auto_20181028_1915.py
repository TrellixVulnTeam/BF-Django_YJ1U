# Generated by Django 2.0.5 on 2018-10-28 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 19, 15, 30, 920466)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 19, 15, 30, 920466), null=True),
        ),
    ]