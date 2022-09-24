from pickle import FALSE
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from user.models import User
from user.serializers import Userserializer
from django.forms.models import model_to_dict

# Create your views here.
class Userview(APIView):
    def get(self ,request):
        userid=request.GET['userid']
        try:
            userdata = User.objects.get(UserID=userid)
        except:
            return JsonResponse("No Data Found",safe=False)
        return JsonResponse(model_to_dict(userdata),safe=False)

    def post(self ,request):
        postdata=request.data
        serialized_userdata=Userserializer(data=postdata)
        if(serialized_userdata.is_valid()):
            serialized_userdata.save()
            return JsonResponse("User Saved",safe=False)
        else:
            return JsonResponse("Incorrect Userdata",safe=False)

    def put(self,request):
        newdata=request.data
        userdata=User.objects.get(EmailID=newdata['EmailID'])
        serialized_userdata= Userserializer(userdata,data=newdata)
        if(serialized_userdata.is_valid()):
            serialized_userdata.save()
            return JsonResponse("User Updated",safe=False)
        else:
            return JsonResponse("Update Error",safe=False)
    
    def delete(self ,request):
        userid=request.GET['userid']
        try:
            userdata = User.objects.get(UserID=userid)
        except:
            return JsonResponse("No Data Found",safe=False)
        userdata.delete()
        return JsonResponse("User deleted successfully",safe=False)