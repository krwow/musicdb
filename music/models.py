from email.policy import default
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
# importing validationerror
from django.core.exceptions import ValidationError

def validate_year(value):
    if value > 1900 and value < 2050:
        return value
    else:
        raise ValidationError('Enter the correct year value!')

def validate_number_of_discs(value):
    if value > 0 and value < 20:
        return value
    else:
        raise ValidationError('Enter the correct number of discs value!')

def validate_number_of_tracks(value):
    if value > 0 and value < 150:
        return value
    else:
        raise ValidationError('Enter the correct number of tracks value!')

class Album(models.Model):
    album_title = models.CharField(max_length=100)
    album_artist = models.CharField(max_length=100)
    release_year = models.IntegerField(validators=[validate_year])
    genre = models.CharField(max_length=100, default = 'Unknown')
    number_of_discs = models.IntegerField(validators=[validate_number_of_discs], default = 1)
    number_of_tracks = models.IntegerField(validators=[validate_number_of_tracks])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='user_albums',
                                on_delete=models.CASCADE)
    compilation = models.BooleanField(default = False)
    RATING_CHOICES = (
        ('empty', 'Unrated'),
        ('0', '☆☆☆☆☆'),
        ('1', '★☆☆☆☆'),
        ('2', '★★☆☆☆'),
        ('3', '★★★☆☆'),
        ('4', '★★★★☆'),
        ('5', '★★★★★'),
    )
    rating = models.CharField(max_length=7,
                            choices=RATING_CHOICES,
                            default='empty')

    class Meta:
        ordering = ('album_title',)

    def __str__(self):
        return self.album_title

    def get_absolute_url(self):
        return reverse('music:album_detail',
                        args=[self.created.year,
                        self.created.strftime('%m'),
                        self.created.strftime('%d'),
                        self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.album_title)
        super().save(*args, **kwargs)


class Track(models.Model):
    from_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    track_number = models.IntegerField(validators=[validate_number_of_tracks])
    length = models.CharField(max_length=7, blank=True)
    RATING_CHOICES = (
        ('empty', 'Unrated'),
        ('0', '☆☆☆☆☆'),
        ('1', '★☆☆☆☆'),
        ('2', '★★☆☆☆'),
        ('3', '★★★☆☆'),
        ('4', '★★★★☆'),
        ('5', '★★★★★'),
    )
    track_rating = models.CharField(max_length=7,
                            choices=RATING_CHOICES,
                            default='empty')
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ['track_number']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('music:album_detail',
                        args=[self.from_album.created.year,
                        self.from_album.created.strftime('%m'),
                        self.from_album.created.strftime('%d'),
                        self.from_album.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)