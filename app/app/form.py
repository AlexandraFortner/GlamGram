from django import forms
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from random import choice
from app.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', )