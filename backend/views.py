from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
import os
from django.conf import settings
# from .form import ImageUploadForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import Staffs,Stays,Guests,Rooms,Menus
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
#services overview
def services(request):
    restaurant_menus = [
        {"name": "Breakfast Buffet", "description": "Start your day with our fresh breakfast.", "image_url": "https://storage.googleapis.com/gen-atmedia/3/2017/01/369383bca2cbf05c3f9656d00ddefdbd51b38031.jpeg"},
        {"name": "Seafood Special", "description": "Delicious seafood prepared by top chefs.", "image_url": "https://thecornishfishmonger.co.uk/cdn/shop/files/Fruits_De_Mer_Selection_Single.jpg?v=1741011304&width=1214"},
        {"name": "Dessert Bar", "description": "Cakes, pastries, and ice cream galore!", "image_url": "https://bakingmelazy.com/wp-content/uploads/2020/12/dessert-bar-full-1-1024x768.jpg"},
    ]
    housekeeping_services = [
        {"name": "Room Cleaning", "description": "Request a full room cleaning service.", "image_url": "https://www.thespruce.com/thmb/fBOdyMFmEBHusOiO6Ryep-Ud9I0=/4000x2667/filters:no_upscale()/SPR-how-to-deep-cleaning-house-7152794-Hero-01-e5cd99973ec24e69b00b5ee6b992f760.jpg"},
        {"name": "Laundry Service", "description": "We'll take care of your clothes.", "image_url": "https://www.marketresearchintellect.com/images/blogs/top-dry-cleaning-and-laundry-services.webp"},
        {"name": "Towel Change", "description": "Fresh towels on demand.", "image_url": "https://motionarray.imgix.net/housekeeper-entering-hotel-room-for-clea-1804484-high_0008.jpg?w=660&q=60&fit=max&auto=format"},
    ]
    other_services = [
        {"name": "Transportation", "description": "Convenient transportation.", "image_url": "https://image-tc.galaxy.tf/wijpeg-1ffkk49ev5r19ar5gzhl4r6de/shuttle_standard.jpg?crop=106%2C0%2C1708%2C1281"},
        {"name": "Swimming Pool", "description": "Relax and Feel our swimming pool, even for kids", "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/92/Backyardpool.jpg"},
        {"name": "Tour Guide", "description": "Explore the city with our experts.", "image_url": "https://images.unsplash.com/photo-1518684079-3c830dcef090"},
    ]
    return render(request, "servicesOverview.html", {
        "restaurant_menus": restaurant_menus,
        "housekeeping_services": housekeeping_services,
        "other_services": other_services,
    })
#menu List Overview
def menu_list(request):
    menus = Menus.objects.all().order_by('menuName')  # sorted alphabetically
    return render(request, 'menu_list.html', {'menus': menus})

#bookingList route
@managerSession_required('staff_ID')
def bookingList(request):
    return render(request,"bookingsList.html")
#service requests List
@managerSession_required('staff_ID')
def servicesList(request):
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