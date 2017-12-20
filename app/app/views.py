from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from app.models import Photo
from django.http import HttpRequest, HttpResponse
from app import forms, models


def upload(request):
    '''Photo Form for Upload.'''
    form = forms.PhotoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('app:feed')
    else:
        return render(request, 'app/form.html', {'form': form})


def feed(request):
    '''Main view of feed.'''
    photos = models.Photo.objects.all()
    return render(request, 'app/feed.html', {'photos': photos})