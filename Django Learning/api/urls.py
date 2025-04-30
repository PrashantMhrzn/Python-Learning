from django.urls import path, include
from .views import *

urlpatterns = [
    path('all', all_todo),
    path('all/<id>', all_detail)
]