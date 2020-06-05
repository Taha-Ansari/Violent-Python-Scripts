#!/usr/bin/python
import socket
import nmap

class PortScanner:
    def get_ip(self, hostname):
        return socket.gethostbyname(hostname)

    def check_port(self, host, port):
        # Will throw an exception if connection to socket fails to initialize
        try:
            s = socket.socket()
            s.connect((host, port))
            r = s.recv(150)
            print("Port {}: Open | {}".format(port, str(r)))
            s.close()
        except:
            print("Port {}: Closed".format(port))

    def execute_scan(self, host, ports):
        # Assuming ip is standard ipv4 with 3 '.' chars
        is_ip = True if host.count(".") == 3 else False

        # Convert hostname to ip if required
        if not is_ip:
            host = self.get_ip(host)
            print("IP address for target is: {}".format(host))

        # Check ports
        for port in ports:
            self.check_port(host, port)

        print("Scan complete")   

if __name__ == '__main__':

    # Init scanner obj
    ps = PortScanner()

    # Commonly used ports
    ports = [21, 22, 80, 443]
    host = input("Enter ip address or full web address: ") or '192.168.2.131'
    
    # Execute TCP Scan or Nmap
    ps.execute_scan(host, ports)