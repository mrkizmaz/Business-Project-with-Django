from django import forms
from .models import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ["company", "position", "qualifications"]

## Daha sonra düzenle!