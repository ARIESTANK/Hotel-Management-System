from django.contrib import admin
from django.urls import path
import backend.views as views
urlpatterns = [
    #api

    path("api/authGuest",views.authGuest,name="authGuest"),
    path('api/roomsData',views.roomsData,name="roomsData"),
    #file routing
    path('cssFile/',views.css_file,name="css_file"),
    path('js_File/', views.js_file, name='js_file'),

    path('',views.home,name="home"),
    path('admin/', admin.site.urls),
    path('loginPage/',views.loginPage,name="loginPage"),
    path('bookings/',views.bookingList,name="bookingList"),
    path('servicesList/',views.servicesList,name="servicesList"),
    path('guests/',views.guestList,name="guests"),
    path('staffs/',views.staffList,name="staffs"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('staffProfile/',views.staffProfile,name="staffProfile"),
    path('rooms/',views.rooms,name="rooms"),
    path('services/',views.services,name="services"),
    path('menuList/', views.menu_list, name='menuList'),
    path('menuList/<str:type>',views.categoryMenu,name="categoryMenu"),
    path('contactUs/',views.contact_us,name="contactUs"),
    path('booking/',views.booking,name="booking"),
    path('roomDetail/<str:roomType>',views.roomDetail,name="roomDetail"),
    path('guestProfile/',views.guestProfile,name="guestProfile"),
    path('roomsList/',views.roomList,name="roomsList"),
# functions
    path('logout/',views.logout,name="logout"),
    path('login/',views.login,name="login"),
    path('createRoom/',views.createRoom,name="createRoom"),
    path('filterRooms/',views.filterRoom,name="filterRoom"),
    path('createOrder/',views.createOrder,name="createOrder"),
    ]
