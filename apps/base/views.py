from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    title = "Geeks"
    settings = Settings.objects.latest('id')
    return render(request, 'base/index.html', locals())

def contact(request):
    settings = Settings.objects.latest('id')
    return render(request, 'base/contact.html', locals())
