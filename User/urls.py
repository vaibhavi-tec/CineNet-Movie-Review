from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("indexmain", views.indexmain, name="indexmain"),
    path('movies', views.movies, name='movies'),
    path('mainmovie', views.mainmovie, name='mainmovie'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('fav', views.fav, name='fav'),
    path('password', views.password, name='password'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('videoplay', views.videoplay, name='videoplay'),


    path('login_check/', views.login_view.as_view(), name='login_check'),

    path('api/add_user/', views.AddUserView.as_view(), name='add_user'),
    path('api/delete_user/', views.delete_user.as_view(), name='delete_user'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)