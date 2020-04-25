#!/usr/local/bin/python3

import socket
import os
import subprocess

import platform



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
		return subprocess.check_output(["xrandr | grep \"*\""], shell=True)

		
	except:
		return None




def uptime():
	try:
		return subprocess.check_output(["uptime -p"], shell=True)
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
		return platform.processor()
	except:
		return None

#def cpu_usage():
#	try:
#		
		return psutil.cpu_percent()

#	except :
#		return None

def battery_percentage():
	try:
		return subprocess.check_output("upower -i /org/freedesktop/UPower/devices/battery_BAT0")

	except:
		return None



def memory():
	try:
		return os.system("sudo inxi -m")
	except:
		return None


def de():
    try:
        return os.environ.get('DESKTOP_SESSION')
    except:
        return None


TEMPLATE = """
                           
         
\033[97m       a88888.       {hostname} \033[0m
\033[97m      d888888b.   \033[0m   {hostname_sep}
\033[97m      d888888b.   \033[0m\033[97m  OS: {os_version}
\033[97m      8P"YP"Y88   \033[0m\033[97m  Kernel:{kernel}
\033[96m      8|o||o|88   \033[0m\033[97m  Cpu architecture: {cpu}
\033[96m      8'    .88   \033[0m\033[97m  Shell: {shell}
\033[96m      8'    .88   \033[0m\033[97m  DE(WM): {de}                                
\033[96m      8`._.' Y8   \033[0m\033[97m  Uptime: {uptime}  
\033[96m     d/      `8b. \033[0m\033[97m  Resolution: {size}         
\033[96m   .dP   .     Y8b\033[0m\033[97m  Local IP: {local_ip}
\033[91m   d8:'   "   `::88b. 
\033[91m  d8"           `Y88b
\033[91m :8P     '       :888
\033[91m  8a.    :      _a88
\033[91m  ._/"Yaa_ :    .| 88P|                                                
\033[91m   \    YP"      `| 8P  `.
\033[91m  /     \._____.d|    .'
\033[91m  `--..__)888888P`._.'
                                                                                                         
\033[90m███\033[0m\033[91m███\033[0m\033[92m███\033[0m\033[93m███\033[0m\033[94m███\033[0m\033[95m███\033[0m\033[96m███\033[0m\033[97m███\033[0m

"""


print(TEMPLATE.format(hostname = host_name(),
	hostname_sep = "-" * len(host_name()),
	os_version=os_version(),
	kernel=kernel(),
        cpu=cpu_spec(),
	shell=shell(),
        de=de(),
	uptime=uptime(),
	size=screen_size(),
	local_ip=local_ip()
)
)
os.system("rm -rf .tmp.txt")#temporary file


