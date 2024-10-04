from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'user/entry.html', context=None)


# Create your views here.
