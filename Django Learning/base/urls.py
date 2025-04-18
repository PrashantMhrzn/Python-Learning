from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('contactus/', contact_us),
    path('about/', about_us),
    path('home/', home),
    path('/', base),
    path('views/', view),
    # path('create/', create),

]