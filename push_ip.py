#!/usr/bin/python

import prowlpy
import json
from socket import gethostname
from subprocess import Popen, PIPE
import timeout_decorator

@timeout_decorator.timeout(15)
def send_push(subject=None, priority=1, body=None):
	apikey = json.load(open("/home/pi/auto/creds/prowl.json", "rb"))["apikey"]
	p = prowlpy.Prowl(apikey)
	return p.add(subject, priority, body)
	

def get_ip():
	return Popen("hostname -I", shell=True, stdout=PIPE).communicate()[0].split()[0]


if __name__ == "__main__":
	send_push(subject="{hn} IP".format(hn=gethostname()), priority=0, body=get_ip())
