from email import message
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from profiles_api import serializers

from django.shortcuts import render


class HypervisorConnect(APIView):
    """Get the Hypervisor information class"""

    serializer_class = serializers.HypervisorIPInput

    def get(self, request, format=None):

        """Return VM Information"""
        hypervisor_info = {
        '0' : {
        'hostname' : 'ismail.com',
        'ipAddress' : '10.11.17.200',
        'opeartingSystem' : 'Redhat 7', 
        },
        '1' :{
        'hostname' : 'ismail2.com',
        'ipAddress' : '10.11.17.201',
        'opeartingSystem' : 'Redhat 7', 
        },
        }
        return Response(hypervisor_info)

    def post(self, request):
        """Get IP of hypervisor - to fetch information"""
        
        #fetch data from request 
        serializer = self.serializer_class(data=request.data)
        #validate the data
        if serializer.is_valid():
            ipAddress = serializer.validated_data.get('ipAddress')
            message = f'Hypervisor IP: {ipAddress}'
            return Response({'message': message})
        else:
            return Response (
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


def dashboard(request):
    return render(request, "index.html")
    
