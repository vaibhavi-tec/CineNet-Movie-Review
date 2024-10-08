from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'user/entry.html', context=None)


# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from Adminsite.models import User



def indexmain(request):
    return render(request,"user/indexmain.html",context=None)

def movies(request):
    return render(request,"user/movies.html",context=None)

def mainmovie(request):
    return render(request,"user/mainmovie.html",context=None)

def about(request):
    return render(request,"user/about.html",context=None)

def contact(request):
    return render(request,"user/contact.html",context=None)

def dashboard(request):
    return render(request,"user/dashboard.html",context=None)


def fav(request):
    return render(request,"user/fav.html",context=None)



def password(request):
    return render(request,"user/password.html",context=None)

def updateprofile(request):
    return render(request,"user/updateprofile.html",context=None)


def videoplay(request):
    return render(request,"user/videoplay.html",context=None)
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