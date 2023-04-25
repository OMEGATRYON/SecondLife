from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import CustomUser
from .serializers import CustomUserSerializer
from .models import Listing
from .serializers import ListingSerializer

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ListingListCreate(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


#  SAME HERE DONT FORGET .models --- Listing, Image, Message, Category, ListingCategory
#  SAME HERE DONT FORGET .serializers --- ListingSerializer, ImageSerializer, MessageSerializer, CategorySerializer, ListingCategorySerializer

# class ListingListCreate(generics.ListCreateAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer


# class ListingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer


# class ImageListCreate(generics.ListCreateAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer


# class ImageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer


# class MessageListCreate(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


# class MessageRetrieveUpdateDestroy(generics.Ret