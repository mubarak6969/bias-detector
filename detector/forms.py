from django import forms
from django.core.exceptions import ValidationError

class DatasetForm(forms.Form):
    name = forms.CharField(max_length=255, label="Dataset Name")
    file = forms.FileField(label="Upload Dataset (CSV, JSON)")

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith(('.csv', '.json')):
            raise ValidationError("Only CSV or JSON files are allowed.")
        return file

class MLModelForm(forms.Form):
    name = forms.CharField(max_length=255, label="Model Name")
    file = forms.FileField(label="Upload Model (Pickle)")

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith('.pkl'):
            raise ValidationError("Only pickle (.pkl) files are allowed.")
        return file