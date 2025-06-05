#!/usr/bin/python3

import argparse
import json


def check_config():
    print("Config check")


def install_bot():
    print("Installing...")

    
def test_bot():
    print("Testing...")



parser = argparse.ArgumentParser(description="")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--test', action='store_true', help="Run tests")
group.add_argument('--install', action='store_true', help="Run installation")

args = parser.parse_args()

if args.test:
    test_bot()
elif args.install:
    install_bot()

