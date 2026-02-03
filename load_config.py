#####################################################
## cisco_load_config.py
## created by gdtlumauig 2026
##
##
#####################################################

from netmiko import ConnectHandler
from datetime import datetime
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
import os
import getpass
import readline

def multiple_cisco_load(dev,uname,pwd,cmd):
    
    try:
        cisco_ios = {
            'device_type': 'cisco_ios',
            'host' : dev,
            'username' : uname,
            'password' : pwd,
        }


        command_folder = "load_config_folder/"+cmd
        net_connect = ConnectHandler(**cisco_ios)
        config_execute = net_connect.send_config_from_file(command_folder)

        result = "loaded"
        

    except FileNotFoundError:
        print("Command filename:" +cmd+ " in the directory load_config_folder")

    except AuthenticationException:
        result = "Auth_Error"
        print("Authentication error\n")

    except NetMikoTimeoutException:
        result = "unreachable"
        

    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"Error/s: {type(e).__name__}/n/n")
    
    return result



def load_config(uname,pwd,cmd,devlist):
    try:
        with open ("load_config_folder/"+devlist,'r') as device_list:
            devices = device_list.readlines()

            for  device in devices:
                result = multiple_cisco_load(device,uname,pwd,cmd)
                if result == "Auth_Error":
                    print("Re-run the program again")
                    break;
                else:
                    print(f"Device name: "+str(device)+" - test")
    except FileNotFoundError:
        print("Device list filename:" +devlist+ " is not in the directory load_config_folder")


try:

    os.system('clear')
    print("=====================================")
    print("Load Configuration To Cisco Device")
    print("Created by G-Lumauig")
    print("\n\n")
    username = input("Enter your username: ")
    passwd = getpass.getpass("Enter your password: ")
    commands_to_load = input("Enter filename of the commands to be loaded: ")
    device_list = input("Enter the filename of the device list: ")
    print("\n\n")

    load_config(username,passwd,commands_to_load,device_list)



    print("\n\n=====================================")

except KeyboardInterrupt:
    print("\n\n=====================================")
    print("\nKeyboardInterrupt received. Exiting gracefully.")
    print("\n\n=====================================")

