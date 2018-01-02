from django import forms
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from random import choice
from app.models import Photo


class PhotoForm(forms.ModelForm):
    FILTER_CHOICES = [
        ('none', 'None'),
        ('blur', 'Blur'),
        ('sharpen', 'Sharpen'),
        ('contour', 'Contour'),
        ('detail', 'Detail'),
        ('edge_enhance', 'Edge Enhance'),
        ('edge_enhance_more', 'Edge Enhance More'),
        ('emboss', 'Emboss'),
        ('find_edges', 'Find Edges'),
        ('smooth', 'Smooth'),
        ('smooth_more', 'Smooth More'),
    ]
    filterChoice = forms.CharField(
        label='Filters:', widget=forms.Select(choices=FILTER_CHOICES))

    class Meta:
        model = Photo
        fields = ('photo', )