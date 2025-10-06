from django.contrib import admin
from django.urls import path
import backend.views as views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginPage/',views.loginPage,name="loginPage"),
    path('',views.home,name="home"),
    path('bookings/',views.bookingList,name="bookingList"),
    path('services/',views.services,name="services"),
    path('guests/',views.guestList,name="guests"),
    path('staffs/',views.staffList,name="staffs"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('staffProfile/',views.staffProfile,name="staffProfile"),
    path('cssFile/',views.css_file,name="css_file"),


# functions
    path('logout/',views.logout,name="logout"),
    path('login/',views.login,name="login"),
    
    ]
