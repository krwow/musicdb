from django import forms
from .models import Album, Track
from django.utils.text import slugify

class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['created', 'updated', 'slug', 'added_by']

class TrackAddForm(forms.ModelForm):
    class Meta:
        model = Track
        exclude = ['created', 'updated', 'slug']
        labels  = {
            'title':'Track title',
            'artist':'Track artist',
            'length':'Track length',
        }