from django import forms
from PIL import Image, ImageFont, ImageDraw, ImageFilter
# from random import choice
from app.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', )


# class Filters(forms.Form):
#     FILTER_CHOICES = [
#         ('none', 'None'),
#         ('blur', 'Blur'),
#         ('sharpen', 'Sharpen'),
#         ('contour', 'Contour'),
#         ('detail', 'Detail'),
#         ('edge_enhance', 'Edge Enhance'),
#         ('edge_enhance_more', 'Edge Enhance More'),
#         ('emboss', 'Emboss'),
#         ('find_edges', 'Find Edges'),
#         ('smooth', 'Smooth'),
#         ('smooth_more', 'Smooth More'),
#     ]
#     filterChoice = forms.CharField(
#         label='Filters:', widget=forms.Select(choices=FILTER_CHOICES))


class Filters(forms.Form):
    FilterChoices = [('', ''), ('BLUR', 'BLUR'), ('CONTOUR', 'CONTOUR'),
                     ('DETAIL', 'DETAIL'), ('EDGE_ENHANCE', 'EDGE_ENHANCE'),
                     ('EDGE_ENHANCE_MORE', 'EDGE_ENHANCE_MORE'), ('EMBOSS',
                                                                  'EMBOSS'),
                     ('FIND_EDGES', 'FIND_EDGES'), ('SMOOTH', 'SMOOTH'),
                     ('SMOOTH_MORE', 'SMOOTH_MORE'), ('SHARPEN', 'SHARPEN')]
    f = forms.ChoiceField(choices=FilterChoices)

    def apply_filter(self):
        return {
            'BLUR': ImageFilter.BLUR,
            'CONTOUR': ImageFilter.CONTOUR,
            'DETAIL': ImageFilter.DETAIL,
            'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
            'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
            'EMBOSS': ImageFilter.EMBOSS,
            'FIND_EDGES': ImageFilter.FIND_EDGES,
            'SMOOTH': ImageFilter.SMOOTH,
            'SMOOTH_MORE': ImageFilter.SMOOTH_MORE,
            'SHARPEN': ImageFilter.SHARPEN
        }.get(self.cleaned_data['f'], None)