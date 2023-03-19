from django.shortcuts import render, get_object_or_404
from .models import Album, Track
# New:
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AlbumCreateForm, TrackAddForm

from django.utils.text import slugify
#from django.urls import reverse

# Create your views here.
@login_required
def album_list(request):
    albums = Album.objects.filter(added_by=request.user)
    return render(request,
                'music/album/list.html',
                {'section': 'albums',
                'albums': albums})

@login_required
def album_detail(request, year, month, day, album):
    album = get_object_or_404(Album, slug=album,
                            created__year=year,
                            created__month=month,
                            created__day=day)
    return render(request,
                'music/album/detail.html',
                {'album': album})

@login_required
def album_create(request):
    if request.method == 'POST':
        # If form has been sent.
        form = AlbumCreateForm(data=request.POST)
        if form.is_valid():
            # Form data are valid.
            cd = form.cleaned_data
            new_album = form.save(commit=False)
            # Assign current user to the item.
            new_album.added_by = request.user
            new_album.save()
            messages.success(request, 'Album has been added.')
            # Redirect to new created item detail view.
            return redirect(new_album.get_absolute_url())
    else:
        form = AlbumCreateForm()
    return render(request,
                'music/album/create.html',
                {'section': 'create',
                'form': form})

@login_required
def add_track(request):
    if request.method == 'POST':
        # If form has been sent.
        # Extra "request.user" for customizing "from_album" in ModelForm.
        form = TrackAddForm(request.user, data=request.POST)
        if form.is_valid():
            # Form data are valid.
            cd = form.cleaned_data
            new_track = form.save(commit=False)
            # Assign current user to the item.
            new_track.added_by = request.user
            new_track.save()
            messages.success(request, 'Track has been added.')
            # Redirect to new created item detail view.
            return redirect(new_track.get_absolute_url())
    else:
        # Extra "request.user" for customizing "from_album" in ModelForm.
        form = TrackAddForm(request.user)
    return render(request,
                'music/album/track.html',
                {'section': 'track',
                'form': form})