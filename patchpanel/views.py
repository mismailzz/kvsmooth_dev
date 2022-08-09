from django.shortcuts import render

from .models import Uploadvmpatchdb
from .forms import UploadvmpatchForm
from .serializers import UploadvmpatchdbSerializer
# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .tasks import * #for celerey tasks

import ast #for converting string to list
#https://stackoverflow.com/questions/30510164/python-string-to-list-without-split



class HypervisorVMPatchInfo(APIView):

    def get(self, request):
        if request.method == "GET":
            patchesObj = Uploadvmpatchdb.objects.all()
            serializer = UploadvmpatchdbSerializer(patchesObj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


def HypervisorVMPatch(request):
    if request.method == 'POST':
        form = UploadvmpatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'patchpanel/patchpanel.html')
    else:
        form = UploadvmpatchForm()
    return render(request, 'patchpanel/patchpanel.html', {
        'form': form
    })


def sendpatchinfo(request):
    if request.method == 'GET':
        selectedscript = request.GET.get('selectedscript', None)
        selectedguestvms = request.GET.get('selectedguestvms', None)
        
        hostuser = request.GET.get('hostuser', None)
        hostpass = request.GET.get('hostpass', None)
        guestuser = request.GET.get('guestuser', None)
        guestpass = request.GET.get('guestpass', None)


        mylist = selectedguestvms.replace(',"state":true','')
        _list = ast.literal_eval(mylist)

        for i in range(len(_list)):
            host_ip = _list[i]['host']
            vmguestname = _list[i]['guestname']         
            myceleryfunctionRunScript.delay(host_ip, hostuser, hostpass, 443, True, vmguestname, guestuser, guestpass, selectedscript)


        print(selectedscript)
        print(selectedguestvms)
        print(hostuser)
        print(hostpass)
        print(guestuser)
        print(guestpass)
    '''
    mydict = {
        'mylist1':selectedscript,
        'mylist2':selectedguestvms

    }
    print(mydict)
    '''

        #mytestceleryfunction.delay()

    return render(request, 'patchpanel/patchpanel.html')