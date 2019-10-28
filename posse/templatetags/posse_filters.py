from django import template
import datetime


ZONE_NAMES = {
    -1: 'UnknownZone',
    24: 'Ny\'alotha',
    23: 'The Eternal Palace',
    22: 'Crucible of Storms',
    21: 'Battle of Dazar\'alor ',
    20: 'Mythic+ Dungeons',
    19: 'Uldir',
    17: 'Antorus, The Burning Throne',
    13: 'Tomb of Sargeras',
    12: 'Trial of Valor',
    11: 'The Nighthold',
    10: 'Emerald Nightmare',
}

register = template.Library()


def ctime(s):
    s = (s / 1000)
    s = datetime.datetime.fromtimestamp(s).strftime('%m-%d-%Y')
    return s


def translate_zone_number(s):
    s = ZONE_NAMES[s]
    return s


def replace_dashes(value):
    return value.replace('-', ' ')


register.filter('ctime', ctime)
register.filter('translate_zone_number', translate_zone_number)
register.filter('replace_dashes', replace_dashes)
