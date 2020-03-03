from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, 'live_app/home.html')

def sessions(request):
    pass

def statistics(request):
    pass

def options(request):
    pass

def api(request):
    pass

