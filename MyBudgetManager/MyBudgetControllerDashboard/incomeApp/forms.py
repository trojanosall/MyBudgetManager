from django import forms

from .models import Incomes


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Incomes
        fields = ('registrationDate', 'dateOfPayment',
                  'amount', 'description', 'category',)
        widgets = {
            'registrationDate': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'dateOfPayment': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'amount': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'description': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'category': forms.Textarea(attrs={'cols': 20, 'rows': 20})
        }


class IncomesFormFilter(forms.Form):
    id = forms.CharField(required=False)
    registrationDate = forms.CharField(required=False)
    dateOfPayment = forms.CharField(required=False)
    amount = forms.CharField(required=False)
    description = forms.CharField(required=False)
    category = forms.CharField(required=False)
