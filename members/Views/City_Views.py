from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status, generics
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from members.models import *
from members.serializers import *
# from .encdyc import encrypt_data,decrypt_data
from django.core.exceptions import ObjectDoesNotExist
from members.encryption_utils import encrypt_data,decrypt_data
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password,check_password
import math
from datetime import datetime

class Cities(APIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: CitySerializer(many=True)})
    def get(self, request):
        page_cit = int(request.GET.get("page", 1))
        limit_cit = int(request.GET.get("limit", 10))
        start_cit = (page_cit - 1) * limit_cit
        end_cit = limit_cit * page_cit
        search_param = request.GET.get("search")
        cities = City.objects.all()
        total_cities = cities.count()
        if search_param:
            cities = cities.filter(title__icontains=search_param)
        serializer = self.serializer_class(cities[start_cit:end_cit], many=True)
        return Response({
            "status": "success",
            "total": total_cities,
            "page": page_cit,
            "last_page": math.ceil(total_cities / limit_cit),
            "cities": serializer.data
        })

    @swagger_auto_schema(
        operation_description="Create a new model",
        request_body=CitySerializer,
        responses={201: CitySerializer()})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"City": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CitiesDetail(APIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_citylist(self,pk):
        try:
            return City.objects.get(pk=pk)
        except:
            return None
        
    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: CitySerializer(many=True)})
    def get(self, request,pk):
        citylist = self.get_citylist(pk=pk)
        if citylist == None:
            return Response({"status": "fail", "message": f"City with State Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(citylist)
        return Response({"status": "success", "data": {"City": serializer.data}})
    
    @swagger_auto_schema(
        operation_description="Update a model",
        request_body=CitySerializer,
        responses={200: CitySerializer()})
    def patch(self, request,pk):
        citylist= self.get_citylist(pk)
        if citylist == None:
            return Response({"status": "fail", "message": f"City with State Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            citylist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"City": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Delete a model"
    )
    def delete(self, request,pk):
        citylist = self.get_citylist(pk)
        if citylist == None:
            return Response({"status": "fail", "message": f"City with State Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        citylist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)