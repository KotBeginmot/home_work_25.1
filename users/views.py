from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework_simplejwt.views import TokenObtainPairView

from course.models import Payments
from users.models import User
from users.serializer import UserSerializer, CreateUserSerializer, UserDetailSerializer, SelfUserDetailSerializer


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request):
        obj = User.objects.create(**request.data)
        serializer = CreateUserSerializer(obj)
        return response.Response(serializer.data)

    def partial_update(self, request, pk):
        obj = User.objects.get(pk=pk)
        for i, j in request.data.items():
            setattr(obj, i, j)
        obj.save()
        serializer = UserSerializer(obj)
        return response.Response(serializer.data)

    def retrieve(self, request, pk):
        obj = User.objects.get(pk=pk)
        if request.user.email != User.objects.get(pk=pk).email:
            serializer = UserDetailSerializer(obj)
            return response.Response(serializer.data)
        else:
            serializer = SelfUserDetailSerializer(obj)
            return response.Response(serializer.data)

