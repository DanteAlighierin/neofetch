#!/usr/local/bin/python3

import socket
import os


def local_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	return s.getsockname()[0]


def host_name():
	return socket.gethostname()


def os_version():
	os.system("/usr/sbin/system_profiler SPSoftwareDataType | grep 'System Version' > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			return info.strip()[16:30]


def model():
	os.system("/usr/sbin/system_profiler SPHardwareDataType | grep 'Model Identifier' > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			return info.strip()[18:]


def screen_size():
	os.system("/usr/sbin/system_profiler SPDisplaysDataType |grep Resolution > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			return info.strip()[12:]


def uptime():
	os.system("/usr/sbin/system_profiler SPSoftwareDataType | grep 'Time since boot:' > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			return info.strip()[17:]


def shell():
	return os.environ.get('SHELL', '')


def kernel():
	os.system("uname -a > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			return info.strip()[61:67]


def cpu_spec():
	os.system("sysctl -n machdep.cpu.brand_string | grep Intel > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			cpu = info.strip().replace("CPU", "")
			return cpu.replace("  ", " ")

TEMPLATE = """
\033[92m                    'c.           {hostname} \033[0m
\033[92m                 ,xNMM.\033[0m           {hostname_sep}
\033[92m               .OMMMMo\033[0m\033[93m            OS\033[0m: {os_version}
\033[92m               OMMM0,\033[0m\033[93m             Kernel\033[0m: {kernel}
\033[92m     .;loddo:' loolloddol;.\033[0m\033[93m       Model\033[0m: {model}
\033[92m   cKMMMMMMMMMMNWMMMMMMMMMM0:\033[0m\033[93m     Shell\033[0m: {shell}
\033[93m .KMMMMMMMMMMMMMMMMMMMMMMMWd.\033[0m\033[93m     Uptime\033[0m: {uptime}
\033[93m XMMMMMMMMMMMMMMMMMMMMMMMX.\033[0m\033[93m       Resolution\033[0m: {size}
\033[91m;MMMMMMMMMMMMMMMMMMMMMMMM:\033[0m\033[93m        CPU\033[0m: {cpu}
\033[91m:MMMMMMMMMMMMMMMMMMMMMMMM:\033[0m\033[93m        Local IP\033[0m: {local_ip}
\033[91m.MMMMMMMMMMMMMMMMMMMMMMMMX.\033[0m
\033[91m kMMMMMMMMMMMMMMMMMMMMMMMMWd.\033[0m
\033[95m .XMMMMMMMMMMMMMMMMMMMMMMMMMMk\033[0m
\033[95m  .XMMMMMMMMMMMMMMMMMMMMMMMMK.\033[0m
\033[94m    kMMMMMMMMMMMMMMMMMMMMMMd\033[0m
\033[94m     ;KMMMMMMMWXXWMMMMMMMk.\033[0m
\033[94m       .cooc,.    .,coo:.\033[0m

                                  \033[30m███\033[0m\033[91m███\033[0m\033[92m███\033[0m\033[93m███\033[0m\033[94m███\033[0m\033[95m███\033[0m\033[96m███\033[0m\033[97m███\033[0m
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
	local_ip=local_ip()))

os.system("rm -rf tmp.txt")
