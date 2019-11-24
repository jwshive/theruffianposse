from django.contrib import admin
from .models import WarcraftLogsSettings, RaiderIOSettings, GuildNews, HelpfulGuildLinks, GuildAddonLinks, GuildApplications, BlizzardApiSettings

admin.site.register(WarcraftLogsSettings)
admin.site.register(RaiderIOSettings)
admin.site.register(GuildNews)
admin.site.register(HelpfulGuildLinks)
admin.site.register(GuildAddonLinks)
admin.site.register(GuildApplications)
admin.site.register(BlizzardApiSettings)


