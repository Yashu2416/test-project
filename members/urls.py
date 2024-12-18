from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from members.views import Country
from members.views import State
from members.views import City
from.views import *
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView

router = routers.DefaultRouter()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/members', Members.as_view()),
    path('api/members/<int:pk>', MembersDetail.as_view()),
    path('api/countrys', Countrys.as_view()),
    path('api/countrys/<int:pk>', CountrysDetail.as_view()),
    path('api/states', States.as_view()),
    path('api/states/<int:pk>', StatesDetail.as_view()),
    path('api/cities', Cities.as_view()),
    path('api/cities/<int:pk>', CitiesDetail.as_view()),
    path('api/login/',Login.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/login/', UserLoginView.as_view()),
    # path('countrys/', CountryAPIView.as_view()),
    # path('countrys/<int:pk>/', CountryAPIView.as_view()),
    # path('api/members/details',api_details_Member_view,name="details"),
    # path('api/members/update/<int:memberid>',api_update_Member_view,name="details"),
    # path('api/members/delete/<int:memberid>',api_delete_Member_view,name="delete"),
    # path('api/members/create',api_create_Member_view,name="create"),
    # path('api/members/UserName',MemberListUserName),
    # path('api/members/Password',MemberListPassword),
    # path('api/countries/details',api_details_Country_view,name="details"),
    # path('api/countries/update',api_update_Country_view,name="update"),
    # path('api/countries/delete',api_delete_Country_view,name="delete"),
    # path('api/countries/create',api_create_Country_view,name="create"),
    # path('api/states/details/<int:Country_id>',api_details_State_view,name="details"),
    # path('api/states/update/<int:Country_id>',api_update_State_view,name="update"),
    # path('api/states/delete/<int:Country_id>',api_delete_State_view,name="delete"),
    # path('api/states/create',api_create_State_view,name="create"),
    # path('api/cities/details/<int:State_id>',api_details_City_view,name="details"),
    # path('api/cities/update',api_update_City_view,name="update"),
    # path('api/cities/delete/<int:State_id>',api_delete_City_view,name="delete"),
    # path('api/cities/create',api_create_City_view,name="create"),
    # path('post_Country/',CountryList,name="post_Country"),
    path('api-auth/', include('rest_framework.urls')),
    # path('crud/',CountryList.as_view(),name="countriesss")
 
    # url(r'^$', schema_view)
]