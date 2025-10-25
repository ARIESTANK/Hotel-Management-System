from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
import os
import json
from django.db.models import Count,F,Sum
from django.conf import settings
# from .form import ImageUploadForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import Staffs,Stays,Guests,Rooms,Menus,Bookings,Orders,Services,Transctions
from backend.decorators  import managerSession_required,staffSession_required,guestSession_required,staySession_required,ChefSession_required
from .serializers import StaffsSerializer,GuestsSerializer,RoomSerializer,StaysSerializer,ServiceSerializer,OrdersSerializer
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from datetime import date

# Create your views here.

#api creations

#Auth guest Data creation
@api_view(['GET'])
def authGuest(request):
    guestData=GuestsSerializer(Guests.objects.get(guestID=request.session['user_ID']))
    if guestData:
        return Response(guestData.data)
    else:
        return Response("No AUth User")
    
@api_view(['GET'])
def authStaff(request):
    staffData=StaffsSerializer(Staffs.objects.get(staffID=request.session['staff_ID']))
    if staffData:
        return Response(staffData.data)
    else:
        return Response("No AUth User")
    
@api_view(['GET'])
def StaffByRole(request, role):
    if role in ["Cleaning", "Room Cleaning", "Laundry","Housekeeping"]:
        role = "Housekeeping"
        staffData = Staffs.objects.filter(role=role,status="free")
    else:
        staffData = Staffs.objects.filter(role="Others",status="free")

    serializer = StaffsSerializer(staffData, many=True)  # 👈 ADD many=True

    if staffData.exists():
        return Response(serializer.data)
    else:
        return Response({"message": "No Auth User"})

@api_view(['GET'])
def authStay(request):
    try:
        stay = Stays.objects.get(stayID=request.session['stay_ID'])
        stayData = StaysSerializer(stay).data

        room = stay.roomID
        stayData['room'] = {
            'roomID': room.roomID,
            'roomCode': room.roomCode,
            'building':room.building,
            'type': room.type,
            'price': room.price,
            'status': room.status
        }

        return Response(stayData)
    except Stays.DoesNotExist:
        return Response({"message": "No Auth Stay"}, status=404)

@api_view(['GET'])
def roomTypeProfit(request):
    # Join Rooms and Transactions through Stays
    data = (
        Transctions.objects
        .select_related('stayID__roomID')
        .values(roomType=F('stayID__roomID__type'))
        .annotate(totalProfit=Sum('totalAmount'))
        .order_by('roomType')
    )

    result = list(data)
    return Response(result)

#Room Type Descriptions
@api_view(["GET"])
def roomsData(request):
    roomTypes={
    "Deluxe":{
        "image":"https://www.castlemartyrresort.ie/wp-content/uploads/2020/05/Deluxe-scaled.jpg",
        "description":"Spacious room with premium amenities and city view.",
        "price":"100",
        "additional":{"TV","Free Wifi","AC","Bathtub + rain shower","Electronic key"}
        },
    "Premium":{
        "image":"https://cache.marriott.com/is/image/marriotts7prod/xr-dxbpx-grand-deluxe-21608-28225:Classic-Hor?wid=1920&fit=constrain",
        "description":"Premium Quality and better experience of stays.",
        "price":"120",
        "additional":{"TV","Free Wifi","AC","rain shower","Electronic key","Breakfast",}
    },
    "Standard":{
        "image":"https://cf.bstatic.com/xdata/images/hotel/max1024x768/251287101.jpg?k=10b33cfbb68fdeb6bdba061c7772f84c91802dc59b80675659c9966565b92a89&o=&hp=1",
        "description":"Comfortable room ideal for short stays.",
        "price":"80",
        "additional":{"TV","Free Wifi","AC","rain shower"}
    },
    "Suite":{
        "image":"https://i.pinimg.com/736x/70/a8/ab/70a8ab5aa285df3fa6c8b95d497dadcd.jpg",
        "description":"Luxury suite with separate living area and modern decor.",
        "price":"150",
        "additional":{"TV","Free Wifi","AC","Bathtub + rain shower","Electronic key","Full Meals","Mini Bar"}
    }
    }
    return Response(roomTypes)

@api_view(['GET'])
def roomFilter(request,guestCount,roomType):
    filteredRooms=Rooms.objects.filter(accomodation=guestCount,type=roomType,status="free")
    serializer = RoomSerializer(filteredRooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def stayServiceData(request,stayID):
    serviceData=Services.objects.filter(stayID=stayID)
    serializer = ServiceSerializer(serviceData, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def stayOrderData(request,stayID):
    serviceData=Orders.objects.filter(stayID=stayID)
    serializer = OrdersSerializer(serviceData, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def totalAmount(request,stayID):
    orders=Orders.objects.filter(stayID=stayID)
    totalAmount=0
    for order in orders:
        totalAmount+=order.amount
    services=Services.objects.filter(stayID=stayID)
    stay=Stays.objects.get(pk=stayID)
    room=stay.roomID
    roomCode=f"{room.building}-{room.roomCode}"
    duration=(stay.check_out-stay.check_in).days
    duration+=1
    totalAmount+=duration*room.price
    return Response({
        "totalAmount": totalAmount,
        "roomAmount":duration*room.price,
        "roomCode": roomCode,
        "duration": duration
    })

@api_view(['GET'])
def paymentMethodRevenue(request):
    data = (
        Transctions.objects
        .values('paymentMethod')
        .annotate(total=Sum('totalAmount'))
        .order_by('paymentMethod')
    )
    return Response(list(data))

#login page 
def loginPage(request):
    return render(request,'login.html')
#signup page
def signupPage(request):
    return render(request,'signup.html')
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
    menu_counts = Menus.objects.values('menuType').annotate(total=Count('menuType'))
    menus = Menus.objects.all().order_by('menuName')  # sorted alphabetically
    # print(menu_counts)
    return render(request, 'menu_list.html', {'menus': menus,'menu_count':menu_counts})
#menu list category
def categoryMenu(request, type):
    menus = Menus.objects.filter(menuType=type)
    menu_counts = Menus.objects.values('menuType').annotate(total=Count('menuType'))
    return render(request, 'menu_list.html', {'menus': menus,'menu_count': menu_counts})
#contact_us Page
def contact_us(request):
    return render(request,"contact_us.html")

#create Stay Page
def createStayPage(request):
    return render(request,'createStay.html')

#Stay Lists
def stayList(request):
    stays=Stays.objects.all()
    today = date.today()
    return render(request,'stayList.html',{"stays":stays,"today":today})
#booking page route
@guestSession_required('user_ID')
def booking(request):
    return render(request,"booking.html")
@guestSession_required('user_ID')
def roomDetail(request,roomType):
    return render(request,'roomDetail.html')

@guestSession_required('user_ID')
def guestProfile(request):
    guestID=request.session['user_ID']
    stayID=request.session.get('stay_ID')
    guest=Guests.objects.get(pk=guestID)
    bookings=Bookings.objects.filter(guestID=guest)
    if stayID:
        stay=Stays.objects.get(pk=stayID)
        orders=Orders.objects.filter(stayID=stay)
        services=Services.objects.filter(stayID=stay)
        return render(request,'guestProfile.html',{'bookings':bookings,'orders':orders,'services':services})
    else :
        return render(request,'guestProfile.html',{'bookings':bookings,'orders':[],'services':[]})
    
@staySession_required('user_ID')
def serviceRequestPage(request):
    return render(request,"serviceRequest.html")
#bookingList route
@managerSession_required('staff_ID')
def bookingList(request):
    bookings = Bookings.objects.all().order_by('created_at')
    return render(request,"bookingsList.html",{'bookings':bookings})
#service requests List
@managerSession_required('staff_ID')
def servicesList(request):
    services=Services.objects.all()
    for service in services:
        stay = service.stayID
        if stay:
                # Get the room linked to this stay
            room = Rooms.objects.filter(pk=stay.roomID_id).first()
            if room:                    # Attach roomCode to the order object dynamically
                service.building = room.building
                service.room_code = room.roomCode
    return render(request,"service.html",{'services':services})
#guestList 
@managerSession_required('staff_ID')
def guestList(request):
    guests=Guests.objects.all()
    return render(request,"guest.html",{'guests':guests})
#staffList
@managerSession_required('staff_ID')
def staffList(request):
    staffs=Staffs.objects.all()
    return render(request,"staffs.html",{'staffs':staffs})
#staff Profile ROute
@staffSession_required("staff_ID")
def staffProfile(request):
    return render(request,"staffProfile.html")
#admin Dashboard
@managerSession_required('staff_ID')
def dashboard(request):
    bookings = Bookings.objects.all().order_by('created_at')[:5]
    bookingCount=Bookings.objects.count()
    guestCount=Guests.objects.count()
    staffCount=Staffs.objects.count()
    totalProfit=0
    transactions=Transctions.objects.all()
    for transaction in transactions:
        totalProfit+=transaction.totalAmount
    return render(request,"dashboard.html",{'bookings':bookings,'bookingCount':bookingCount,'staffCount':staffCount,'guestCount':guestCount,'totalProfit':totalProfit})
@managerSession_required('staff_ID')
def roomList(request):
    roomList=Rooms.objects.all()
    return render(request,"roomList.html",{"roomList":roomList})
@ChefSession_required('staff_ID')
def foodOrders(request):
    orders=Orders.objects.all()
    for order in orders:
        # Get the stay linked to this order
        stay = Stays.objects.filter(pk=order.stayID_id).first()
        if stay:
            # Get the room linked to this stay
            room = Rooms.objects.filter(pk=stay.roomID_id).first()
            if room:
                # Attach roomCode to the order object dynamically
                order.building = room.building
                order.room_code = room.roomCode
            else:
                order.building = "N/A"
                order.room_code = "N/A"
        else:
            order.building = "N/A"
            order.room_code = "N/A"
    return render(request,'foodOrders.html',{'orders':orders})

@ChefSession_required('staff_ID')
def foodOrdersWithState(request,state):
    orders=Orders.objects.filter(status=state)
    for order in orders:
        # Get the stay linked to this order
        stay = Stays.objects.filter(pk=order.stayID_id).first()
        if stay:
            # Get the room linked to this stay
            room = Rooms.objects.filter(pk=stay.roomID_id).first()
            if room:
                # Attach roomCode to the order object dynamically
                order.building = room.building
                order.room_code = room.roomCode
            else:
                order.building = "N/A"
                order.room_code = "N/A"
        else:
            order.building = "N/A"
            order.room_code = "N/A"
    return render(request,'foodOrders.html',{'orders':orders})

#css file routing
def css_file(request):
    css_path=os.path.join(settings.BASE_DIR, 'static/css/index.css')
    with open(css_path,'r')as css_file:
        css_route=css_file.read()
    return HttpResponse(css_route,content_type="text/css")
def js_file(request):
    js_path = os.path.join(settings.BASE_DIR, 'static/js/index.js')
    with open(js_path, 'r') as js_file:
        js_route = js_file.read()
    return HttpResponse(js_route, content_type='application/javascript')
#api


#functions
def signup(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    confirm = request.GET.get("confirm")
    name = request.GET.get("fullname")
    nrc = request.GET.get("nrc")

    # in production -> add email unique and password don't match return message 
    if password==confirm:
        guestCreate=Guests.objects.create(guestName=name,guestEmail=email,password=password,guestNRC=nrc)
        guestCreate.save()
        guestData=Guests.objects.filter(guestName=name,guestEmail=email).first()
        request.session["user_ID"] = guestData.guestID
    return redirect("home")



def logout(request):
    request.session.flush() #deleting user session 
    return redirect('home')

def login(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    userData = Staffs.objects.filter(staffEmail=email).first()
    if userData:
        if userData.staffPassword == password:
            request.session['staff_ID'] = userData.staffID
            role = userData.role.strip().lower()
            print(role)
            if role in ["manager", "receptionist"]:
                    return redirect("dashboard")
            elif role == "chef":
                    return redirect("foodOrders")
            elif role == "housekeeping" or role == "others" :
                    return redirect("serviceOrders")
            else:
                    return redirect("home")
        else:
            return HttpResponse("Password Not Matched")

    else:
        guestData = Guests.objects.filter(guestEmail=email).first()
        if guestData and guestData.password == password:
            request.session['user_ID'] = guestData.guestID

            stayData = Stays.objects.filter(guestID=guestData.guestID, status="Unpaid").first()
            if stayData:
                request.session['stay_ID'] = stayData.stayID
            return redirect("home")
        else:
            return HttpResponse("Password is not Matched")


@managerSession_required('staff_ID')
@csrf_exempt
def createRoom(request):
    if request.method == "POST":
        roomCode=request.POST.get("roomCode")
        roomType = request.POST.get("roomType")
        building=request.POST.get("building")
        price = request.POST.get("price")
        accomodation=request.POST.get("accomodation")
        createRoomProcess=Rooms.objects.create(roomCode=roomCode,type=roomType,building=building,price=price,accomodation=accomodation,status="free")
        createRoomProcess.save()
        return redirect("roomsList")
    
@managerSession_required('staff_ID')
@csrf_exempt
def filterRoom(request):
    if request.method=="POST":
        roomType = request.POST.get("roomType")
        accomodation=request.POST.get("accomodation")
        status=request.POST.get("status")
        if not roomType and not accomodation and not status:
            rooms=Rooms.objects.all()
        elif roomType and not accomodation and not status:
            rooms = Rooms.objects.filter(type=roomType)
        elif accomodation and not roomType and not status:
            rooms = Rooms.objects.filter(accomodation=accomodation)
        elif status and not accomodation and not roomType:
            rooms = Rooms.objects.filter(status=status)
        elif roomType and accomodation and not status:
            rooms = Rooms.objects.filter(type=roomType,accomodation=accomodation)
        elif status and accomodation and not roomType:
            rooms = Rooms.objects.filter(status=status,accomodation=accomodation)
        elif roomType and status and not accomodation:
            rooms = Rooms.objects.filter(type=roomType,status=status)
        else:
            rooms = Rooms.objects.filter(status=status,accomodation=accomodation,type=roomType)
        return render(request, "roomList.html", {"roomList": rooms})

@managerSession_required('staff_ID')
@csrf_exempt
def acceptBooking(request):
    if request.method == "POST":
        roomID=request.POST.get('roomID')
        roomData=Rooms.objects.get(pk=roomID)
        bookingID=request.POST.get("bookingID")
        acceptBooking=Bookings.objects.get(bookingID=bookingID)
        acceptBooking.roomID=roomData
        acceptBooking.save()
        roomData.status="Booked"
        roomData.save()
        return redirect('bookingList')

@managerSession_required('staff_ID')
def deleteBooking(request,bookingID):
    bookingData=Bookings.objects.get(bookingID=bookingID)
    # roomData = bookingData.roomID
    # roomData.status = "free"
    # roomData.save()
    bookingData.delete()

    return redirect("bookingList")

@managerSession_required('staff_ID')
def createStay(request,bookingID):
    bookingData=Bookings.objects.get(bookingID=bookingID)
    roomData = bookingData.roomID
    roomData.status="Unavailable"
    roomData.save()
    createStay=Stays.objects.create(check_in=bookingData.checkIn,check_out=bookingData.checkOut,guestID=bookingData.guestID,roomID=bookingData.roomID,guestCount=bookingData.guestCount,status="Unpaid")
    createStay.save()
    bookingData.delete()
    return redirect("roomsList")
    

@staySession_required('stay_ID')
@csrf_exempt
def createOrder(request):
    if request.method == "POST":
        cart_data = request.POST.get("cart_data")
        items = json.loads(cart_data)
        stayID=request.session['stay_ID']
        allAmount=0
        for data in items:
            allAmount += int(data['price']) * int(data['qty'])
        createOrder=Orders.objects.create(menuItems=items,amount=allAmount,stayID_id=stayID,status="Pending")
        createOrder.save()
        return redirect('guestProfile')

@guestSession_required('user_ID')
@csrf_exempt
def createBooking(request):
    if request.method == "POST":
        guest_id = request.session['user_ID']
        guest = Guests.objects.get(pk=guest_id)
        guestCount=request.POST.get("guest_count")
        roomType=request.POST.get("room_type")
        checkIn=request.POST.get("check_in")
        checkOut=request.POST.get("check_out")
        createBooking=Bookings.objects.create(guestID=guest,guestCount=guestCount,roomType=roomType,checkIn=checkIn,checkOut=checkOut)
        createBooking.save()
        return redirect('guestProfile')

@staffSession_required('staff_ID')
def changeState(request,orderID,state):
    if state == "Completed":    
        serviceData=Services.objects.get(pk=orderID)
        serviceData.status=state
        staff=Staffs.objects.get(pk=request.session.get('staff_ID'))
        staff.status="free"
        staff.save()
        serviceData.save()
        return redirect('serviceOrders')
    else:
        orderData=Orders.objects.get(pk=orderID)
        if orderData:
            orderData.status=state
            orderData.save()
        return redirect('foodOrders')

@managerSession_required('staff_ID')
def createStays(request):
    if request.method=="POST":
        guestEmail=request.POST.get("guestEmail")
        guestData=Guests.objects.filter(guestEmail=guestEmail).first()
        guestCount=request.POST.get("accomodation")
        roomID=request.POST.get("roomID")
        room = Rooms.objects.get(pk=roomID)
        # return HttpResponse(room)
        check_in=request.POST.get("check_in")
        check_out=request.POST.get("check_out")
        room.status="Unavailable"
        room.save()
        createStay=Stays.objects.create(guestID=guestData,guestCount=guestCount,roomID=room,check_in=check_in,check_out=check_out,status="Unpaid")
        createStay.save()
    return redirect('stayList')

@staySession_required('user_ID')
def createRequest(request):
    if request.method=="POST":
        type=request.POST.get("serviceType")
        stayID=request.session.get('stay_ID')
        stay = Stays.objects.get(pk=stayID)
        note=request.POST.get("note")
        createRequest=Services.objects.create(type=type,stayID=stay,note=note,status="Pending")
        createRequest.save()
        return redirect("guestProfile")

@managerSession_required('staff_ID')
def createStaff(request):
    if request.method=="POST":
        staffName=request.POST.get("staffName")
        staffEmail=request.POST.get("staffEmail")
        staffPassword=request.POST.get("password")
        role=request.POST.get("role")
        payRoll=request.POST.get("payRoll")

        createStaff=Staffs.objects.create(staffName=staffName,staffEmail=staffEmail,staffPassword=staffPassword,role=role,payRoll=payRoll)
        createStaff.save()
    return redirect("staffs")

@managerSession_required('staff_ID')
def assignStaff(request):
    if request.method == "POST":
        staffID = request.POST.get("staffID")
        serviceID = request.POST.get("serviceID")

        # ✅ get the actual Staff instance
        staff = Staffs.objects.get(pk=staffID)
        staff.status = "Busy"
        staff.save()

        # ✅ get the Service instance
        service = Services.objects.get(pk=serviceID)
        service.status = "Assigned"
        service.staffID = staff  # must assign object, not ID
        service.save()

    return redirect('servicesList')

@staffSession_required('staff_ID')
def serviceOrders(request):
    staffData = Staffs.objects.get(pk=request.session.get('staff_ID'))
    services = Services.objects.filter(staffID=staffData)

    for service in services:
        stay = service.stayID  # ✅ stay is already a Stays object
        if stay and stay.roomID:
            room = stay.roomID  # ✅ roomID is already a Rooms object
            service.building = room.building
            service.room_code = room.roomCode
        else:
            service.building = "N/A"
            service.room_code = "N/A"

    return render(request, 'serviceOrders.html', {'services': services})

@managerSession_required('staff_ID')
def endStay(request):
    if request.method == "POST":
        stayID=request.POST.get("stayID")
        totalAmount=request.POST.get("totalAmount")
        paymentMethod=request.POST.get("paymentType")
        staffID=request.session.get('staff_ID')
        staffData=Staffs.objects.get(pk=staffID)
        orders=Orders.objects.filter(stayID=stayID)
        orders.delete()

        services=Services.objects.filter(stayID=stayID)
        services.delete()
        
        stay=Stays.objects.get(pk=stayID)
        stay.status="Paid"
        stay.save()

        room=stay.roomID
        room.status="free"
        room.save()
        
        transactionCreate=Transctions.objects.create(stayID_id=stayID,totalAmount=totalAmount,paymentMethod=paymentMethod,staffID=staffData)
        transactionCreate.save()
        return redirect('stayList')

@managerSession_required('staff_ID')
def deleteGuest(request, guestID):
    guestData = Guests.objects.get(pk=guestID)
    stayList = Stays.objects.filter(guestID=guestID, status="Unpaid")

    for stay in stayList:
        Orders.objects.filter(stayID=stay.stayID).delete()
        Services.objects.filter(stayID=stay.stayID).delete()

        room = stay.roomID
        room.status = "free"
        room.save()

        stay.delete()

    guestData.delete()
    return redirect('guests')

@managerSession_required('staff_ID')
def deleteRoom(request,roomID):
    updateRoom=Rooms.objects.get(pk=roomID)
    updateRoom.delete()
    return redirect('roomsList')

@managerSession_required('staff_ID')
def updateRoom(request):
    if request.method == "POST":
        roomID=request.POST.get('roomID')
        roomCode=request.POST.get('roomCode')
        building=request.POST.get('building')
        accomodation=request.POST.get('accomodation')
        roomType=request.POST.get('roomType')
        price=request.POST.get('price')

        updateRoom=Rooms.objects.get(pk=roomID)
        updateRoom.roomCode=roomCode
        updateRoom.roomType=roomType
        updateRoom.accomodation=accomodation
        updateRoom.building=building
        updateRoom.price=price

        updateRoom.save()
        return redirect('roomsList')
    
@managerSession_required('staff_ID')
def deleteStaff(request,staffID):
    updateStaff=Staffs.objects.get(pk=staffID)
    updateStaff.delete()
    return redirect('staffList')

@managerSession_required('staff_ID')
def updateStaff(request):
    if request.method == "POST":
        staffID=request.POST.get('staffID')
        staffName=request.POST.get('staffName')
        staffEmail=request.POST.get('staffEmail')
        role=request.POST.get('role')
        payRoll=request.POST.get('payRoll')
        status=request.POST.get('status')
        password=request.POST.get("password")

        updateStaff=Staffs.objects.get(pk=staffID)
        updateStaff.staffName=staffName
        updateStaff.staffEmail=staffEmail
        updateStaff.role=role
        updateStaff.payRoll=payRoll
        updateStaff.status=status
        updateStaff.password=password

        updateStaff.save()
        return redirect('staffs')