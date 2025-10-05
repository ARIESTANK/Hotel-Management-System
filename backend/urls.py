from django.contrib import admin
from django.urls import path
import backend.views as views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('bookings/',views.bookingList,name="bookingList"),
    path('services/',views.services,name="services"),
    path('guests/',views.guestList,name="guests"),
    path('staffs/',views.staffList,name="staffs"),
    path('staffProfile/',views.staffProfile,name="staffProfile"),
    path('cssFile/',views.css_file,name="css_file")
]
