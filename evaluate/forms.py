from django import forms
from .models import *

class SongsForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields = ['songTitle', 'songAlbum','songSinger', 'link']

class AlgosForm(forms.ModelForm):
    class Meta:
        model=Algos
        fields = ['algoName']

class PlaylistsForm(forms.ModelForm):
    class Meta:
        model=Playlists
        fields = ['playlistName']


class SongsInPlaylistForm(forms.ModelForm):
    class Meta:
        model=SongsInPlaylist
        fields = ['playlistId', 'songId']


class RatingsForm(forms.ModelForm):
    class Meta:
        model=Ratings
        fields = ['userId', 'playlistId','algoId', 'time', 'R1','R2','R3','R4','R5']


