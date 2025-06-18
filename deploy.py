#!/usr/bin/python3

import argparse
import json
import os
from datetime import datetime
import shutil

g_run_dir_path = "run_dir_path"
g_token_file_path = "token_file_path"
g_bot_src = "bot.py"
g_bot_src_test = "bot_test.py"
def is_config_valid(config_file: str) -> bool:
    
    FILE = open(config_file,"r")
    config_json = FILE.read()
    config = json.loads(config_json)
    allowed = {g_token_file_path, g_run_dir_path}
    if set(config) <= allowed:
        return True
    
    return False

def install_bot(conf_path: str):

    print("Installing...")
    if not is_config_valid(conf_path):
        print("Invalid config")
        return

    print("OK config.")
    FILEjson = open(conf_path, "r")
    config_json = FILEjson.read()
    config = json.loads(config_json)
    FILEtoken = open(config[g_token_file_path])
    root_run_dir_path = os.path.expanduser(config[g_run_dir_path]) # Path to root of the run dir
    token_string = FILEtoken.read() # String of token

    directory_paths = [
        os.path.expanduser(root_run_dir_path+"/bannedwords"),
        os.path.expanduser(root_run_dir_path+"/misc"),
        os.path.expanduser(root_run_dir_path+"/old-versions"),
        os.path.expanduser(root_run_dir_path+"/pitroles")
    ]
    print(directory_paths)

    for path in directory_paths:
        try:
            os.makedirs(path, exist_ok=True)
            print(f"OK: {path}")
        except PermissionError:
            print(f"Insufficient Permission to create: {path}")
        except OSError as e:
            print(f"Error creating path: {path}: {e}")


    fd = os.open(directory_paths[0]+"/list", os.O_WRONLY | os.O_CREAT)
    os.close(fd)
    fd2 = os.open(root_run_dir_path+"/bot.py", os.O_WRONLY | os.O_CREAT)
    os.close(fd2)
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    os.rename(root_run_dir_path+"/"+g_bot_src, directory_paths[2]+"/bot"+timestamp+".py")
    shutil.copyfile(g_bot_src, root_run_dir_path+"/"+g_bot_src)
    shutil.copytree("misc", root_run_dir_path+"/misc", dirs_exist_ok=True)

    
    
def test_bot(conf_path: str):

    print("Testing...")
    if not is_config_valid(conf_path):
        print("Invalid config")
        return
        
    print("OK config.")
        
    

parser = argparse.ArgumentParser(description="Bot tool")
parser.add_argument("config_file", type=str, help="Path to the config file")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--test', action='store_true', help="Run tests")
group.add_argument('--install', action='store_true', help="Run installation")

args = parser.parse_args()

conf_path = args.config_file

if args.test:
    test_bot(conf_path)
elif args.install:
    install_bot(conf_path)

