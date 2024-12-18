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
import logging

logger = logging.getLogger('django')

class Members(APIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: MemberSerializer(many=True)})
    def get(self, request):
        page_mem = int(request.GET.get("page", 1))
        limit_mem = int(request.GET.get("limit", 10))
        start_mem = (page_mem - 1) * limit_mem
        end_mem = limit_mem * page_mem
        search_param = request.GET.get("search")
        members = Member.objects.all()
        total_members = members.count()
        if search_param:
            members = members.filter(title__icontains=search_param)
        serializer = self.serializer_class(members[start_mem:end_mem], many=True)
        return Response({
            "status": "success",
            "total": total_members,
            "page": page_mem,
            "last_page": math.ceil(total_members / limit_mem),
            "members": serializer.data
        })

    @swagger_auto_schema(
        operation_description="Create a new model",
        request_body=MemberSerializer,
        responses={201: MemberSerializer()})
    def post(self, request):
        # request.data['Password'] = encrypt_data(request.data['Password'])
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"Member": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MembersDetail(APIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_memberlist(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except:
            return None
        
    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: MemberSerializer(many=True)})
    def get(self, request, pk):
        memberlist = self.get_memberlist(pk=pk)
        if memberlist == None:
            return Response({"status": "fail", "message": f"Member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(memberlist)
        return Response({"status": "success", "data": {"Member": serializer.data}})
    
    @swagger_auto_schema(
        operation_description="Update a model",
        request_body=MemberSerializer,
        responses={200: MemberSerializer()})
    def patch(self, request, pk):
        memberlist= self.get_memberlist(pk)
        if memberlist == None:
            return Response({"status": "fail", "message": f"Member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            memberlist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"Member": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Delete a model"
    )
    def delete(self, request, pk):
        memberlist = self.get_memberlist(pk)
        if memberlist == None:
            return Response({"status": "fail", "message": f"Member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        memberlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)