# -*- coding: utf-8 -*-

import os
import socket
import subprocess
import sys


IS_PY3 = sys.version_info >= (3, 0)


_system_profiler_cache = {}


def _system_profiler(resource, name):
    global  _system_profiler_cache
    if resource not in _system_profiler_cache:
        proc = subprocess.Popen(["/usr/sbin/system_profiler", resource], stdout=subprocess.PIPE)
        stdout, _stderr = proc.communicate()
        if IS_PY3:
            stdout = str(stdout, "utf-8")
        res = {}
        for line in stdout.splitlines():
            line = line.strip().split(': ')
            if len(line) > 1:
                res[line[0]] = line[1]
        _system_profiler_cache[resource] = res
    return _system_profiler_cache[resource][name]


def _strip_output(*command, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(command, **kwargs)
    stdout, _stderr = proc.communicate()
    if IS_PY3:
        stdout = str(stdout, "utf-8")
    return stdout.strip()


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_hostname():
    return socket.gethostname()


def get_os_version():
    return _system_profiler("SPSoftwareDataType", "System Version")


def get_model():
    return _system_profiler("SPHardwareDataType", "Model Identifier")


def get_screen_size():
    return _system_profiler("SPDisplaysDataType", "Resolution")


def get_uptime():
    return _system_profiler("SPSoftwareDataType", "Time since boot")


def get_shell():
    return os.environ.get('SHELL', '')


def get_kernel():
    return _strip_output("uname", "-r")


def get_cpu_spec():
    return _strip_output("sysctl", "-n", "machdep.cpu.brand_string")


TEMPLATE = u"""
\033[92m                    'c.           {hostname}\033[0m
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


def main():
    hostname = get_hostname()
    return TEMPLATE.format(
        hostname=hostname,
        hostname_sep="-" * len(hostname),
        os_version=get_os_version(),
        kernel=get_kernel(),
        model=get_model(),
        shell=get_shell(),
        uptime=get_uptime(),
        size=get_screen_size(),
        cpu=get_cpu_spec(),
        local_ip=get_local_ip()
    )


if __name__ == '__main__':
    print(main())
