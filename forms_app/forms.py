from django import forms
from .models import FormModel


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = {'name', 'recipe', 'timeCook', }
