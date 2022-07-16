from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadForm
from .file_utils import plot_points

# Create your views here.

def index(request):
    return HttpResponse("<h1>The Homepage</h1>")

def upload_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            pass 
        return HttpResponseRedirect('post_upload')
    else:
        form = UploadForm()
    
    return render(request, 'eeg_app/upload.html', {'form': form})

def post_upload(request):
    plot_div = plot_points()
    
    return render(request, 'eeg_app/show_graph.html', context={'plot_div': plot_div})