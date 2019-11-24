from django.forms import ModelForm
from .models import GuildApplications


class ApplicationForm(ModelForm):
    class Meta:
        model = GuildApplications
        fields = ['character_armory_link', 'discord_username']