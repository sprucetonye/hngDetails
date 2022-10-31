from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Profile
        fields = ['id', 'slackUsername', 'backend', 'age', 'bio']
        
        
# get_notes(self, obj):
#     from .serializers import ProfileSerialize
# return ProfileSerialize(<from .serializers import Profile>, many=True/False, read_only=True/False).data