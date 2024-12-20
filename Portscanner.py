import socket
import termcolor

def scan(target,ports):
        print('\n' + 'Starting Scan for' + str(target))
        for port in range(1,ports):
             scanport(target,port)

def scanport(ipaddress,port):
        try:
            sock = socket.socket()
            sock.connect((ipaddress,port))
            print(" Port Open "+str(port))
            sock.close()
        except:
            pass
targets= input("Enter the targets  to scan:")
ports =int( input("Enter the number of  port to scan : "))
if ',' in targets:
        print(termcolor.colored(("[*]Scanning multiple targets"),'green'))
        for ipaddr in targets.split(','):
                  scan(ipaddr.strip(' '),ports)
else:
       scan (targets,ports)
