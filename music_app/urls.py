from django.urls import path
from .views import homefunc, listfunc, detailfunc, Create, deletefunc

urlpatterns = [
    path('home/', homefunc, name='home'),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create/', Create.as_view(), name='create'),
    path('delete/<int:pk>', deletefunc, name='delete'),
]
