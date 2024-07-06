from django import forms
from ..models import Category


class CategoryCreateForm(forms.ModelForm):
    category_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите категорию'
        })
    )
    subcategory_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите Подкатегорию'
        })
    )
   
    class Meta:
        model = Category
        exclude = []
