from django import forms
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from random import choice
from app.models import Photo


class PhotoForm(forms.ModelForm):
    FILTER_CHOICES = [('blur', 'Blur'), ('sharpen', 'Sharpen')]
    filterChoice = forms.CharField(
        label='Filters:', widget=forms.Select(choices=FILTER_CHOICES))

    class Meta:
        model = Photo
        fields = ('photo', )