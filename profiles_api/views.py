from email import message
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers
from django.shortcuts import render

from .models import Hypervisortabledb
from .serializers import HypervisortabledbSerializer

class HypervisorConnect(APIView):
    """Get the Hypervisor information class"""

    def get(self, request):
        hypervisorInfo = Hypervisortabledb.objects.filter(hypervisorIP = "192.168.150.17")
        serializer = HypervisortabledbSerializer(hypervisorInfo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'hypervisorIP': '192.168.150.19', 
            'name': 'ltm',
            'operatingSystem': 'Unkown', 
            'ipAddress': '10.11.1.19',
            'state':'powerON'
        }
        serializer = HypervisortabledbSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''

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
  
'''

def dashboard(request):
    return render(request, "index.html")
    
