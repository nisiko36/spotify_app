from django.urls import path
from .views import homefunc

urlpatterns = [
    path('home', homefunc, name='home')
]
