from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.conf import settings

from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


from .forms import UploadForm
from .helpers.plot_utils import plot_points
from .helpers.file_handler import save_file
from .helpers.eeg_processsing import return_epochs

class HomeView(TemplateView):
    template_name='eeg_app/home.html'

class SignupView(CreateView):
    form_class: UserCreationForm
    template_name='eeg_app/register.html'
    success_url='/home'

class SystemLoginView(LoginView):
    template_name='eeg_app/login.html'



def upload_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            fname = save_file(request.FILES['file'], 
                str(request.FILES['file']), settings.MEDIA_ROOT)
            eps = return_epochs(fname)
            print(eps)
        return HttpResponseRedirect('post_upload')
    else:
        form = UploadForm()
    
    return render(request, 'eeg_app/upload.html', {'form': form})

def post_upload(request):
    plot_div = plot_points()
    
    return render(request, 'eeg_app/show_graph.html', context={'plot_div': plot_div})

def download_file(request):
    fileResponse = FileResponse(open(settings.MEDIA_ROOT + '/test_generator.edf', 'rb'), as_attachment=True)
    return fileResponse