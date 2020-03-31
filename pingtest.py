import subprocess
import os
import re
def ping(server='camera1.local', count=1, wait_sec=1):
    """

    :rtype: dict or None
    """
    cmd = "ping -c {} -W {} {}".format(count, wait_sec, server).split(' ')
    try:
        output = subprocess.check_output(cmd).decode().strip()
        lines = output.split("\n")
        total = lines[-2].split(',')[3].split()[1]
	loss = lines[-2].split(',')[2].split()[0]
        timing = lines[-1].split()[3].split('/')

	if(loss[0]=="0"):
	    ipaddr=re.findall(r'\(([^)]+)\)',output)[0]

	    print(ipaddr)
        return {
            'type': 'rtt',
            'min': timing[0],
            'avg': timing[1],
            'max': timing[2],
            'mdev': timing[3],
            'total': total,
            'loss': loss,
            'ipaddr': ipaddr
        }
    except Exception as e:
        print(e)
        return None

ping()

