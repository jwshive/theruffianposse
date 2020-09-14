from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class GuildInformation(models.Model):
    guild_name = models.CharField(max_length=100)
    guild_name_slug = models.SlugField(blank=True, null=True)
    guild_main_realm = models.CharField(max_length=100)
    guild_main_realm_slug = models.SlugField(blank=True, null=True)
    guild_ranks_to_query = models.CharField(max_length=100)
    guild_description = models.TextField()

    class Meta:
        verbose_name_plural = 'Guild Information'

    def save(self, *args, **kwargs):
        self.guild_name_slug = slugify(self.guild_name)
        self.guild_main_realm_slug = slugify(self.guild_main_realm)
        super(GuildInformation, self).save(*args, **kwargs)

    def __str__(self):
        return self.guild_name


class BlizzardApiSettings(models.Model):
    client_key = models.CharField(max_length=200)
    client_secret = models.CharField(max_length=200)
    token_api_url = models.URLField()
    character_media_api_url = models.URLField()
    character_profile_api_url = models.URLField()
    guild_api_url = models.URLField()

    class Meta:
        verbose_name_plural = 'Blizzard API Settings'

    def __str__(self):
        return 'Blizzard API Settings'


class WarcraftLogsSettings(models.Model):
    days_to_show = models.IntegerField()
    api_url = models.URLField()

    class Meta:
        verbose_name_plural = 'WarcraftLogs Settings'

    def __str__(self):
        return 'WarcraftLogs Settings'


class RaiderIOSettings(models.Model):
    raid_rankings_api_url = models.URLField()
    raid_progression_api_url = models.URLField()

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
    character_armory_link = models.URLField()
    discord_username = models.CharField(max_length=100)
    character_image_url = models.URLField()
    character_name = models.CharField(max_length=12)
    character_realm = models.CharField(max_length=100)
    character_class = models.CharField(max_length=20)
    character_level = models.IntegerField()
    character_item_level_equipped = models.IntegerField()
    application_status = models.CharField(max_length=20, choices=APPLICANT_CHOICES, default=APPLICANT_CHOICES[0][0])

    class Meta:
        verbose_name_plural = 'Guild Applicants'
        unique_together = [['character_name', 'character_realm']]

    def __str__(self):
        return '{} => {} => {}'.format(self.character_name, self.discord_username, self.application_status)


class GuildLeadership(models.Model):
    character_name = models.CharField(max_length=12)
    character_image_url = models.URLField()
    guild_rank = models.IntegerField()
    character_realm = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Guild Leaders'

    def __str__(self):
        return self.character_name


class GuildMOTD(models.Model):
    guild_motd_desc = models.CharField(max_length=255)
    guild_motd = models.TextField()
    posted_on = models.DateTimeField(auto_created=True)

    class Meta:
        verbose_name_plural = 'Guild Messages of the Day'

    def __str__(self):
        return self.guild_motd_desc


CLASS_CHOICES = [
    ('TANK_DK', 'Tank Death Knight'),
    ('DPS_DK', 'DPS Death Knight'),
    ('TANK_DH', 'Tank Demon Hunter'),
    ('DPS_DH', 'DPS Demon Hunter'),
    ('TANK_DRUID', 'Tank Druid'),
    ('DPS_DRUID', 'DPS Druid'),
    ('HEALER_DRUID', 'Healer Druid'),
    ('HUNTER', 'Hunter'),
    ('MAGE', 'Mage'),
    ('TANK_MONK', 'Tank Monk'),
    ('DPS_MONK', 'DPS Monk'),
    ('HEALER_MONK', 'Healer Monk'),
    ('TANK_PALADIN', 'Tank Paladin'),
    ('DPS_PALADIN', 'DPS Paladin'),
    ('HEALER_PALADIN', 'Healer Paladin'),
    ('HEALER_PRIEST', 'Healer Priest'),
    ('DPS_PRIEST', 'DPS Priest'),
    ('ROGUE', 'Rogue'),
    ('HEALER_SHAMAN', 'Healer Shaman'),
    ('DPS_SHAMAN', 'DPS Shaman'),
    ('WARLOCK', 'Warlock'),
    ('TANK_WARRIOR', 'Tank Warrior'),
    ('DPS_WARRIOR', 'DPS Warrior'),

]


class ShadowlandsClassChart(models.Model):
    username = models.CharField('Current Main Name', max_length=25)
    shadowlands_first_choice = models.CharField('Shadowlands Class First Choice', max_length=50, choices=CLASS_CHOICES)
    shadowlands_second_choice = models.CharField('Shadowlands Class Second Choice', max_length=50, choices=CLASS_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Shadowlands Class Chart'
        unique_together = [['username', 'shadowlands_first_choice']]

    def __str__(self):
        return self.username
