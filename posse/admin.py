from django.contrib import admin
from .models import WarcraftLogsSettings, RaiderIOSettings, GuildNews, HelpfulGuildLinks, GuildAddonLinks

admin.site.register(WarcraftLogsSettings)
admin.site.register(RaiderIOSettings)
admin.site.register(GuildNews)
admin.site.register(HelpfulGuildLinks)
admin.site.register(GuildAddonLinks)


