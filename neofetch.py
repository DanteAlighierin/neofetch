#!/usr/local/bin/python3
import time
import socket
import os
import subprocess
import sys
import platform
import sysconfig
import psutil

def local_ip():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		return s.getsockname()[0]
	except:
		return None



def host_name():
	try:
		return socket.gethostname()
	except:
		return None

def os_version():
	
	try:
		return platform.linux_distribution(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'redhat', 'mandrake', ...), full_distribution_name=1)

	except:
		return None

def model():
	try:
		return str("PC on x_86 architecture.Desktop computer")
	except:
		return None

def screen_size():
	try:
		return subprocess.check_output(["uptime"])

		
	except:
		return None




def uptime():
	try:
		return subprocess.check_output(["uptime"])
	except:
		return None

def shell():
	try:
		return os.environ.get('SHELL', '')
	except:
		return None

def kernel():
	try:
		return platform.release()
	except:
		return None

def cpu_spec():
	try:
		return os.system("sudo lshw -class cpu")
	except:
		return None

def cpu_usage():
	try:
		
		return psutil.cpu_percent()

	except :
		return None

def battery_percentage():
	try:
		return os.system("upower -i /org/freedesktop/UPower/devices/battery_BAT0")

	except:
		return None



def memory():
	try:
		return os.system("sudo inxi -m")
	except:
		return None





TEMPLATE = """
                                     {hostname} 
                                               {hostname_sep}
         
OS: {os_version}
Kernel: {kernel}
Model: {model}
Shell: {shell}
Uptime: {uptime}
Resolution: {size}
Local IP: {local_ip}
Battery: {battery_percentage}
Cpu_usage:{cpu_usage}
                   





                                                     
                                                        
                                                         
                                                         
                                                         
                                                         
                                                        
                                                 
"""


print(TEMPLATE.format(hostname = host_name(),
	hostname_sep = "-" * len(host_name()),
	os_version=os_version(),
	kernel=kernel(),
	model=model(),
	shell=shell(),
	uptime=uptime(),
	size=screen_size(),
	cpu=cpu_spec(),
	cpu_usage=cpu_usage(),
	local_ip=local_ip(),
	battery_percentage=battery_percentage(),
	memory = memory(),
)
)
os.system("rm -rf .tmp.txt")


