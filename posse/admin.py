from django.contrib import admin
from .models import WarcraftLogsSettings, RaiderIOSettings, GuildNews, HelpfulGuildLinks, GuildAddonLinks, GuildApplications, BlizzardApiSettings, GuildInformation, GuildLeadership, GuildMOTD, ShadowlandsClassChart

admin.site.register(WarcraftLogsSettings)
admin.site.register(RaiderIOSettings)
admin.site.register(GuildNews)
admin.site.register(HelpfulGuildLinks)
admin.site.register(GuildAddonLinks)
admin.site.register(GuildApplications)
admin.site.register(BlizzardApiSettings)
admin.site.register(GuildInformation)
admin.site.register(GuildLeadership)
admin.site.register(GuildMOTD)
admin.site.register(ShadowlandsClassChart)