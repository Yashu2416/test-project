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

class Countrys(APIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: CountrySerializer(many=True)})
    def get(self, request):
        page_cunt = int(request.GET.get("page", 1))
        limit_cunt = int(request.GET.get("limit", 10))
        start_cunt = (page_cunt - 1) * limit_cunt
        end_cunt = limit_cunt * page_cunt
        search_param = request.GET.get("search")
        countrys = Country.objects.all()
        total_countrys = countrys.count()
        if search_param:
            countrys = countrys.filter(title__icontains=search_param)
        serializer = self.serializer_class(countrys[start_cunt:end_cunt], many=True)
        return Response({
            "status": "success",
            "total": total_countrys,
            "page": page_cunt,
            "last_page": math.ceil(total_countrys / limit_cunt),
            "countrys": serializer.data
        })

    @swagger_auto_schema(
        operation_description="Create a new model",
        request_body=CountrySerializer,
        responses={201: CountrySerializer()})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"Country": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CountrysDetail(APIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_countrylist(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except:
            return None
        
    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: CountrySerializer(many=True)})
    def get(self, request, pk):
        countrylist = self.get_countrylist(pk=pk)
        if countrylist == None:
            return Response({"status": "fail", "message": f"Country with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(countrylist)
        return Response({"status": "success", "data": {"Country": serializer.data}})
    
    @swagger_auto_schema(
        operation_description="Update a model",
        request_body=CountrySerializer,
        responses={200: CountrySerializer()})
    def patch(self, request, pk):
        countrylist= self.get_countrylist(pk)
        if countrylist == None:
            return Response({"status": "fail", "message": f"Country with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            countrylist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"Country": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Delete a model"
    )
    def delete(self, request, pk):
        countrylist = self.get_countrylist(pk)
        if countrylist == None:
            return Response({"status": "fail", "message": f"Country with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        countrylist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)