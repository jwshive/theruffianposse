import requests
from .models import BlizzardApiSettings
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



