from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import User



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
        # Create a new appointment without the appointment_id
        user = User(
            email=data.get('email'),
            username=data.get('username'),
            # appointment_id is not set here, Django will auto-generate it
            password=data.get('password'),
            role=data.get('role')
        )
        user.save()
        # Return a success message
        return JsonResponse({"message": "Signed Up successfully!"})