from ipaddress import ip_address
from rest_framework import serializers 


class HypervisorIPInput(serializers.Serializer):
    """Serializes an ip field for our API View"""
    ipAddress = serializers.CharField(max_length=16)
