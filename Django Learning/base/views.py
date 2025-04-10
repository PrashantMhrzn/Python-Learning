from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hi')

def contact_us(request):
    return HttpResponse('Contact us here')

def about_us(request):
    return HttpResponse('Hi we are learning Django!')
# Create your views here.
