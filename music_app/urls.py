from django.urls import path
from .views import homefunc, listfunc

urlpatterns = [
    path('home/', homefunc, name='home'),
    path('list/', listfunc, name='list')
]
