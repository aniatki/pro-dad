from django.forms import ModelForm
from .models import Package


class AddPackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'