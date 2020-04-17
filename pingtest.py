import subprocess
import os
import re

class Transform:

    prefix = "http://"
    suffix = ":8081/?action=stream"


    def __init__(self, server , count = 1, wait_sec = 1):
        self.server=server
        """
        :rtype: dict or None
        """
        cmd = "ping -c {} -W {} {}".format(count, wait_sec, self.server).split(' ')

        try:
            output = subprocess.check_output(cmd).decode().strip()
            lines = output.split("\n")
            total = lines[-2].split(',')[3].split()[1]
            loss = lines[-2].split(',')[2].split()[0]
            timing = lines[-1].split()[3].split('/')

            if(loss[0] == "0"):
                self.ipaddr = re.findall(r'\(([^)]+)\)', output)[0]
                #self.ipaddr = ("http://{}:8081/?action=stream\"".format(self.ipaddr))

        except Exception as e:
            print(e)
            return None
    
    def mjpegformat(self) -> str:
        return ( "{prefix}{ip}{suffix}".format(prefix = self.prefix, ip = self.ipaddr ,suffix = self.suffix))


#print(Transform("camera1.local").mjpegformat())
