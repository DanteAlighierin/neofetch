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

#def cpu_spec():
#	try:
#		return os.system("sudo inxi -m")
#	except:
#		return None

#def cpu_usage():
#	try:
#		
		return psutil.cpu_percent()

#	except :
#		return None

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
         
       a88888.             OS: {os_version}
      d888888b.            Kernel: {kernel}
      8P"YP"Y88            Shell: {shell}
      8|o||o|88            Uptime: {uptime}
      8'    .88            Resolution: {size}
      8`._.' Y8            Local IP: {local_ip}
     d/      `8b.             
   .dP   .     Y8b.
   d8:'   "   `::88b.
  d8"           `Y88b
 :8P     '       :888
  8a.    :      _a88
  ._/"Yaa_ :    .| 88P|                                                
  \    YP"      `| 8P  `.
  /     \._____.d|    .'
  `--..__)888888P`._.'
                                                                                                         
"""


print(TEMPLATE.format(hostname = host_name(),
	hostname_sep = "-" * len(host_name()),
	os_version=os_version(),
	kernel=kernel(),
	shell=shell(),
	uptime=uptime(),
	size=screen_size(),
	local_ip=local_ip()
)
)
os.system("rm -rf .tmp.txt")


