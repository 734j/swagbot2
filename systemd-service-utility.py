import argparse
import getpass
import sys
import os
import subprocess

def install_service(root_run_dir_path: str, user: str) -> bool:

    print(f"Elevated privelege to user: {getpass.getuser()}")
    print("Installing the service.")
    ExecStart = f"{sys.executable} bot.py"
    WorkingDirectory = root_run_dir_path
    if not os.path.isfile("swagbot2.service"):
        print("swagbot2.service does not exist.")
        return False
    
    FILEservice = open("swagbot2.service", "r")
    data = FILEservice.read()
    FILEservice.close()
    data = data.replace("__USER__", user)
    data = data.replace("__EXEC_START__", ExecStart)
    data = data.replace("__ROOT_RUN_DIR__", WorkingDirectory)
    FILEservice = open("swagbot2.service.tmp", "w")
    FILEservice.write(data)
    FILEservice.close()
    os.rename("swagbot2.service.tmp", "/etc/systemd/system/swagbot2.service")
    print("swagbot2.service.tmp -> /etc/systemd/system/swagbot2.service")
    return True

def enable_service():
    print("Enabling the service...")
    subprocess.run(["sudo", "systemctl", "enable", "swagbot2.service"], check=True)
    
def stop_service():

    print("Stopping the service...")
    subprocess.run(["sudo", "systemctl", "stop", "swagbot2.service"], check=True)
    
def start_service():

    print("Starting the service...")
    subprocess.run(["sudo", "systemctl", "start", "swagbot2.service"], check=True)

    
parser = argparse.ArgumentParser(description="SwagBot2 Service helper (for elevated priveleges)")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--start', action='store_true', help='Start the service')
group.add_argument('--stop', action='store_true', help='Stop the service')
group.add_argument('--enable', action='store_true', help='Enable the service')
group.add_argument('--install', nargs=2, metavar=('ARG1', 'ARG2'), help='Install the service')

args = parser.parse_args()

if args.start:
    start_service()
elif args.stop:
    stop_service()
elif args.enable:
    enable_service()
elif args.install:
    arg1, arg2 = args.install
    install_service(arg1, arg2)
