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
  


def dashboard(request):
    result = myceleryfunction.delay()
    return render(request, 'index.html', context={'task_id': result.task_id})

