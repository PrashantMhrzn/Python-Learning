from django.urls import path, include
from .views import *

urlpatterns = [
    # path('all', AllTodo.as_view()),
    # path('all/<id>', DetailTodo.as_view())
    path('all/<pk>', TodoView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'})),
    path('all', TodoView.as_view({'get': 'list', 'post': 'create'}))

]