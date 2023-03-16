from django.forms import ModelForm
from .models import Package
from django.core.exceptions import ValidationError
from django import forms
from datetime import date


class AddPackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'


class DateForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    def clean_date(self):
        date = self.cleaned_data['date']
        if date.weekday() in [5, 6]:
            raise ValidationError("Weekend dates are not allowed")
        if date < date.today():
            raise ValidationError("Date cannot be in the past")
        return date
