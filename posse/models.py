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


APPLICANT_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Denied', 'Denied'),
]


class GuildApplications(models.Model):
    character_name = models.CharField(max_length=12)
    character_realm = models.CharField(max_length=100)
    character_class = models.CharField(max_length=20)
    character_role = models.CharField(max_length=10)
    character_level = models.IntegerField()
    discord_username = models.CharField(max_length=100)
    application_status = models.CharField(max_length=20, choices=APPLICANT_CHOICES, default=APPLICANT_CHOICES[0][0])

    class Meta:
        verbose_name_plural = 'Guild Applicants'

    def __str__(self):
        return '{} of {}'.format(self.character_name, self.character_realm)
