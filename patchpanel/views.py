from django.shortcuts import render

from .models import Uploadvmpatchdb
from .forms import UploadvmpatchForm
from .serializers import UploadvmpatchdbSerializer
# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .tasks import * #for celerey tasks


class HypervisorVMPatchInfo(APIView):

    def get(self, request):
        if request.method == "GET":
            patchesObj = Uploadvmpatchdb.objects.all()
            serializer = UploadvmpatchdbSerializer(patchesObj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            '''
            mydict = {}
            for i in range(0,patchesObj.count()):
                mydict.update({i:patchesObj[i].script.name.split('/')[1]})
            '''   
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
    '''
    mydict = {
        'mylist1':selectedscript,
        'mylist2':selectedguestvms

    }
    print(mydict)
    '''

    mytestceleryfunction.delay()

    return render(request, 'patchpanel/patchpanel.html')