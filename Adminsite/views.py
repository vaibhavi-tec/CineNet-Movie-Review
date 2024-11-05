from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Category, Language,Movie, CastMember
from django.views.generic.base import TemplateView


def indexmain(request):
    return render(request,"admin/indexmain.html",context=None)

from django.shortcuts import render, get_object_or_404
from .models import Movie  # Ensure you import the Movie model

def movies(request):
    movie = Movie.objects.all()
    return render(request, "admin/movies.html", {'movie': movie})

def mainmovie(request, mid):
    movie = get_object_or_404(Movie, mid=mid)
    cast_members = movie.cast_members.all()  # Assuming you have a related name for cast members
    return render(request, 'admin/mainmovie.html', {'movie': movie, 'cast_members': cast_members})

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
    category = Category.objects.all()
    return render(request,"admin/categories.html",{'category': category})

def language(request):
    language = Language.objects.all()
    return render(request,"admin/language.html",{'language': language})

def review(request):
    return render(request,"admin/review.html",context=None)

def add(request):
    return render(request,"admin/add.html",context=None)

def fav(request):
    return render(request,"admin/fav.html",context=None)

def movielist(request):
    movie = Movie.objects.all()
    castmember = CastMember.objects.all() 
    return render(request,"admin/movielist.html",{'movie': movie, 'castmember': castmember})

def password(request):
    return render(request,"admin/password.html",context=None)

def updateprofile(request):
    return render(request,"admin/updateprofile.html",context=None)

def userview(request):
    users = User.objects.all()
    return render(request,"admin/userview.html", {'users': users})

# In your views.py
def videoplay(request, mid):
    movie = get_object_or_404(Movie, mid=mid)
    return render(request, 'admin/videoplay.html', {'movie': movie})


# Create your views here.


#...............................................................................................
class login_view(APIView):
    def post(self,request):
        patientname=request.data.get('patientname')
        password=request.data.get('pateintpass')
        pt = User.objects.filter(username=patientname,password=password).values()
        print("********pt: ", pt)
        if len(pt) > 0:
            request.session["userdata"]= pt[0]["username"]
            return JsonResponse({"status":"pass", "user": pt[0]["username"], "role": pt[0]["role"]})
        else:
            return JsonResponse({"status": "fail"})
        
#....................................................................................................

class AddUserView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print("Received data:", data)  # Log incoming data

        # Additional checks for unique constraints can be added here

        user = User(
            email=data.get('email'),
            username=data.get('username'),
            password=data.get('password'),
            role=data.get('role'),
            image=data.get('profile')  # Handle profile image
        )
        user.save()
        
        return JsonResponse({"message": "Signed Up successfully!"})
    
class delete_user(APIView):
    def post(self,request):
        username = request.POST['username']
        User.objects.filter(username=username).delete()
        return JsonResponse({"status":"pass"})

#............................................................................................................

class AddCategoriesView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print("Received data:", data)  # Log incoming data

        # Additional checks for unique constraints can be added here

        category = Category(
            title=data.get('title'),
        )
        category.save()
        
        return JsonResponse({"message": "Categories added successfully!"})

class CategoryView(TemplateView):
    model = Category
    template_name = "categories.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.session.get("category")
        category = Category.objects.get(title=title)
        context['currentuser'] = category.title
        return context
    
class delete_categories(APIView):
    def post(self,request):
        cid = request.POST['cid']
        Category.objects.filter(cid=cid).delete()
        return JsonResponse({"status":"pass"})

#............................................................................................................

class AddLanguageView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print("Received data:", data)  # Log incoming data

        # Additional checks for unique constraints can be added here

        language = Language(
            language=data.get('language'),
        )
        language.save()
        
        return JsonResponse({"message": "Categories added successfully!"})


class delete_language(APIView):
    def post(self,request):
        lid = request.POST['lid']
        Language.objects.filter(lid=lid).delete()
        return JsonResponse({"status":"pass"})
    
#.......................................................................................................................

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

class AddMovieView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        data = request.data
        
        # Validate required fields
        required_fields = ['title', 'description', 'category', 'language', 
                           'director', 'writer', 'stars', 'reviews', 
                           'year', 'duration', 'movie_video', 'castName']
        for field in required_fields:
            if field not in data:
                return Response({"error": f"{field} is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create movie instance
        movie = Movie(
            title=data.get('title'),
            description=data.get('description'),
            category=data.get('category'),
            language=data.get('language'),
            director=data.get('director'),
            writer=data.get('writer'),
            stars=data.get('stars'),
            reviews=data.get('reviews'),
            year=data.get('year'),
            duration=data.get('duration'),
            movie_link=data.get('movie_video'),
        )

        # Handle file uploads
        if 'movie_poster' in request.FILES:
            movie.mimage = request.FILES['movie_poster']

        try:
            movie.save()  # Save the movie to the database

            # Handle cast members
            castNames = data.getlist('castName')  # Expecting a list of names
            castImages = request.FILES.getlist('castImage')  # Expecting a list of image files

            for cast, cimage in zip(castNames, castImages):
                CastMember.objects.create(movie=movie, cast=cast, cimage=cimage)

            return Response({"message": "Movie added successfully!", "movie_id": movie.mid}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteMovieView(APIView):
    def post(self, request):
        mid = request.data.get('mid')
        try:
            Movie.objects.get(mid=mid).delete()
            return JsonResponse({"status": "success", "message": "Movie deleted successfully!"})
        except Movie.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Movie not found!"})