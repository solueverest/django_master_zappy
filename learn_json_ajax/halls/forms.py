from .models import Video
from django import forms


class Videoform(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {
            'url': 'YouTube URL'
        }


class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label="Search Here...")
