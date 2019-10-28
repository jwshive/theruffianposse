from django.contrib.auth.models import User
from django.db import models


class WarcraftLogsSettings(models.Model):
    days_to_show = models.IntegerField()
    api_url = models.URLField()

    class Meta:
        verbose_name_plural = 'WarcraftLogs Settings'

    def __str__(self):
        return 'WarcraftLogs Settings'


class RaiderIOSettings(models.Model):
    api_url = models.URLField()

    class Meta:
        verbose_name_plural = 'Raider.IO Settings'

    def __str__(self):
        return 'Raider.IO Settings'


class GuildNews(models.Model):
    news_description = models.CharField(max_length=255)
    news_body = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_created=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Guild News and Updates'

    def __str__(self):
        return self.news_description


class HelpfulGuildLinks(models.Model):
    link_name = models.CharField(max_length=255)
    link_url = models.URLField()
    link_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Helpful Guild Links'

    def __str__(self):
        return self.link_name


class GuildAddonLinks(models.Model):
    addon_name = models.CharField(max_length=255)
    link_url = models.URLField()

    class Meta:
        verbose_name_plural = 'Guild Addon Links'

    def __str__(self):
        return self.addon_name
