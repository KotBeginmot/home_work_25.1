from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, response, serializers
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from course.models import Payments
from users.models import User
from users.serializer import UserSerializer, CreateUserSerializer, UserDetailSerializer, SelfUserDetailSerializer
from users.services import user_create


class UserViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny, ]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request):
        user_create(request)
        password = request.data.pop('password')
        obj = User.objects.create(**request.data)
        obj.set_password(password)
        obj.save()
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


class MyObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
