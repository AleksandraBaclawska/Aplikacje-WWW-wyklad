from rest_framework import serializers
from gamesAPI.models import Gamemodel, Player,GameType
from django.contrib.auth.models import User

class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model=Gamemodel
        fields='__all__'
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Player
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Mate:
        model = User
        fields = ['id','last_login','is_superuser','username','email','data_joined']

class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=GameType
        fields='__all__'
