from django.shortcuts import render
# from api.get_token import get_token
from api.noname import test
from api.create_playlist import create_playlist


# Create your views here.
def homefunc(request):
    context = {'test':test()}
    # create_playlist()
    return render(request, 'home.html',  context)
