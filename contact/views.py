from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from django.http import Http404
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status, authentication, permissions


# Create your views here.
class ContactFormList(APIView):
    def get(self,request,format=None):
            user=ContactForm.objects.all()
            serializer=ContactFormSerializer(user,many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
            print("post is called")
            serializer=ContactFormSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)


class CatelogRequestList(APIView):
    def get(self,request,format=None):
            user=CatelogRequest.objects.all()
            serializer=CatelogRequestSerializer(user,many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
            serializer=CatelogRequestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)
