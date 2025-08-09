from django.shortcuts import render, redirect
from .forms import DatasetForm, MLModelForm
from .models import Dataset, MLModel
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

@login_required
def upload_file(request):
    dataset_form = DatasetForm()
    model_form = MLModelForm()
    if request.method == 'POST':
        if 'dataset_submit' in request.POST:
            dataset_form = DatasetForm(request.POST, request.FILES)
            if dataset_form.is_valid():
                dataset = Dataset(
                    user=request.user,
                    name=dataset_form.cleaned_data['name'],
                    file=dataset_form.cleaned_data['file']
                )
                dataset.save()
                return redirect('upload_file')
        elif 'model_submit' in request.POST:
            model_form = MLModelForm(request.POST, request.FILES)
            if model_form.is_valid():
                model = MLModel(
                    user=request.user,
                    name=model_form.cleaned_data['name'],
                    file=model_form.cleaned_data['file']
                )
                model.save()
                return redirect('upload_file')
    return render(request, 'upload.html', {'dataset_form': dataset_form, 'model_form': model_form})