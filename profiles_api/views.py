from email import message
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers
from django.shortcuts import render

from .models import Hypervisortabledb
from .serializers import HypervisortabledbSerializer

from .tasks import *



  

class HypervisorConnect(APIView):
    """Get the Hypervisor information class"""
    '''
    def get(self, request, format=None):
        myceleryfunction.delay()
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
    
    def get(self, request):
        hypervisorInfo = Hypervisortabledb.objects.filter(hypervisorIP = "192.168.150.17")
        serializer = HypervisortabledbSerializer(hypervisorInfo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        if request.method == 'POST':
            
            username = request.POST["user"]
            password = request.POST["pass"]
            ipaddress = request.POST["ipaddr"]
 
            myceleryfunction.delay(ipaddress, password, username, 443, None, True)
            
        
        return render(request, 'index.html')
    

       

def dashboard(request):
    #result = myceleryfunction.delay()
    #return render(request, 'index.html', context={'task_id': result.task_id})
    return render(request, 'index.html')
