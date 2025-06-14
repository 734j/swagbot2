#!/usr/bin/python3

import argparse
import json

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
    FILEjson = open(config_file, "r")
    config_json = FILEjson.read()
    config = json.loads(config_json)
    FILEtoken = open(config[g_token_dir_path])
    root_run_dir_path = config[g_run_dir_path]
    token_string = FILEtoken.read()
    
    
    
    
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

