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

def task(request):
    obj = TodoList.objects
    tasks = obj.all()
    all = obj.all().count() 
    completed  = obj.filter(is_completed = True).count()
    not_completed  = obj.filter(is_completed = False).count()
    context = {
        'tasks': tasks,
        'all' : all,
        'completed' : completed,
        'not_completed' : not_completed
    }
    return render(request, 'task.html', context)

def create(request):
    return render(request, 'create.html')
# Create your views here.
