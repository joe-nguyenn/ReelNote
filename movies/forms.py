from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'date_watched', 'rating', 'review']
        widgets = {
            'date_watched': forms.DateInput(attrs={'type': 'date'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'review': forms.Textarea(attrs={'rows': 4})
        }

