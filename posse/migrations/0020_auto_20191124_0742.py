# Generated by Django 2.2.6 on 2019-11-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0019_guildapplications_character_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildapplications',
            name='character_class',
            field=models.CharField(default='None', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guildapplications',
            name='character_item_level_equipped',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guildapplications',
            name='character_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guildapplications',
            name='character_name',
            field=models.CharField(default='None', max_length=12),
            preserve_default=False,
        ),
    ]
