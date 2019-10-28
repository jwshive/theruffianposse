# Generated by Django 2.2.6 on 2019-10-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaysOfLogsToShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_to_show', models.IntegerField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Number of Days to show for Warcraft Logs',
            },
        ),
    ]
