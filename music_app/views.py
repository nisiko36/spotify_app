from django.shortcuts import render, redirect
from django.views.generic import CreateView
# from api.get_token import get_token
from api.noname import test
from api.create_playlist import create_playlist
from .models import SpotifyAlarmModel
from django.urls import reverse_lazy




# Create your views here.
def homefunc(request):
    zuruionna = test()
    context = {'test':zuruionna}
    # create_playlist()
    return render(request, 'home.html',  context)

def listfunc(request):
    object = SpotifyAlarmModel.objects.all()
    context = {'object': object,}
    return render(request, 'list.html', context)

def detailfunc(request,pk):
    object = SpotifyAlarmModel.objects.get(pk=pk)
    context = {'object': object}
    return render(request, 'detail.html', context)

class Create(CreateView):
    template_name = 'create.html'
    model = SpotifyAlarmModel
    fields = ('time','track_name','artist_name','switch')
    success_url = reverse_lazy('create')

def deletefunc(request,pk):
    object = SpotifyAlarmModel.objects.filter(pk=pk)
    context = {'object':object}
    if request.method == 'POST':
        object.delete()
        return redirect('list')
    else:
        return render(request, 'delete.html', context)


