from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('contactus/', contact_us),
    path('about/', about_us),
    path('home/', home),
    path('/', base),
    path('task/', task),
    path('task/create/', create),
    # path('create/', create),

]