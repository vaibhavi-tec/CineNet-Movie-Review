from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import User, Category
from django.views.generic.base import TemplateView


def indexmain(request):
    return render(request,"admin/indexmain.html",context=None)

def movies(request):
    return render(request,"admin/movies.html",context=None)

def mainmovie(request):
    return render(request,"admin/mainmovie.html",context=None)

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
    return render(request,"admin/categories.html",{'users': category})

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
    return render(request,"admin/updateprofile.html",context=None)

def userview(request):
    users = User.objects.all()
    return render(request,"admin/userview.html", {'users': users})

def videoplay(request):
    return render(request,"admin/videoplay.html",context=None)
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

class UserDoctorView(TemplateView):
    model = User
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
        