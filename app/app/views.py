from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from app.models import Photo
from django.http import HttpRequest, HttpResponse


def feed(request):
    '''Renders a template saying hello. Example view.'''
    return render(request, 'app/feed.html', {'photos': Photo.objects.all()})