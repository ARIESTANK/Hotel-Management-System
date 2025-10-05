# from django.shortcuts import redirect
# import models as models_base
# def guestSession_required(session_key="guestID"):
#     def decorator(view_func):
#         def _wrapper_view(request, *args, **kwargs):
#             if(request.session.get(session_key)): #session key request
#                 user=models_base.Guests.objects.filter()
