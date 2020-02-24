from django import forms
from houseowner.models import housedetail


class HouseDetailForm(forms.ModelForm):
    class Meta:
        model = housedetail
        fields = ['bedrooms', 'bathrooms', 'area', 'expected_rent', 'expected_advance', 'image']