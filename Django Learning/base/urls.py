from django.urls import path
from .views import index, contact_us, about_us, home, base

urlpatterns = [
    path('index/', index),
    path('contactus/', contact_us),
    path('about/', about_us),
    path('home/', home),
    path('/', base),

]