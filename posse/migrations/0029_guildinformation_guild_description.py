# Generated by Django 2.2.6 on 2019-11-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0028_guildleadership_character_realm'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildinformation',
            name='guild_description',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]