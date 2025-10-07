from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
import os
from django.conf import settings
# from .form import ImageUploadForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import Staffs,Stays,Guests,Rooms
from backend.decorators  import managerSession_required,staffSession_required
# Create your views here.

#login page 
def loginPage(request):
    return render(request,'login.html')
#home page route
def home(request):
    return render(request, "home.html")
#rooms 
def rooms(request):
    return render(request,"roomsOverview.html")


#bookingList route
@managerSession_required('staff_ID')
def bookingList(request):
    return render(request,"bookingsList.html")
#service requests List
@managerSession_required('staff_ID')
def services(request):
    return render(request,"service.html")
#guestList 
@managerSession_required('staff_ID')
def guestList(request):
    return render(request,"guest.html")
#staffList
@managerSession_required('staff_ID')
def staffList(request):
    return render(request,"staffs.html")
#staff Profile ROute
@staffSession_required("staff_ID")
def staffProfile(request):
    return render(request,"staffProfile.html")
#admin Dashboard
@managerSession_required('staff_ID')
def dashboard(request):
    return render(request,"dashboard.html")




#css file routing
def css_file(request):
    css_path=os.path.join(settings.BASE_DIR, 'static/css/index.css')
    with open(css_path,'r')as css_file:
        css_route=css_file.read()
    return HttpResponse(css_route,content_type="text/css")
#api


#functions

def logout(request):
    request.session.flush() #deleting user session 
    return redirect('home')
def login(request):
    email=request.GET.get("email")
    password=request.GET.get("password")
    userData=Staffs.objects.filter(staffEmail=email).first()
    # return HttpResponse(userData)
    if userData.staffPassword == password:
        request.session['staff_ID']=userData.staffID
        return redirect("dashboard")
    else :
        return HttpResponse("Password Not Matched")