fily = open('fwfix.log','r')
fily = fily.readlines()

import collections
import socket
import requests

outs = []
for i in fily:
    i = i.replace('\n','')
    i = i.split('\t')
    outs.append(i[2])

def most_commad():
    return collections.Counter(outs).most_common(20)

def host_names():

    for i in most_commad():
        ip = i[0].replace('\r', '')
        print ip
        try:
            data = socket.gethostbyaddr(ip)
            print data
        except:
            print ip, 'cant'

def chekck(ip):
    ip = ip
    for i in fily:
        i = i.replace('\n', '')
        i = i.split('\t')
        if ip in i[2]:
            print i



def PSOT_req():
    for i in most_commad():
        ip = i[0].replace('\r', '')

        try:
            r = requests.post('http://' + ip)
            rc = r.headers
            print i, rc
        except:
            print i,'cant'


PSOT_req()


