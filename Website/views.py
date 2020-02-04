from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class HomeView(generic.ListView):
    template_name = 'site/index.html'
