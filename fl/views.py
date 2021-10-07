from os import name
from django.contrib import messages
from django.shortcuts import render
from .models import FlUpload
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

# Create your views here.
def index(request):
    if request.method == "POST":
        fl = request.FILES['file']
        fl_name = request.FILES['file'].name
        doc = FlUpload.objects.create(file=fl, name=fl_name)
        doc.save()
        messages.success(request, 'Your file was uploaded successfully!')

    return render(request, 'index.html')

def download(request):
    dnld_file = FlUpload.objects.all()

    return render(request, 'download.html', {'dnld' : dnld_file})

class DelFile(DeleteView):
    model = FlUpload
    context_object_name = 'fl'
    success_url = reverse_lazy('download')
    template_name = 'file_delete.html'