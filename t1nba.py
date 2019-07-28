import socket
import requests
import re

#global serach vars
ip = '143.0.101.24' #bank
localip = '10.0.2.146'
time = '01:58:14'
fily = open('list_of_conections','r')
fily = fily.readlines()
timeNumber = 205679
list_of_c_after_bank = []
port = 8080

#creat i as  list form string

def creat_list(file):
    n = 0
    listy = []
    for i in file:
        i = i.replace('\n', '')
        i = i.split(' ')
        i.append(str(n))  # lets add a count
        n += 1
        listy.append(i)
    return listy
#############################

def search_for_outIP(ip):    
    listof_matchIP = []
    for i in creat_list(fily):
        if str(ip) in str(i[3]):
            listof_matchIP.append(i)
    return listof_matchIP

def set_time_ofC(localip,ip):
    global timeNumber
    for i in creat_list(fily):
        if localip in i[2] and ip in i[3]:
            timeNumber = int(i[4])
    print 'sets timeNumber to :'+str(timeNumber)

def serch_for_LocalIP_after_c_with_ip(localip):
    global timeNumber
    list_of_local_out_after_bank = []
    for i in creat_list(fily):
        if localip in i[2]and timeNumber<= int(i[4]):
            if len(list_of_local_out_after_bank) < 4: #set how many
                list_of_local_out_after_bank.append(i)
            else:
                pass
    return list_of_local_out_after_bank

def serch_for_LocalIP_BEFORE_c_with_ip(localip):
    global timeNumber
    list_of_local_out_before_bank = []
    listmmm = []
    for i in creat_list(fily):
        if localip in i[2]and timeNumber >= int(i[4]):
            listmmm.append(i)
    for i in range(4):
        list_of_local_out_before_bank.append(listmmm[-1])
        listmmm.remove(listmmm[-1])
    return list_of_local_out_before_bank[:-1]

def Make_aList_conectedtwithIP(ip):
    listing =[]
    for i in creat_list(fily):
        if ip in i[3]:
            listing.append([i[2],i[4]])
    return listing


def get_url(function):
    urls = []
    for i in function:
        try:
            urls.append(socket.gethostbyaddr(str(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i[3])[0])))
        except:
            print str(i)+' Error :cant get the URl'
    for i in urls:
        print i

def check_port(listin):

    global port
    for i in listin:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        ip = str(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i[3])[0])
        print ip
        result = sock.connect_ex((ip, port))
        if result == 0:
            print "Port is open"
        else:
            print "Port is not open"
        sock.close()

def send_POSTreq(listing):
    pass

def send_GETreq(listing):
    pass

#check_port(serch_for_LocalIP_BEFORE_c_with_ip(localip))


