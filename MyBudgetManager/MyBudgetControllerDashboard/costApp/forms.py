from django import forms

from .models import Costs


class CostForm(forms.ModelForm):

    class Meta:
        model = Costs
        fields = ('registrationDate', 'dateOfPayment',
                  'amount', 'description', 'category',)
        widgets = {
            'registrationDate': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'dateOfPayment': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'amount': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'description': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'category': forms.Textarea(attrs={'cols': 20, 'rows': 20})
        }
