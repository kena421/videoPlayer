from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from main.models import Document
from main.forms import DocumentForm
# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
        # print("form",form)
    return render(request, 'main/index.html', {
        'form': form
    })