# Generated by Django 2.2.6 on 2019-10-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0002_remove_daysoflogstoshow_days_to_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='daysoflogstoshow',
            name='days_to_show',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
