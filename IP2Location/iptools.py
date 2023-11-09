import sys
import struct
import socket
import re
import json
import os
import ipaddress
import binascii
from re import match

if sys.version < '3':
    import urllib, httplib
    def urlencode(x):
        return urllib.urlencode(x)
    def httprequest(x, usessl):
        try:
            # conn = httplib.HTTPConnection("api.ip2location.com")
            if (usessl is True):
                conn = httplib.HTTPSConnection("api.ip2location.com")
            else:
                conn = httplib.HTTPConnection("api.ip2location.com")
            conn.request("GET", "/v2/?" + x)
            res = conn.getresponse()
            return json.loads(res.read())
        except:
            return None
    def u(x):
        return x.decode('utf-8')
    def b(x):
        return str(x)
else:
    import urllib.parse, http.client
    def urlencode(x):
        return urllib.parse.urlencode(x)
    def httprequest(x, usessl):
        try:
            # conn = http.client.HTTPConnection("api.ip2location.com")
            if (usessl is True):
                conn = http.client.HTTPSConnection("api.ip2location.com")
            else:
                conn = http.client.HTTPConnection("api.ip2location.com")
            conn.request("GET", "/v2/?" + x)
            res = conn.getresponse()
            return json.loads(res.read())
        except:
            return None
    def u(x):
        if isinstance(x, bytes):
            return x.decode()
        return x
    def b(x):
        if isinstance(x, bytes):
            return x
        return x.encode('ascii')
        
# Windows version of Python does not provide it
# for compatibility with older versions of Windows.
if not hasattr(socket, 'inet_pton'):
    def inet_pton(t, addr):
        import ctypes
        a = ctypes.WinDLL('ws2_32.dll')
        in_addr_p = ctypes.create_string_buffer(b(addr))
        if t == socket.AF_INET:
            out_addr_p = ctypes.create_string_buffer(4)
        elif t == socket.AF_INET6:
            out_addr_p = ctypes.create_string_buffer(16)
        n = a.inet_pton(t, in_addr_p, out_addr_p)
        if n == 0:
            raise ValueError('Invalid address')
        return out_addr_p.raw
    socket.inet_pton = inet_pton

def is_ipv4(ip):
    if '.' in ip:
        ip_parts = ip.split('.')
        if len(ip_parts) == 4:
            for i in range(0,len(ip_parts)):
                if str(ip_parts[i]).isdigit():
                    if int(ip_parts[i]) > 255:
                        return False
                else:
                    return False
            pattern = r'^([0-9]{1,3}[.]){3}[0-9]{1,3}$'
            if match(pattern, ip) is not None:
                return 4
        else:
            return False
    else:
        return False
    return False

def is_ipv6(hostname):
    if ':' in hostname:
        return 6
    return False

def is_valid_ip(hostname):
    if is_ipv4(hostname) is not False or is_ipv6(hostname) is not False:
        return True
    else:
        return False

class IP2LocationIPTools(object):

    def is_ipv4(self, ip):
        if '.' in ip:
            ip_parts = ip.split('.')
            if len(ip_parts) == 4:
                for i in range(0,len(ip_parts)):
                    if str(ip_parts[i]).isdigit():
                        if int(ip_parts[i]) > 255:
                            return False
                    else:
                        return False
                pattern = r'^([0-9]{1,3}[.]){3}[0-9]{1,3}$'
                if match(pattern, ip) is not None:
                    return True
            else:
                return False
        else:
            return False
        return False

    def is_ipv6(self, ip):
        try:
            socket.inet_pton(socket.AF_INET6, ip)
        except socket.error:  # not a valid address
            return False
        return True
    
    def ipv4_to_decimal(self, ip):
        try:
            ipnum = struct.unpack('!L', socket.inet_pton(socket.AF_INET, ip))[0]
        except (socket.error, OSError, ValueError):
            # ipnum = -1
            return
        return ipnum
    
    def decimal_to_ipv4(self, decimal):
        if str(decimal).isdigit() is False:
            return
        if (int(decimal) > 4294967295):
            return
        else:
            return (socket.inet_ntoa(struct.pack('!I', int(decimal))))
    
    def ipv6_to_decimal(self, ip):
        if self.is_ipv6(ip) is False:
            return
        return(int(ipaddress.ip_address(u(ip))))
    
    def decimal_to_ipv6(self, decimal):
        if str(decimal).isdigit() is False:
            return
        result = ipaddress.IPv6Address(int(decimal))
        if (result.ipv4_mapped != None):
            return('::ffff:' + str(result.ipv4_mapped))
        else:
            return str(result)
    
    def ipv4_to_cidr(self, from_ip, to_ip):
        if self.is_ipv4(from_ip) is False:
            return
        if self.is_ipv4(to_ip) is False:
            return
        startip = ipaddress.IPv4Address(u(from_ip))
        endip = ipaddress.IPv4Address(u(to_ip))
        ar = [ipaddr for ipaddr in ipaddress.summarize_address_range(startip, endip)]
        ar1 = []
        for i in range(len(ar)):
            ar1.append(str(ar[i]))
        return (ar1)
    
    def ipv6_to_cidr(self, from_ip, to_ip):
        if self.is_ipv6(from_ip) is False:
            return
        if self.is_ipv6(to_ip) is False:
            return
        startip = ipaddress.IPv6Address(u(from_ip))
        endip = ipaddress.IPv6Address(u(to_ip))
        ar = [ipaddr for ipaddr in ipaddress.summarize_address_range(startip, endip)]
        ar1 = []
        for i in range(len(ar)):
            ar1.append(str(ar[i]))
        return (ar1)
    
    def cidr_to_ipv4(self, cidr):
        if '/' not in cidr:
            return
        net = ipaddress.ip_network(u(cidr))
        return({"ip_start": str(net[0]), "ip_end": str(net[-1])})
    
    def cidr_to_ipv6(self, cidr):
        if '/' not in cidr:
            return
        net = ipaddress.ip_network(cidr, False)
        # return({"ip_start": net.network_address.exploded, "ip_end": net.broadcast_address.exploded})
        return({"ip_start": str(net[0]), "ip_end": str(net[-1])})
    
    def compressed_ipv6(self, ip):
        if self.is_ipv6(ip) is False:
            return
        return ((ipaddress.IPv6Address(u(ip)).compressed))
    
    def expand_ipv6(self, ip):
        if self.is_ipv6(ip) is False:
            return
        return ((ipaddress.IPv6Address(u(ip)).exploded))
