from django.db import models
import json
# Create your models here.

# Staff Table Attributes
class Staffs(models.Model):
    staffID=models.AutoField(primary_key=True)
    staffName=models.CharField(max_length=255)
    staffEmail=models.EmailField(max_length=255,null=False)
    staffPassword=models.CharField(max_length=255,null=False)
    roles=[('manager','Manager'),('Kitchen Staff','kitchen staff'),('HouseKeeping','housekeeping'),('receptionist','Receptionist')]
    role=models.CharField(max_length=255,choices=roles,default="staff")
    payRoll=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({
            'staffID':self.staffID,
            'staffName':self.staffName,
            'staffEmail':self.staffEmail,
            'staffPassword':self.staffPassword,
            'role':self.role,   
        })

# Room Table Attributes

class Rooms(models.Model):
    roomID=models.AutoField(primary_key=True)
    roomCode=models.CharField(max_length=5,null=False)
    buildingNo=[('A','buildingA'),('B','buildingB'),('C','buildingC'),('D','buildingD'),('E','buildingE'),('F','buildingF')]
    building=models.CharField(max_length=2,choices=buildingNo,default="A")
    accomodation=models.IntegerField(default="1") # amount that can fit in the room
    roomType=[('P', 'premium'),('E', 'economy'),('A', 'average'),('V', 'VIP'),] # room types
    type=models.CharField(max_length=100,null=False,choices=roomType)
    price=models.IntegerField(default=0)
    roomState=[ ('free', 'Free'),('booked', 'Booked'),('unavailable', 'Unavailable'),]
    status=models.CharField(max_length=100,choices=roomState) # room state (eg: if room is unavailable, it shouldn't be booked or served)

    def __str__(self):
        return json.dumps({
            'roomID':self.roomID,
            'roomCode':self.roomCode,
            'building':self.building,
            'accomodation':self.accomodation,
            'type':self.type,
            'price':self.price,
            'status':self.status,
        })
    
# attributes of guest table
class Guests(models.Model):
    guestID=models.AutoField(primary_key=True)
    guestName=models.CharField(max_length=255,null=False)
    guestEmail=models.EmailField(max_length=255,null=False)
    password=models.CharField(max_length=255,null=False)
    guestNRC=models.CharField(max_length=100,null=False)
    guestPh=models.CharField(max_length=11,null=True)
    Address=models.CharField(max_length=255,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return json.dumps({
            'guestID': self.guestID,
            'guestName': self.guestName,
            'guestEmail': self.guestEmail,
            'guestNRC': self.guestNRC,
            'guestPh': self.guestPh,
            'Address': self.Address,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        })
# fact table of guest-room stays
class Stays(models.Model):
    stayID=models.AutoField(primary_key=True)
    guestID=models.ForeignKey(Guests,on_delete=models.CASCADE,db_column='guestID')
    roomID=models.ForeignKey(Rooms,on_delete=models.CASCADE,db_column='roomID')
    check_in=models.DateTimeField(auto_now_add=True)
    check_out=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({
            'stayID':self.stayID,
            'guestID':self.guest.guestID if self.guest else "",
            'roomID':self.room.roomID if self.room else "",
            'check_in':self.check_in,
            'check_out':self.check_out,
        })

# Booking Table

class Bookings(models.Model):
    bookingID=models.AutoField(primary_key=True)
    guestID=models.ForeignKey(Guests,on_delete=models.CASCADE,db_column='guestID')
    roomID=models.ForeignKey(Rooms,on_delete=models.CASCADE,db_column='roomID')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({
            'bookingID': self.bookingID,
            'guestID':self.guest.guestID if self.guest else "",
            'roomID':self.room.roomID if self.room else "",
            'created_at':self.created_at,
        })

# Service that staff(houseKeeping has to do) table 
class Services(models.Model):
    serviceID=models.AutoField(primary_key=True)
    serviceType=[("Transportation",'T'),("Laundary","L"),("Maintainance","M"),("Special Requests"),("HouseKeeping","H")]
    type=models.CharField(max_length=244,choices=serviceType)
    state=[("Pending","P"),("Accepted","A"),("Reject","R")]
    status=models.CharField(max_length=100,choices=state)
    stayID=models.ForeignKey(Stays,on_delete=models.CASCADE,db_column="stayID")
    staffID=models.ForeignKey(Staffs,null=True,on_delete=models.CASCADE,db_column="staffID")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({
            'serviceID':self.serviceID,
            'type':self.type,
            'status':self.status,
            'stayID':self.stay.stayID if self.stay else "",
            'staffID':self.staff.staffID if self.staff else "",
            'create_at':self.created_at,
        })
    
class 