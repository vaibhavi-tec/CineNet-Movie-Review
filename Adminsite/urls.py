from django.urls import path

from . import views

urlpatterns = [
    path("indexmain", views.indexmain, name="indexmain"),
    path('movies', views.movies, name='movies'),
    path('mainmovie', views.mainmovie, name='mainmovie'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('categories', views.categories, name='categories'),
    path('language', views.language, name='language'),
    path('review', views.review, name='review'),
    path('add', views.add, name='add'),
    path('fav', views.fav, name='fav'),
    path('movielist', views.movielist, name='movielist'),
    path('password', views.password, name='password'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('userview', views.userview, name='userview'),
    path('videoplay', views.videoplay, name='videoplay'),


    path('login_check/', views.login_view.as_view(), name='login_check'),

    path('api/add_user/', views.AddUserView.as_view(), name='add_user'),

]