from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profilepic','bio', 'prefname', 'contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'landing_page', 'description', 'live_link', 'design', 'usability', 'creativity', 'content ', 'overall', 'categories', 'technologies', 'posted', 'user')