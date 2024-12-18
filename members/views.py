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
from .models import *
from .serializers import *
# from .encdyc import encrypt_data,decrypt_data
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password,check_password
import math
from datetime import datetime
from .Views.City_Views import Cities,CitiesDetail,CitySerializer
from .Views.State_Views import States,StatesDetail,StateSerializer
from .Views.Country_Views import Countrys,CountrysDetail,CountrySerializer
from .Views.Members_Views import Members,MembersDetail,MemberSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework_jwt.settings import api_settings

# class Login(APIView): 
#     @swagger_auto_schema(
#         operation_description="Create a new model",
#         request_body=LoginSerializer,
#         responses={201: LoginSerializer()})
#     def post(self, request): 
#         UserName = request.data.get('UserName') 
#         Password = request.data.get('Password') 
#         user = authenticate(UserName=UserName, Password=Password) 
#         if user: 
#             jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER 
#             jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER 
#             payload = jwt_payload_handler(user) 
#             token = jwt_encode_handler(payload) 
#             response_data = {
#                  'token': token 
#                  } 
#             return Response(response_data, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    serializer_class = LoginSerializer
    @swagger_auto_schema(
        operation_description="Create a new model",
        request_body=LoginSerializer,
        responses={201: LoginSerializer()})
    def post(self,request):
       data=request.data 
       serializer = self.serializer_class(data=request.data)
       if not serializer.is_valid():
           return Response({
               "status": False,
               "data":serializer.errors
           })
       print(serializer.data)
       UserName=serializer.data['UserName']
       Password=serializer.data['Password']
       print('---------------------------------------------------------------------lalit ------------------------------------------');
       print(UserName);
       print(Password);
       user_obj=authenticate(UserName=UserName,Password=Password)
       if user_obj:
           token,_=Token.objects.get_or_create(user=user_obj)
           print(token)
           return Response({
           "status": True,
           "data": {'token': ''}
       })

       return Response({
           "status": False,
           "data": {},
           "message":"invalid credinatials"
       })


# class RegisterUserView(APIView):
#     serializer_class = MemberSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({
#                 'username': user.UserName,
#                 'message': 'User registered successfully'
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserRegistrationView(APIView):
#     serializer_class = MemberSerializer
#     permission_classes = [permissions.AllowAny]

# class UserLoginView(APIView):
#     @swagger_auto_schema(
#         operation_description="Create a new model",
#         request_body=MemberSerializer,
#         responses={201: MemberSerializer()})
#     def post(self, request):
#         user = authenticate(username=request.data['UserName'], password=request.data['Password'])
#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=401)


# class Login(APIView):
#     @swagger_auto_schema(
#         operation_description="Searches for a  model",
#         request_body=LoginSerializer,
#         responses={201: LoginSerializer()})
#     def post(self,request):
#         try:
#             data = request.data
#             serializer = LoginSerializer(data=data)
#             if serializer.is_valid():
#                 UserName=serializer.data['UserName']
#                 Password=serializer.data['Password']


#                 user = authenticate(UserName=UserName,Password=Password)

#                 if user is None:
#                      return Response({
#                        'status': 400,
#                        'message': 'invalid password',
#                        'data': {}
#             })
                
#                 refresh = RefreshToken.for_user(user)
#                 return {
#                        'refresh': str(refresh),
#                        'access': str(refresh.access_token),
#             }


#             return Response({
#                 'status': 400,
#                 'message': 'something went wrong',
#                 'data': serializer.errors
#             })

#         except Exception as e:
#              print(e)    

# class Members(APIView):
#     serializer_class = MemberSerializer
#     queryset = Member.objects.all()

#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: MemberSerializer(many=True)})
#     def get(self, request):
#         page_mem = int(request.GET.get("page", 1))
#         limit_mem = int(request.GET.get("limit", 10))
#         start_mem = (page_mem - 1) * limit_mem
#         end_mem = limit_mem * page_mem
#         search_param = request.GET.get("search")
#         members = Member.objects.all()
#         total_members = members.count()
#         if search_param:
#             members = members.filter(title__icontains=search_param)
#         serializer = self.serializer_class(members[start_mem:end_mem], many=True)
#         return Response({
#             "status": "success",
#             "total": total_members,
#             "page": page_mem,
#             "last_page": math.ceil(total_members / limit_mem),
#             "members": serializer.data
#         })

#     @swagger_auto_schema(
#         operation_description="Create a new model",
#         request_body=MemberSerializer,
#         responses={201: MemberSerializer()})
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": {"Member": serializer.data}}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class MembersDetail(APIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer

#     def get_memberlist(self, pk):
#         try:
#             return Member.objects.get(pk=pk)
#         except:
#             return None
        
#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: MemberSerializer(many=True)})
#     def get(self, request, pk):
#         memberlist = self.get_memberlist(pk=pk)
#         if memberlist == None:
#             return Response({"status": "fail", "message": f"Member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(memberlist)
#         return Response({"status": "success", "data": {"Member": serializer.data}})
    
#     @swagger_auto_schema(
#         operation_description="Update a model",
#         request_body=MemberSerializer,
#         responses={200: MemberSerializer()})
#     def patch(self, request, pk):
#         memberlist= self.get_memberlist(pk)
#         if memberlist == None:
#             return Response({"status": "fail", "message": f"Member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(
#             memberlist, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.validated_data['updatedAt'] = datetime.now()
#             serializer.save()
#             return Response({"status": "success", "data": {"Member": serializer.data}})
#         return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     @swagger_auto_schema(
#         operation_description="Delete a model"
#     )
#     def delete(self, request, pk):
#         memberlist = self.get_memberlist(pk)
#         if memberlist == None:
#             return Response({"status": "fail", "message": f"Member with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         memberlist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class Countrys(APIView):
#     serializer_class = CountrySerializer
#     queryset = Country.objects.all()

#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: CountrySerializer(many=True)})
#     def get(self, request):
#         page_cunt = int(request.GET.get("page", 1))
#         limit_cunt = int(request.GET.get("limit", 10))
#         start_cunt = (page_cunt - 1) * limit_cunt
#         end_cunt = limit_cunt * page_cunt
#         search_param = request.GET.get("search")
#         countrys = Country.objects.all()
#         total_countrys = countrys.count()
#         if search_param:
#             countrys = countrys.filter(title__icontains=search_param)
#         serializer = self.serializer_class(countrys[start_cunt:end_cunt], many=True)
#         return Response({
#             "status": "success",
#             "total": total_countrys,
#             "page": page_cunt,
#             "last_page": math.ceil(total_countrys / limit_cunt),
#             "countrys": serializer.data
#         })

#     @swagger_auto_schema(
#         operation_description="Create a new model",
#         request_body=CountrySerializer,
#         responses={201: CountrySerializer()})
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": {"Country": serializer.data}}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class CountrysDetail(APIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer

#     def get_countrylist(self, pk):
#         try:
#             return Country.objects.get(pk=pk)
#         except:
#             return None
        
#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: CountrySerializer(many=True)})
#     def get(self, request, pk):
#         countrylist = self.get_countrylist(pk=pk)
#         if countrylist == None:
#             return Response({"status": "fail", "message": f"Country with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(countrylist)
#         return Response({"status": "success", "data": {"Country": serializer.data}})
    
#     @swagger_auto_schema(
#         operation_description="Update a model",
#         request_body=CountrySerializer,
#         responses={200: CountrySerializer()})
#     def patch(self, request, pk):
#         countrylist= self.get_countrylist(pk)
#         if countrylist == None:
#             return Response({"status": "fail", "message": f"Country with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(
#             countrylist, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.validated_data['updatedAt'] = datetime.now()
#             serializer.save()
#             return Response({"status": "success", "data": {"Country": serializer.data}})
#         return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     @swagger_auto_schema(
#         operation_description="Delete a model"
#     )
#     def delete(self, request, pk):
#         countrylist = self.get_countrylist(pk)
#         if countrylist == None:
#             return Response({"status": "fail", "message": f"Country with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         countrylist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class States(APIView):
#     serializer_class = StateSerializer
#     queryset = State.objects.all()

#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: StateSerializer(many=True)})
#     def get(self, request):
#         page_stt = int(request.GET.get("page", 1))
#         limit_stt = int(request.GET.get("limit", 10))
#         start_stt = (page_stt - 1) * limit_stt
#         end_stt = limit_stt * page_stt
#         search_param = request.GET.get("search")
#         states = State.objects.all()
#         total_states = states.count()
#         if search_param:
#             states = states.filter(title__icontains=search_param)
#         serializer = self.serializer_class(states[start_stt:end_stt], many=True)
#         return Response({
#             "status": "success",
#             "total": total_states,
#             "page": page_stt,
#             "last_page": math.ceil(total_states / limit_stt),
#             "states": serializer.data
#         })

#     @swagger_auto_schema(
#         operation_description="Create a new model",
#         request_body=StateSerializer,
#         responses={201: StateSerializer()})
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": {"State": serializer.data}}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class StatesDetail(APIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer

#     def get_statelist(self,pk):
#         try:
#             return State.objects.get(pk=pk)
#         except:
#             return None

#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: StateSerializer(many=True)})
#     def get(self, request,pk):
#         statelist = self.get_statelist(pk=pk)
#         if statelist == None:
#             return Response({"status": "fail", "message": f"State with Country Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(statelist)
#         return Response({"status": "success", "data": {"State": serializer.data}})
    
#     @swagger_auto_schema(
#         operation_description="Update a model",
#         request_body=StateSerializer,
#         responses={200: StateSerializer()})
#     def patch(self, request,pk):
#         statelist= self.get_statelist(pk)
#         if statelist == None:
#             return Response({"status": "fail", "message": f"State with Country Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(
#             statelist, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.validated_data['updatedAt'] = datetime.now()
#             serializer.save()
#             return Response({"status": "success", "data": {"State": serializer.data}})
#         return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     @swagger_auto_schema(
#         operation_description="Delete a model"
#     )
#     def delete(self, request,pk):
#         statelist = self.get_statelist(pk)
#         if statelist == None:
#             return Response({"status": "fail", "message": f"State with Country Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         statelist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class Cities(APIView):
#     serializer_class = CitySerializer
#     queryset = City.objects.all()

#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: CitySerializer(many=True)})
#     def get(self, request):
#         page_cit = int(request.GET.get("page", 1))
#         limit_cit = int(request.GET.get("limit", 10))
#         start_cit = (page_cit - 1) * limit_cit
#         end_cit = limit_cit * page_cit
#         search_param = request.GET.get("search")
#         cities = City.objects.all()
#         total_cities = cities.count()
#         if search_param:
#             cities = cities.filter(title__icontains=search_param)
#         serializer = self.serializer_class(cities[start_cit:end_cit], many=True)
#         return Response({
#             "status": "success",
#             "total": total_cities,
#             "page": page_cit,
#             "last_page": math.ceil(total_cities / limit_cit),
#             "cities": serializer.data
#         })

#     @swagger_auto_schema(
#         operation_description="Create a new model",
#         request_body=CitySerializer,
#         responses={201: CitySerializer()})
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": {"City": serializer.data}}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class CitiesDetail(APIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer

#     def get_citylist(self,pk):
#         try:
#             return City.objects.get(pk=pk)
#         except:
#             return None
        
#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: CitySerializer(many=True)})
#     def get(self, request,pk):
#         citylist = self.get_citylist(pk=pk)
#         if citylist == None:
#             return Response({"status": "fail", "message": f"City with State Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(citylist)
#         return Response({"status": "success", "data": {"City": serializer.data}})
    
#     @swagger_auto_schema(
#         operation_description="Update a model",
#         request_body=CitySerializer,
#         responses={200: CitySerializer()})
#     def patch(self, request,pk):
#         citylist= self.get_citylist(pk)
#         if citylist == None:
#             return Response({"status": "fail", "message": f"City with State Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.serializer_class(
#             citylist, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.validated_data['updatedAt'] = datetime.now()
#             serializer.save()
#             return Response({"status": "success", "data": {"City": serializer.data}})
#         return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     @swagger_auto_schema(
#         operation_description="Delete a model"
#     )
#     def delete(self, request,pk):
#         citylist = self.get_citylist(pk)
#         if citylist == None:
#             return Response({"status": "fail", "message": f"City with State Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

#         citylist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET'])
# def api_details_Member_view (request):
#    try:
#       member_list=Member.objects.all()
#    except Member.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "GET":
#       serializer=MemberSerializer(member_list,many=True)
#       return Response(serializer.data)
# @api_view(['PUT'])
# def api_update_Member_view (request, memberid):
#    try:
#       obj=Member.objects.get(id = memberid)
#    except Member.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "PUT":
#       serializer=MemberSerializer(obj,data=request.data,many=True)
#       data={}
#       if serializer.is_valid():
#          serializer.save()
#          data["success"]="update successfully"
#          return Response (data=data)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['DELETE'])
# def api_delete_Member_view (request, memberid):
#    try:
#       obj=Member.objects.get(id = memberid)
#    except Member.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "DELETE":
#       operation = obj.delete()
#       if operation:
#          data["success"]="delete successful"
#       else:
#          data["failure"]="data failed"
#       return Response(data=data)
# @api_view(['POST'])
# def api_create_Member_view(request):
#  data = request.data
#  data["Password"] = encrypt_data(data["Password"])
#  serializer = MemberSerializer(data=data)
#  if Member.objects.filter(**request.data).exists():
#     raise serializers.ValidationError('already exists')
#  if serializer.is_valid():
#       serializer.save()
#       print("saved")
#       return Response({'status':"success"}, status=200)
#  else:
#        return Response({'status':"failed{serializer.error}"}, status=500)  
# @api_view(['POST'])
# def api_create_Member_view(request):
#  data = request.data
#  data['Password'] = encrypt_data(data['Password'])
#  serializer = MemberSerializer(data=request.data)
#  try:
#    if serializer.is_valid():
#       serializer.save()
#       print("saved")
#       return Response({'status':"success"}, status=200)
#    else:
#        return Response({'status':"failed{serializer.error}"}, status=500)
#  except:  
#       return Response({'status':"failed"}, status=500)
 
#  class MemberListEncryptedView(APIView):
#     renderer_classes = [CustomAesRenderer]

#     def get(self, request):
#         member_list = Member.objects.all()
#         if:
#             serializer = MemberSerializer(members_list, many=True)
#             data = serializer.data
#         data = {
#             'status': 'success',
#             'code' : status.HTTP_200_OK,
#             'data': data
#             }
#         return Response(data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def api_details_Country_view (request):
#    try:
#       country_list=Country.objects.all()
#    except Country.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "GET":
#       serializer=CountrySerializer(country_list,many=True)
#       return Response(serializer.data)
# @api_view(['PUT'])
# def api_update_Country_view(request):
#     country_list = Country.objects.filter()
#     data = CountrySerializer(instance=country_list, data=request.data)
#     if Country.objects.filter(**request.data).exists():
#      raise serializers.ValidationError('already exists')
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['PUT'])
# def api_update_Country_view (request):
#    try:
#        country_list=Country.objects.filter()
#    except Country.doesNotExists:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "PUT":
#       serializer=CountrySerializer(country_list,data=request.data)
#       if Country.objects.filter(**request.data).exists():
#        raise serializers.ValidationError('already exists')
#       if serializer.is_valid():
#          serializer.save()
#          print("saved")
#          return Response ({'status':"success"}, status=200)
#       else:
#          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['DELETE'])
# def api_delete_Country_view (request):
#    try:
#       country_list=Country.objects.all()
#    except Country.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "DELETE":
#       operation=country_list.delete()
#       data={}
#       if operation:
#          data["success"]="delete successful"
#       else:
#          data["failure"]="data failed"
#       return Response(data=data)
# @api_view(['POST'])
# def api_create_Country_view(request):
#  serializer = CountrySerializer(data=request.data)
#  if Country.objects.filter(**request.data).exists():
#     raise serializers.ValidationError('already exists')
#  if serializer.is_valid():
#       serializer.save()
#       print("saved")
#       return Response({'status':"success"}, status=200)
#  else:
#        return Response({'status':"failed{serializer.error}"}, status=500)  
 

# @api_view(['GET'])
# def api_details_State_view (request,Country_id):
#    try:
#       state_list=State.objects.filter(Country_id=Country_id)
#    except State.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "GET":
#       serializer=StateSerializer(state_list,many=True)
#       return Response(serializer.data)

# @api_view(['PUT'])
# def api_update_State_view(request,Country_id):
#     state_list = State.objects.filter(Country_id=Country_id)
#     data = StateSerializer(instance=state_list, data=request.data)
#     if State.objects.filter(**request.data).exists():
#      raise serializers.ValidationError('already exists')
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['PUT'])
# def api_update_State_view (request):
#    try:
#       state_list=State.objects.filter()
#    except State.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "PUT":
#       serializer=StateSerializer(state_list,data=request.data)
#       data={}
#       if serializer.is_valid():
#          serializer.save()
#          data["success"]="update successfully"
#          return Response (data=data)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['DELETE'])
# def api_delete_State_view (request,Country_id):
#    try:
#       state_list=State.objects.filter(Country_id=Country_id)
#    except State.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "DELETE":
#       operation=state_list.delete()
#       data={}
#       if operation:
#          data["success"]="delete successful"
#       else:
#          data["failure"]="data failed"
#       return Response(data=data)
# @api_view(['POST'])
# def api_create_State_view(request):
#  serializer = StateSerializer(data=request.data)
#  if State.objects.filter(**request.data).exists():
#     raise serializers.ValidationError('already exists')
#  if serializer.is_valid():
#       serializer.save()
#       print("saved")
#       return Response({'status':"success"}, status=200)
#  else:
#        return Response({'status':"failed{serializer.error}"}, status=500)  
# @api_view(['POST'])
# def api_create_State_view(request):
#  data = request.data
#  serializer = StateSerializer(data=data)
#  try:
#    if serializer.is_valid():
#       serializer.save()
#       print("saved")
#       return Response({'status':"success"}, status=200)
#    else:
#        return Response({'status':"failed{serializer.error}"}, status=200)
#  except:  
#       return Response({'status':"failed"}, status=200)
 

# @api_view(['GET'])
# def api_details_City_view (request,State_id):
#    try:
#       city_list=City.objects.filter(State_id=State_id)
#    except City.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "GET":
#       serializer=CitySerializer(city_list,many=True)
#       return Response(serializer.data)

# @api_view(['PUT'])
# def api_update_City_view(request):
#    #  city_list = City.objects.filter()
#     serializer = CitySerializer(data=request.data)
#     if City.objects.filter(**request.data).exists():
#      raise serializers.ValidationError('already exists')
#     if request.method == "PUT":
#       serializer=CitySerializer(data=request.data)
#     data={}
#     if serializer.is_valid():
#         serializer.save()
#         data["success"]="update successfully"
#         return Response(data=data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['PUT'])
# def api_update_City_view (request):
#    try:
#       city_list=City.objects.filter(**request.data)
#    except ObjectDoesNotExist:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "PUT":
#       serializer=CitySerializer(city_list,data=request.data)
#       data={}
#       if serializer.is_valid():
#          serializer.save()
#          data["success"]="update successfully"
#          return Response (data=data)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['DELETE'])
# def api_delete_City_view (request,State_id):
#    try:
#       city_list=City.objects.filter(State_id=State_id)
#    except City.doesNotExists:
#       return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == "DELETE":
#       operation=city_list.delete()
#       data={}
#       if operation:
#          data["success"]="delete successful"
#       else:
#          data["failure"]="data failed"
#       return Response(data=data)
# @api_view(['POST'])
# def api_create_City_view(request):
#  serializer = CitySerializer(data=request.data)
#  if City.objects.filter(**request.data).exists():
#     raise serializers.ValidationError('already exists')
#  if serializer.is_valid():
#       serializer.save()
#       print("saved")
#       return Response({'status':"success"}, status=200)
#  else:
#        return Response({'status':"failed{serializer.error}"}, status=500) 
# @api_view(['POST'])
# def api_create_City_view(request):
#  data = request.data
#  serializer = CitySerializer(data=data)
#  try:
#    if serializer.is_valid():
#       serializer.save()
#       print("saved")
#       return Response({'status':"success"}, status=200)
#    else:
#        return Response({'status':"failed{serializer.error}"}, status=200)
#  except:  
#       return Response({'status':"failed"}, status=200)

# class CountryListAPIView(genericAPIView):
#     # Swagger documentation for the GET method
#     @swagger_auto_schema(
#         operation_description="Retrieve all Country instances",  # Description of what the GET endpoint does
#         responses={200: CountrySerializer(many=True)}  # Expected response: 200 status with a list of MyModel instances serialized
#     )
#     def GET(request):
#         country_list = Country.objects.all()  # Fetch all MyModel instances from the database
#         serializer = CountrySerializer(country_list, many=True)  # Serialize the instances
#         return Response(serializer.data)  # Return the serialized data in the response
    

#     @swagger_auto_schema(
#         operation_description="Update an existing MyModel instance",  # Description of what the PUT endpoint does
#         request_body=CountrySerializer,  # Expected request body format using MySerializer
#         responses={200: CountrySerializer, 400: 'Bad Request', 404: 'Not Found'}  # Expected responses: 200 for success, 400 for bad request, 404 if not found
#     )
#     def PUT(request):
#         if  Country.objects.all().exists():  # Check if a valid pk is provided and the instance exists
#             qs = Country.objects.all()  # Retrieve the MyModel instance
#             serializer = CountrySerializer(qs, data=request.data, partial=True)  # Deserialize the request data with partial update
#             if serializer.is_valid():  # Check if the data is valid
#                 serializer.save()  # Save the updated MyModel instance
#                 return Response({
#                     'message': 'Successfully updated',  # Success message
#                     'error': None,
#                     'data': serializer.data
#                 }, status=status.HTTP_200_OK)  # Return the serialized data with 200 status
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors with 400 status

#         return Response({
#             'message': 'Provide a valid Country',  # Error message for invalid pk
#             'error': 'Not Found',  # Error detail
#             'data': None
#         }, status=status.HTTP_404_NOT_FOUND)  # Return 404 status if the pk is invalid or instance doesn't exist


# schema_view = get_swagger_view(title='Pastebin API')

# class membersViewSet(viewsets.ModelViewSet):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer

# @api_view(['GET'])
# def CountryList(request):
#     country_list= Country.objects.all()
#     serializer=CountrySerializer(country_list, many=True)
#     print ("data : ",country_list)
#     return Response({
#         "data" : serializer.data
#         })


# @api_view(['POST'])
# def post_Country(request):
#  data = request.data
#  serializer = CountrySerializer(data=data)
#  try:
#    if serializer.is_valid():
#       serializer.save()
#       print("saved")
#       return Response({'status':"success"}, status=200)
#    else:
#        return Response({'status':"failed{serializer.error}"}, status=200)
#  except:  
#       return Response({'status':"failed"}, status=200)

    
# class membersViewSet(viewsets.ModelViewSet):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer
#     name=GetStateList=(
#         'Country_id'
#     )

# @csrf_exempt
# def CountryList(request,):
#     if request.method == 'GET':
#         country_list= Country.objects.all()
#         serializer=CountrySerializer(country_list, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         jsondata= JSONParser().parse(request)
#         serializer=CountrySerializer(data=jsondata)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,safe=False)
#         else:
#             return JsonResponse(serializer.data,safe=False)


# @csrf_exempt
# def StateList(request,Country_id):
#     if request.method == 'GET':
#         State_list= State.objects.filter(Country_id=Country_id)
#         serializer=StateSerializer(State_list, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         jsondata= JSONParser().parse(request)
#         serializer=StateSerializer(data=jsondata)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,safe=False)
#         else:
#             return JsonResponse(serializer.data,safe=False)
                     

# @csrf_exempt
# @api_view(['GET','POST'])
# def CityList(request,State_id):
#     if request.method == 'GET':
#         city_list= City.objects.filter(State_id=State_id)
#         serializer=CitySerializer(city_list, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         jsondata= JSONParser().parse(request)
#         serializer=CitySerializer(data=jsondata)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,safe=False)
#         else:
#             return JsonResponse(serializer.data,safe=False)
        
    

# @api_view(['GET'])
# def StateList(request, Country_id):
#     state_list= State.objects.filter(Country_id=Country_id)
#     serializer=StateSerializer(state_list, many=True)
#     print ("data : ",state_list)
#     return Response(serializer.data)

# @api_view(['POST'])
# def post_State(request):

#     serializer = StateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)

#     # data = request.data
#     # print(data)  

# @api_view(['PUT'])
# def put_State(self, request):
#     return Response({
#     "message": "put method"
# })

# class membersViewSet(viewsets.ModelViewSet):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer   

# @api_view(['GET'])
# def CityList(request,State_id):
#     city_list= City.objects.filter(State_id=State_id)
#     serializer=CitySerializer(city_list, many=True)
#     print ("data : ",city_list)
#     return Response(serializer.data)

# @api_view(['POST'])
# def post_city(request):

#     serializer = CitySerializer(data=request.data)
#     if serializer.is_valid():
#        serializer.save()
#     return Response(serializer.data)

#     # data = request.data
#     # print(data)

# @api_view(['PUT'])
# def put_City(self, request):
#     return Response({
#     "message": "put method"
# })


# @api_view(['GET','PUT','DELETE'])
# def MemberList(request):
#     serializer=MemberSerializer
#     if request.method == 'GET':
#         try:
#          member_list= Member.objects.all()
#         except:
#          return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=MemberSerializer(member_list,many=True)
#         return Response(serializer.data)
      
#     if request.method == 'PUT':
#         member_list= Member.objects.all()
#         serializer=MemberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         member_list=Member.objects.all().delete()
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','PUT','DELETE'])
# def MemberListUserName(request):
#     serializer=MemberSerializer
#     if request.method == 'GET':
#         try:
#          member_list= Member.objects.all()
#         except:
#          return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=MemberSerializer(member_list,many=True)
#         return Response(serializer.data)
      
#     if request.method == 'PUT':
#         member_list= Member.objects.all()
#         serializer=MemberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         member_list=Member.objects.all().delete()
#         return Response(status=status.HTTP_400_BAD_REQUEST)    

# @api_view(['GET','PUT','DELETE'])
# def MemberListPassword(request):
#     serializer=MemberSerializer
#     if request.method == 'GET':
#         try:
#          member_list= Member.objects.all()
#         except:
#          return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=MemberSerializer(member_list,many=True)
#         return Response(serializer.data)
      
#     if request.method == 'PUT':
#         member_list= Member.objects.all()
#         serializer=MemberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         member_list=Member.objects.all().delete()
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def CountryList(request):
#     serializer=CountrySerializer
#     if request.method == 'GET':
#         try:
#          country_list= Country.objects.all()
#         except:
#          return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=CountrySerializer(country_list,many=True)
#         return Response(serializer.data)
        
#     if request.method == 'PUT':
#         country_list= Country.objects.all()
#         serializer=CountrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         Country_list=Country.objects.all().delete()
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def StateList(request,Country_id):
#     if request.method == 'GET':
#         try:
#          state_list= State.objects.filter(Country_id=Country_id)
#         except:
#          return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=StateSerializer(state_list,many=True)
#         return Response(serializer.data)
      
#     if request.method == 'PUT':
#         state_list= State.objects.filter(Country_id=Country_id)
#         serializer=StateSerializer(state_list ,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         state_list=State.objects.filter(Country_id=Country_id).delete()
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def CityList(request,State_id):
#     if request.method == 'GET':
#         try:
#          city_list= City.objects.filter(State_id=State_id)
#         except:
#          return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=CitySerializer(city_list,many=True)
#         return Response(serializer.data)
      
#     if request.method == 'PUT':
#         city_list= City.objects.filter(State_id=State_id)
#         serializer=CitySerializer(city_list ,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         city_list=City.objects.filter(State_id=State_id).delete()
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# import base64
# import hashlib
# from Crypto import Random
# from Crypto.Cipher import AES

# class AESCipher(object):

#     def __init__(self, key):
#         self.bs = AES.block_size
#         self.key = hashlib.sha256(key.encode()).digest()

#     def encrypt(self, raw):
#         raw = self._pad(raw)
#         iv = Random.new().read(AES.block_size)
#         cipher = AES.new(self.key, AES.MODE_CBC, iv)
#         return base64.b64encode(iv + cipher.encrypt(raw.encode()))

#     def decrypt(self, enc):
#         enc = base64.b64decode(enc)
#         iv = enc[:AES.block_size]
#         cipher = AES.new(self.key, AES.MODE_CBC, iv)
#         return AESCipher._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

#     def _pad(self, s):
#         return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

#     @staticmethod
#     def _unpad(s):
#         return s[:-ord(s[len(s)-1:])]



# class CountryAPIView(APIView):
#     @swagger_auto_schema(
#         operation_description="Get all models",
#         responses={200: CountrySerializer(many=True)}
#     )
#     def get(self, request):
#         queryset = Country.objects.all()
#         serializer = CountrySerializer(queryset, many=True)
#         return Response(serializer.data)

#     @swagger_auto_schema(
#         operation_description="Create a new model",
#         request_body=CountrySerializer,
#         responses={201: CountrySerializer()}
#     )
#     def post(self, request):
#         serializer = CountrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @swagger_auto_schema(
#         operation_description="Update a model",
#         request_body=CountrySerializer,
#         responses={200: CountrySerializer()}
#     )
#     def put(self, request, pk):
#         try:
#             instance = Country.objects.get(pk=pk)
#         except Country.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = CountrySerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @swagger_auto_schema(
#         operation_description="Delete a model"
#     )
#     def delete(self, request, pk):
#         try:
#             instance = Country.objects.get(pk=pk)
#         except Country.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse("Hello world!")