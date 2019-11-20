from django.forms import ModelForm
from .models import GuildApplications


class ApplicationForm(ModelForm):
    class Meta:
        model = GuildApplications
        fields = ['character_name', 'character_realm', 'character_class', 'character_role', 'character_level', 'discord_username']