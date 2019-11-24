# Generated by Django 2.2.6 on 2019-11-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0014_blizzardapisettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='blizzardapisettings',
            name='playable_class_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blizzardapisettings',
            name='realms_api_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]