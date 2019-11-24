# Generated by Django 2.2.6 on 2019-11-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posse', '0026_auto_20191124_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildLeadership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=12)),
                ('character_image_url', models.URLField()),
                ('guild_rank', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Guild Leaders',
            },
        ),
    ]
