from rest_framework import serializers
from .models import Member
from .models import Country
from .models import State
from .models import City

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        Password = validated_data.pop('Password')
        user = Member(**validated_data)
        user.set_password(Password)
        user.save() 
        return user
    
class LoginSerializer(serializers.Serializer):
    UserName=serializers.CharField()   
    Password=serializers.CharField() 

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'  