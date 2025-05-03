from django.urls import path, include
from .views import *

urlpatterns = [
    path('all', AllTodo.as_view()),
    path('all/<id>', DetailTodo.as_view())
]