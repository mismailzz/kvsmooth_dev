from rest_framework import serializers 
from .models import Hypervisortabledb


class HypervisortabledbSerializer(serializers.ModelSerializer):
    '''
    hypervisorIP = serializers.CharField(max_length=16)
    name = serializers.CharField(max_length=100)
    operatingSystem = serializers.CharField(max_length=100)
    ipAddress = serializers.CharField(max_length=16)
    state = serializers.CharField(max_length=20)

    class Meta:
        model = Hypervisortabledb
        fields = ('__all__')
    '''
    class Meta:
        model = Hypervisortabledb
        fields = ["hypervisorIP", "name", "operatingSystem", "ipAddress", "state"] 
        