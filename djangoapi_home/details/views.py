from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.

def profile_list(request):
    profiles =  Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return JsonResponse(serializer.data, safe=False)
