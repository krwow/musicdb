from django.contrib import admin
from .models import Album, Track

# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("album_title",)}

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def get_album_title(self, obj):
        return obj.from_album.album_title

    get_album_title.short_description = 'Album title'

    list_display = ('title', 'get_album_title',)