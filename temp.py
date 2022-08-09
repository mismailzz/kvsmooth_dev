import sys
sys.path.insert(1, '/root/async_project/pyvmomi-community-samples/samples/')
from argparse import Namespace

import time
import re
from tools import cli, service_instance, pchelper
from pyVmomi import vim, vmodl


def myceleryfunctionRunScript(host_ip, host_user, host_pass, host_port, disablessl, vmguestname, vmguestuser, vmguestpass, scriptPath):
    """
    Simple command-line program for executing a process in the VM without the
    network requirement to actually access it.
    """
    #args = parser.get_args()
    args = Namespace(disable_ssl_verification=disablessl, host=host_ip, password=host_pass, port=host_port, user=host_user, uuid=None, vm_name=vmguestname, vm_password=vmguestpass, vm_user=vmguestuser)
   
    si = service_instance.connect(args)
    try:
        content = si.RetrieveContent()

        vm = None
        if args.uuid:
            # if instanceUuid(last argument) is false it will search for VM BIOS UUID instead
            vm = content.searchIndex.FindByUuid(None, args.uuid, True)
        elif args.vm_name:
            vm = pchelper.get_obj(content, [vim.VirtualMachine], args.vm_name)

        if not vm:
            raise SystemExit("Unable to locate the virtual machine.")

        tools_status = vm.guest.toolsStatus
        if tools_status in ('toolsNotInstalled', 'toolsNotRunning'):
            raise SystemExit(
                "VMwareTools is either not running or not installed. "
                "Rerun the script after verifying that VMwareTools "
                "is running")

        creds = vim.vm.guest.NamePasswordAuthentication(
            username=args.vm_user, password=args.vm_password
        )

        with open(scriptPath) as f: #my script path
            lines_cmds = f.readlines()
            for line in lines_cmds:
                temp_cmds = line.strip()
                print(temp_cmds)
                temp_programpath_extract = str(temp_cmds.split(" ")[0:1][0])
                args.path_to_program = temp_programpath_extract
                args.program_arguments = " ".join(temp_cmds.split(" ")[1:])
                print(args.path_to_program + " " + args.program_arguments)
                     
                try:
                    profile_manager = content.guestOperationsManager.processManager
        
                    if args.program_arguments:
                        program_spec = vim.vm.guest.ProcessManager.ProgramSpec(
                            programPath=args.path_to_program,
                            arguments=args.program_arguments)
                    else:
                        program_spec = vim.vm.guest.ProcessManager.ProgramSpec(
                            programPath=args.path_to_program)
        
                    res = profile_manager.StartProgramInGuest(vm, creds, program_spec)
        
                    if res > 0:
                        print("Program submitted, PID is %d" % res)
                        pid_exitcode = \
                            profile_manager.ListProcessesInGuest(vm, creds, [res]).pop().exitCode
                        # If its not a numeric result code, it says None on submit
                        while re.match('[^0-9]+', str(pid_exitcode)):
                            print("Program running, PID is %d" % res)
                            time.sleep(5)
                            pid_exitcode = \
                                profile_manager.ListProcessesInGuest(vm, creds, [res]).pop().exitCode
                            if pid_exitcode == 0:
                                print("Program %d completed with success" % res)
                                break
                            # Look for non-zero code to fail
                            elif re.match('[1-9]+', str(pid_exitcode)):
                                print("ERROR: Program %d completed with Failute" % res)
                                print("  tip: Try running this on guest %r to debug"
                                    % vm.summary.guest.ipAddress)
                                print("ERROR: More info on process")
                                print(profile_manager.ListProcessesInGuest(vm, creds, [res]))
                                break
        
                except IOError as ex:
                    print(ex)
    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return -1

    return 0


# Start program
if __name__ == "__main__":
    myceleryfunctionRunScript("192.168.150.17", "root", "Gr@v!Tid3@c7ivAt0rs", 443, True, "ismail_DontDeleteWithouPermission", "root", "Temp/123", "/root/async_project/kvsmooth_dev/media/documents/temp.sh")
