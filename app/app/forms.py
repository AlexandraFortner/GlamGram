from django import forms
from app.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', )