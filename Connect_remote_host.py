#!/uss/bin/env python

import paramiko, os, getpass, sys, time


USER = raw_input(("Please enter Username to login: ") or "test")
#PASS = getpass.getpass("Enter Password :")
print("Please input IP Address details: ")
INVENTORY = sys.stdin.readlines()
print("Please input single command in each line and press 'CTRL + D' when  done: ")
COMMANDS = sys.stdin.readlines()
session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.load_system_host_keys()
session.set_missing_host_key_policy(paramiko.WarningPolicy())
#KEY_PASS = getpass("Enter passphrase of key file: ")
#KEY_FILE = paramiko.RSAKey.from_private_key_file("/home/ec2-user/.ssh/id_rsa", key_pass)
KEY_FILE = paramiko.RSAKey.from_private_key_file("/home/ec2-user/.ssh/id_rsa")

def CISCO_EXEC():
    """Connect to HOSTS"""
    try:
        for node in INVENTORY:
            try:
                session.connect(node.strip(),username=USER,pkey=KEY_FILE)
                #session.connect(node.strip(),username=USER,password=PASS)
                #session.connect(node.strip(),username=USER,password=PASS)
                DEVICE_ACCESS = session.invoke_shell()
                for CMD in COMMANDS:
                    DEVICE_ACCESS.send('\n' + CMD)
                    time.sleep(.3)
                    OUTPUT = DEVICE_ACCESS.recv(65000)
                    print(OUTPUT.decode())
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

CISCO_EXEC()
