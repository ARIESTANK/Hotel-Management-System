from django.shortcuts import redirect
import backend.models as models_base
#  for staffs
def staffSession_required(session_key="staff_ID"):
    def decorator(view_func):
        def _wrapper_view(request, *args, **kwargs):
            if(request.session.get(session_key)): #session key reques
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home') # no session data
        return _wrapper_view
    return decorator

# for manager and receptionist
def managerSession_required(session_key="staff_ID"):
    def decorator(view_func):
        def _wrapper_view(request, *args, **kwargs):
            if(request.session.get(session_key)): #session key request
                user=models_base.Staffs.objects.filter(staffID=request.session[session_key]).first()
                if user.role=="Manager" or user.role=="Receptionist":
                    return view_func(request, *args, **kwargs)
                else :
                    return redirect('home')
            else:
                return redirect('home') # no session data
        return _wrapper_view
    return decorator
#for chefs
def ChefSession_required(session_key="staff_ID"):
    def decorator(view_func):
        def _wrapper_view(request, *args, **kwargs):
            if(request.session.get(session_key)): #session key request
                user=models_base.Staffs.objects.filter(staffID=request.session[session_key]).first()
                if user.role=="Chef":
                    return view_func(request, *args, **kwargs)
                else :
                    return redirect('home')
            else:
                return redirect('home') # no session data
        return _wrapper_view
    return decorator

def guestSession_required(session_key="user_ID"):
    def decorator(view_func):
        def _wrapper_view(request, *args, **kwargs):
            if(request.session.get(session_key)): #session key request
                user=models_base.Guests.objects.filter(guestID=request.session[session_key]).first()
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home') # no session data
        return _wrapper_view
    return decorator

def staySession_required(session_key="stay_ID"):
    def decorator(view_func):
        def _wrapper_view(request, *args, **kwargs):
            if(request.session.get(session_key)): #session key request
                user=models_base.Stays.objects.filter(stayID=request.session[session_key]).first()
                return view_func(request, *args, **kwargs)
            else:
                return redirect('home') # no session data
        return _wrapper_view
    return decorator
