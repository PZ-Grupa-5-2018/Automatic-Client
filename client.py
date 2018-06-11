import requests
import platform
import os
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-me", "--measurement", help="= measurement")
parser.add_argument("-a", "--active", dest='active', action='store_true')
parser.add_argument("-na", "--noactive", dest='active', action='store_false')
parser.set_defaults(active=True)
parser.add_argument("-nh", "--nhosts", type=int, help="= nhosts")
parser.set_defaults(nhosts=10)
parser.add_argument("-mo", "--monitors", nargs='+', help="= monitors")
args = parser.parse_args()

try:
    while True:
        hosts_data = []
        for monitor in args.monitors:
            url = monitor
            monitor_url = url
            url = url + "/hosts/"
            response = requests.get(url+"?active={}".format(args.active))
            hosts = response.json()
            for host in hosts:
                host_url = url + str(host["id"]) + "/metrics/{}/measurements?count=1".format(args.measurement)
                host_response = requests.get(host_url)
                measurements = host_response.json()
                if type(measurements) is list:
                    host["load"] = measurements[0]['value']
                    hosts_data.append(host)
            top_hosts = sorted(hosts_data,key=lambda k: k['load'], reverse=True)
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        print("{:<20}{:<20}{:<20}".format('HOST', 'IP', args.measurement))
        for top_host in top_hosts[0:args.nhosts]:
            print("{:<20}{:<20}{:<20}".format(top_host['name'], top_host['ip'], top_host['load']))
        time.sleep(5)
except KeyboardInterrupt:
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
    exit()

