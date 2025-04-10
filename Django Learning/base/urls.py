from django.urls import path
from .views import index, contact_us, about_us

urlpatterns = [
    path('index/', index),
    path('contactus/', contact_us),
    path('about/', about_us),
]