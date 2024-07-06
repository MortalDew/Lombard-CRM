from django import forms

from ..models import Loan


class LoanCreateForm(forms.ModelForm):
    client_amount = forms.DecimalField(
        label='Запрашиваемая сумма',
        max_digits=20,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите запрашиваемую сумму',
            'step': '10'
        })
    )
    duration = forms.IntegerField(
        label='Срок займа',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '5',
            'max': '30',
            'placeholder': 'Введите срок займа'
        })
    )
    total_amount = forms.DecimalField(
        label='Общая сумма займа',
        required=True,
        max_digits=8,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'placeholder': 'Здесь выведется общая сумма займа'
        })
    )
    warranty_date = forms.DateField(
        label='Дата гарантийного срока',
        widget=forms.DateInput(attrs={
            'placeholder': 'Введите дату гарантийного срока',
            'id': 'warranty_date',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Loan
        exclude = ['client', 'date_of_expire', 'total_amount', 'status']
