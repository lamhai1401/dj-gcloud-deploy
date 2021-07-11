
from rest_framework import serializers
from django.contrib.auth import get_user_model # new
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'author', 'title', 'body', 'created_at',)


class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model() 
        fields = ('id', 'username',)