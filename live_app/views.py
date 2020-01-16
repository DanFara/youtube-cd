from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, 'live_app/home.html')