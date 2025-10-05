from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
import os
from django.conf import settings
# from .form import ImageUploadForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

#home page route
def home(request):
    return render(request, "home.html")
#bookingList route
def bookingList(request):
    return render(request,"bookingsList.html")
#service requests List
def services(request):
    return render(request,"service.html")
#guestList 
def guestList(request):
    return render(request,"guest.html")
#staffList
def staffList(request):
    return render(request,"staffs.html")
#staff Profile ROute
def staffProfile(request):
    return render(request,"staffProfile.html")





#css file routing
def css_file(request):
    css_path=os.path.join(settings.BASE_DIR, 'static/css/index.css')
    with open(css_path,'r')as css_file:
        css_route=css_file.read()
    return HttpResponse(css_route,content_type="text/css")
#api
