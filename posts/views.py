from rest_framework import generics
from .models import Posts
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model  # new
from rest_framework import viewsets 
# Create your views here.


class PostList(viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostDetail(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)  # new
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class UserList(viewsets.ModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(viewsets.ModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
