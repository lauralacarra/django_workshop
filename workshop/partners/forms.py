from django import forms
from .models import Partner


class PartnerForm(forms.ModelForm):

    class Meta:
        model = Partner
        exclude = ('created_date', )


