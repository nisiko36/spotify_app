from django.urls import path
from .views import homefunc, listfunc, detailfunc, Create, deletefunc, Update

urlpatterns = [
    path('home/', homefunc, name='home'),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create/', Create.as_view(), name='create'),
    path('delete/<int:pk>', deletefunc, name='delete'),
    path('update/<int:pk>', Update.as_view(), name='update'),
]
