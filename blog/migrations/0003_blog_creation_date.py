# Generated by Django 4.0.3 on 2022-04-15 21:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 15, 21, 9, 47, 468069, tzinfo=utc)),
        ),
    ]
