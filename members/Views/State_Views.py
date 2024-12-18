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

class States(APIView):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: StateSerializer(many=True)})
    def get(self, request):
        page_stt = int(request.GET.get("page", 1))
        limit_stt = int(request.GET.get("limit", 10))
        start_stt = (page_stt - 1) * limit_stt
        end_stt = limit_stt * page_stt
        search_param = request.GET.get("search")
        states = State.objects.all()
        total_states = states.count()
        if search_param:
            states = states.filter(title__icontains=search_param)
        serializer = self.serializer_class(states[start_stt:end_stt], many=True)
        return Response({
            "status": "success",
            "total": total_states,
            "page": page_stt,
            "last_page": math.ceil(total_states / limit_stt),
            "states": serializer.data
        })

    @swagger_auto_schema(
        operation_description="Create a new model",
        request_body=StateSerializer,
        responses={201: StateSerializer()})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"State": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class StatesDetail(APIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get_statelist(self,pk):
        try:
            return State.objects.get(pk=pk)
        except:
            return None

    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: StateSerializer(many=True)})
    def get(self, request,pk):
        statelist = self.get_statelist(pk=pk)
        if statelist == None:
            return Response({"status": "fail", "message": f"State with Country Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(statelist)
        return Response({"status": "success", "data": {"State": serializer.data}})
    
    @swagger_auto_schema(
        operation_description="Update a model",
        request_body=StateSerializer,
        responses={200: StateSerializer()})
    def patch(self, request,pk):
        statelist= self.get_statelist(pk)
        if statelist == None:
            return Response({"status": "fail", "message": f"State with Country Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            statelist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"State": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Delete a model"
    )
    def delete(self, request,pk):
        statelist = self.get_statelist(pk)
        if statelist == None:
            return Response({"status": "fail", "message": f"State with Country Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        statelist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)