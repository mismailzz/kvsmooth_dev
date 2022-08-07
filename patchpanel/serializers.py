from rest_framework import serializers 
from .models import Uploadvmpatchdb


class UploadvmpatchdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploadvmpatchdb
        fields = ["script"] 
        