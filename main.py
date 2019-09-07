import socket
import json
import ssl

def main():
    hosts = get_hosts()

    for host in hosts:
        print(host + ";" + get_ip(host) + ";" + get_ssl_cn(host))

def get_ssl_cn(host):
    try:
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=host)
        s.connect((host, 443))
        cert = s.getpeercert()

        subject = dict(x[0] for x in cert['subject'])
        issued_to = subject['commonName']

        return issued_to
    except:
        return 'NO_CERT'

def get_ip(host):
    try:
        return socket.gethostbyname(host) 
    except:
        return 'NO_RESOLVED'
    
def get_hosts():
    with open('hosts.json', 'r') as f:
       file_dict = json.load(f) 

    return file_dict['hosts']


if __name__ == "__main__":
    main()