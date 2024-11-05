from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'user/entry.html', context=None)

def signup(request):
    return render(request, 'user/signup.html', context=None)
    #return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
