from rest_framework import serializers
from restgameapi.models import Gamemodel

class Serializationclass(serializers.ModelSerializer):
    class Meta:
        model=Gamemodel
        fields='__all__'
