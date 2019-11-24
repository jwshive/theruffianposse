import requests
from .models import BlizzardApiSettings, GuildInformation
from django.forms.models import model_to_dict


def get_or_renew_auth_token():
    api_lookup = BlizzardApiSettings.objects.all().first()
    api_information = model_to_dict(api_lookup)
    client_key = api_information['client_key']
    client_secret = api_information['client_secret']

    r = requests.post(api_information['token_api_url'], dict(grant_type='client_credentials'), auth=(client_key, client_secret)).json()

    return r['access_token']


def get_character_information(character_realm, character_name):
    api_token = get_or_renew_auth_token()
    api_lookup = BlizzardApiSettings.objects.all().first()
    api_information = model_to_dict(api_lookup)
    character_bust_lookup_url = str(api_information['character_media_api_url']).format(character_realm, character_name, api_token)
    character_information_lookup_url = str(api_information['character_profile_api_url']).format(character_realm, character_name, api_token)
    character_bust = requests.get(character_bust_lookup_url).json()
    character_information = requests.get(character_information_lookup_url).json()
    info_dict = {
        'character_name': character_information['name'],
        'character_realm': character_information['realm']['name'],
        'character_class': character_information['character_class']['name'],
        'character_level': character_information['level'],
        'character_item_level_equipped': character_information['equipped_item_level'],
        'character_image_url': character_bust['bust_url']
    }

    return info_dict


def get_guild_members():
    api_token = get_or_renew_auth_token()
    my_guild = GuildInformation.objects.all().first()
    api_lookup = BlizzardApiSettings.objects.all().first()
    my_guild_information = model_to_dict(my_guild)
    api_information = model_to_dict(api_lookup)

    my_guild_lookup = str(api_information['guild_api_url']).format(my_guild_information['guild_main_realm_slug'], my_guild_information['guild_name_slug'],
                                                                                       api_token)
    guild_information = requests.get(my_guild_lookup).json()

    return guild_information


def get_character_bust(character_realm, character_name):
    api_token = get_or_renew_auth_token()
    api_lookup = BlizzardApiSettings.objects.all().first()
    api_information = model_to_dict(api_lookup)
    character_bust_lookup_url = str(api_information['character_media_api_url']).format(character_realm,
                                                                                       str(character_name).lower(), api_token)
    character_bust = requests.get(character_bust_lookup_url).json()

    return character_bust['bust_url']