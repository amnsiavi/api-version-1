# Generated by Django 5.0.6 on 2024-05-31 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list', '0007_review_alter_streamplatform_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 17, 39, 16, 783608)),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 17, 39, 16, 783608)),
        ),
        migrations.AlterField(
            model_name='streamplatform',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 17, 39, 16, 783608)),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 17, 39, 16, 783608)),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 31, 17, 39, 16, 783608)),
        ),
    ]
