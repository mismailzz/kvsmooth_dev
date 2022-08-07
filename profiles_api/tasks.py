# Celery
from celery import shared_task
# Celery-progress
from celery_progress.backend import ProgressRecorder
# Task imports
import time

#----------------------------VMtasks import
import sys
sys.path.insert(1, '/root/async_project/pyvmomi-community-samples/samples/')

import re
from pyVmomi import vmodl, vim
#from tools import cli, service_instance
from argparse import Namespace
#----------------------------VMtasks import end

from profiles_api import serializers
from .models import Hypervisortabledb
from .serializers import HypervisortabledbSerializer

from .tasks import *



'''
# Celery Task
@shared_task(bind=True)
def myceleryfunction(self):
        print('Task started')
        # Create the progress recorder instance
        # which we'll use to update the web page
        progress_recorder = ProgressRecorder(self)

        print('Start')

        time.sleep(5)
        progress_recorder.set_progress(1 + 1, 3, description="Downloading")
        time.sleep(5)
        progress_recorder.set_progress(2 + 1, 3, description="Downloading")

        print('End')

        return 'Task Complete'
        
'''

# Celery Task
@shared_task(bind=True)
def myceleryfunction(self, arg_host, arg_pass, arg_user, arg_port, arg_find, arg_disablessl):
    """
    Simple command-line program for listing the virtual machines on a system.
    """
    
    '''
    parser = cli.Parser()
    parser.add_custom_argument('-f', '--find', required=False,
                               action='store', help='String to match VM names')
    args = parser.get_args()
    print(type(args))
    print(args)
    print(args.host)
    
    #hypervisorIP = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(args))
    hypervisorIP = str(args.host)
    '''
    #args = Namespace(disable_ssl_verification=True, find=None, host='192.168.x.x', password='password123', port=443, user='root')
    args = Namespace(disable_ssl_verification=arg_disablessl, find=arg_find, host=arg_host, password=arg_pass, port=arg_port, user=arg_user)
    
    hypervisorIP = str(args.host)
    
    si = service_instance.connect(args)
    
    try:
        content = si.RetrieveContent()
    
        container = content.rootFolder  # starting point to look into
        view_type = [vim.VirtualMachine]  # object types to look for
        recursive = True  # whether we should look into it recursively
        container_view = content.viewManager.CreateContainerView(
            container, view_type, recursive)
    
        children = container_view.view
        
        vmlistdict = []
        key_count = 0
        
        if args.find is not None:
            pat = re.compile(args.find, re.IGNORECASE)
        for child in children:
            if args.find is None:
                print_vm_info(child)
            else:
                if pat.search(child.summary.config.name) is not None:
                    print_vm_info(child)
            tempdict = { 'hypervisorIP' : hypervisorIP, 'name' : child.summary.config.name, 'operatingSystem' : child.summary.config.guestFullName, 'ipAddress' : child.summary.guest.ipAddress, 'state' : child.summary.runtime.powerState }
            vmlistdict.append(tempdict)
            #print(child.summary.config)
        
    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return -1
    
    print(vmlistdict)
    
    serializer = HypervisortabledbSerializer(data=vmlistdict, many=True)
    print("ismail------------")
    
    if serializer.is_valid():
        serializer.save()
        print('serialize true')
    
    return vmlistdict
        


def print_vm_info(virtual_machine):
    #print(virtual_machine.summary.config)
    """
    Print information for a particular virtual machine or recurse into a
    folder with depth protection
    """
    summary = virtual_machine.summary
    print("Name       : ", summary.config.name)
    print("Template   : ", summary.config.template)
    print("Path       : ", summary.config.vmPathName)
    print("Guest      : ", summary.config.guestFullName)
    print("Instance UUID : ", summary.config.instanceUuid)
    print("Bios UUID     : ", summary.config.uuid)
    annotation = summary.config.annotation
    if annotation:
        print("Annotation : ", annotation)
    print("State      : ", summary.runtime.powerState)
    if summary.guest is not None:
        ip_address = summary.guest.ipAddress
        tools_version = summary.guest.toolsStatus
        if tools_version is not None:
            print("VMware-tools: ", tools_version)
        else:
            print("Vmware-tools: None")
        if ip_address:
            print("IP         : ", ip_address)
        else:
            print("IP         : None")
    if summary.runtime.question is not None:
        print("Question  : ", summary.runtime.question.text)
    print("")  
