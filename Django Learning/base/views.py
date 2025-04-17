from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList

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

def view(request):
    tasks = TodoList.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'view.html', context)
# Create your views here.
