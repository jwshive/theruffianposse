from django.shortcuts import render
import datetime
from time import mktime
import urllib.request
import json
from .models import WarcraftLogsSettings, RaiderIOSettings, GuildNews, HelpfulGuildLinks, GuildAddonLinks


def get_json_data(json_url):
    req = urllib.request.Request(
        json_url,
        data=None,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as url:
        data = json.loads(url.read().decode())
        return data


def home(request):
    warcraftlog_settings = WarcraftLogsSettings.objects.all().values('days_to_show', 'api_url')
    raiderio_settings = RaiderIOSettings.objects.all().values('api_url')
    guild_news = GuildNews.objects.filter(active=True).order_by('-added_on')
    helpful_links = HelpfulGuildLinks.objects.filter(link_active=True)
    addon_links = GuildAddonLinks.objects.all()

    now = datetime.datetime.now()
    a_month_ago_in_seconds = mktime(
        (now - datetime.timedelta(days=int(warcraftlog_settings[0]['days_to_show']))).timetuple()) * 1000.0

    warcraft_logs_api = warcraftlog_settings[0]['api_url'].format(a_month_ago_in_seconds)
    warcraft_logs_json = get_json_data(warcraft_logs_api)

    guild_raid_rankings = raiderio_settings[0]['api_url']
    guild_raid_rankings = get_json_data(guild_raid_rankings)

    return render(request, 'front_page.html', {'warcraft_logs': warcraft_logs_json, 'guild_raid_rankings': guild_raid_rankings, 'guild_news': guild_news, 'helpful_links': helpful_links, 'addon_links': addon_links})


def read_news(request, id):
    news_post = GuildNews.objects.get(pk=id)
    return render(request, 'read_news.html', {'news_post': news_post})
