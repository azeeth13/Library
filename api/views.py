from django.shortcuts import render
from blog.models import *
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serilaizer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.forms import model_to_dict
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .permission import Name




class BooksApi(RetrieveUpdateDestroyAPIView):
    permission_classes=(Name,)
    queryset=Book.objects.all()
    serializer_class=KitoblarSer

class CategoryApi(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategSer


class UserSignup(APIView):
    """Users Api"""
    permission_classes=(IsAdminUser,)
    def get(self,request):
        users=User.objects.all().values()
        return Response({'users':users})
    
    def post(self,request):
        username=request.data['username']
        email=request.data['email']
        password1=request.data['password1']
        password2=request.data['password2']
        if password1==password2:
            new_user=User.objects.create(
                username=username,
                email=email,
                password=password1
            )
        return Response({'users':model_to_dict(new_user)})




class KitoblarCreate(CreateAPIView):
    permission_classes=(AllowAny,)
    queryset=Book.objects.all()
    serializer_class=KitoblarSer







class ApiBooks(APIView):
    """KItoblatr uchun Get so'rovlar uc                                                                                                                                                                                                                                                                 hun"""
    def get(self,request):
        book=Book.objects.all().values()
        return Response({'book':book})


class KitoblarViews(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = KitoblarSer


class KitoblarListCreateViews(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=KitoblarSer

class KitoblarDeleteViews(RetrieveDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=KitoblarSer 

class KitoblarUpdateViews(RetrieveUpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=KitoblarSer

