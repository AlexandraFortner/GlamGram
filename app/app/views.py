from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from app.models import Photo
from django.http import HttpRequest, HttpResponse
from django.views import View
from app import form, models
from django import forms
from app.form import Filters
from PIL import Image


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


class PictureFilter(View):
    def get(self, request, image_id):
        form = Filters()
        path = 'app/static/' + Photo.objects.get(id=image_id).image_url()
        return render(request, 'app/feed.html', {'form': form})

    def post(self, request, image_id):
        form = Filters(request.POST)
        path = 'app/static/' + Photo.objects.get(id=image_id).image_url()
        image = Image.open(path)
        if form.is_valid():
            f = form.apply_filter()
            image.convert('RGB').filter(f).save(path)
            return redirect('app:feed')
        return render(request, 'app/PictureFilters.html', {'form': form})