from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from app.models import Photo
from django.http import HttpRequest, HttpResponse
from app import form, models
from django import forms


def upload(request):
    '''Photo Form for Upload.'''
    if request.POST or request.FILES:
        form1 = form.PhotoForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('app:feed')
        else:
            return render(request, 'app/form.html', {'form': form1})
    else:
        return render(request, 'app/form.html', {'form': form.PhotoForm()})


def feed(request):
    '''Main view of feed.'''
    photos = models.Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'app/feed.html', {'photos': photos})