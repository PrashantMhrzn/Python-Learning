from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contact_us(request):
    return HttpResponse('Contact us here')

def about_us(request):
    return HttpResponse('Hi we are learning Django!')

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')
# Create your views here.
