from django import forms


class PhotoForm(forms.Form):
    '''Returns the form for photos. (docstring for later editing) '''
    photo = forms.ImageField()