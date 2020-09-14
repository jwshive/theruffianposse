from django.forms import ModelForm
from .models import GuildApplications, ShadowlandsClassChart


class ApplicationForm(ModelForm):
    class Meta:
        model = GuildApplications
        fields = ['character_armory_link', 'discord_username']


class ShadowlandsClass(ModelForm):
    class Meta:
        model = ShadowlandsClassChart
        fields = ['username', 'shadowlands_first_choice', 'shadowlands_second_choice']