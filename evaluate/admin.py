from django.contrib import admin
from .models import *

admin.site.register(Songs)
admin.site.register(Algos)
admin.site.register(Playlists)
admin.site.register(SongsInPlaylist)
admin.site.register(Ratings)
