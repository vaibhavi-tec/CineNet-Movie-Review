from django.shortcuts import render
from django.http import HttpResponse


def indexmain(request):
    return render(request,"admin/indexmain.html",context=None)

def movies(request):
    return render(request,"admin/movies.html",context=None)

def mainmovie(request):
    return render(request,"admin/main movie.html",context=None)

def about(request):
    return render(request,"admin/about.html",context=None)

def contact(request):
    return render(request,"admin/contact.html",context=None)

def signin(request):
    return render(request,"admin/signin.html",context=None)

def signup(request):
    return render(request,"admin/signup.html",context=None)

def dashboard(request):
    return render(request,"admin/dashboard.html",context=None)

def categories(request):
    return render(request,"admin/categories.html",context=None)

def language(request):
    return render(request,"admin/language.html",context=None)

def review(request):
    return render(request,"admin/review.html",context=None)

def add(request):
    return render(request,"admin/add.html",context=None)

def fav(request):
    return render(request,"admin/fav.html",context=None)

def movielist(request):
    return render(request,"admin/movielist.html",context=None)

def password(request):
    return render(request,"admin/password.html",context=None)

def updateprofile(request):
    return render(request,"admin/update profile.html",context=None)

def userview(request):
    return render(request,"admin/userview.html",context=None)

def videoplay(request):
    return render(request,"admin/video play.html",context=None)
# Create your views here.
