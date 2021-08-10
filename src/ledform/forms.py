from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'titre',
            'description',
            'prix'
        ]
class RawProductForm(forms.Form):
    title = forms.CharField(label="Titre", widget=forms.TimeInput(attrs={"placeholder": ""}))
    description =  forms.CharField(
                            label="Déscription",
                            required=False,
                            widget=forms.Textarea(
                            attrs={
                                "class": "new_class_name two",
                                "id": "my_id",
                                "rows": 20,
                                "cols": 120
                            })
    )
    price = forms.DecimalField()