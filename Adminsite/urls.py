from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("indexmain", views.indexmain, name="indexmain"),
    path('movies', views.movies, name='movies'),
    path('mainmovie/<str:mid>/', views.mainmovie, name='mainmovie'),
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
    path('videoplay/<str:mid>/', views.videoplay, name='videoplay'),


    path('login_check/', views.login_view.as_view(), name='login_check'),

    path('api/add_user/', views.AddUserView.as_view(), name='add_user'),
    path('api/delete_user/', views.delete_user.as_view(), name='delete_user'),

    path('api/add_categories/', views.AddCategoriesView.as_view(), name='add_categories'),
    path('api/delete_categories/', views.delete_categories.as_view(), name='delete_categories'),
    path('CategoryView', views.CategoryView.as_view(), name='CategoryView'),

    path('api/add_language/', views.AddLanguageView.as_view(), name='add_language'),
    path('api/delete_language/', views.delete_language.as_view(), name='delete_language'),

    path('api/add_movie/', views.AddMovieView.as_view(), name='add_movie'),
    path('api/delete_movie/', views.DeleteMovieView.as_view(), name='delete_movie'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)