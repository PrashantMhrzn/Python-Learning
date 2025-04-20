from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title == '' and description == '':
            context = {
                'error' : 'Both fields are required to submit task'
            }
            return render(request, 'create.html', context)
        
        TodoList.objects.create(title = title, description = description)
        return redirect('/task/')
    return render(request, 'create.html')

def mark(request, pk):
    task = TodoList.objects.get(pk = pk)
    task.is_completed = True
    task.save()
    return redirect('/task/')

def edit(request, pk):
    task = TodoList.objects.get(pk = pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('/task')
    context = {
        "task" : task
    }
    return render(request, 'edit.html', context)

def delete(request, pk):
    task = TodoList.objects.get(pk = pk)
    task.delete()
    task.save()
    return redirect('/task/')
# Create your views here.
