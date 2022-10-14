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

class IP2LocationWebService(object):
    ''' IP2Location web service '''
    def __init__(self,apikey,package,usessl=True):
        if ((re.match(r"^[0-9A-Z]{10}$", apikey) == None) and (apikey != 'demo')):
            raise ValueError("Please provide a valid IP2Location web service API key.")
        if (re.match(r"^WS[0-9]+$", package) == None):
            package = 'WS1'
        self.apikey = apikey
        self.package = package
        self.usessl = usessl
    
    def lookup(self,ip,addons=[],language='en'):
        '''This function will look the given IP address up in IP2Location web service.'''
        parameters = urlencode((("key", self.apikey), ("ip", ip), ("package", self.package), ("addon", ','.join(addons)), ("lang", language)))
        response = httprequest(parameters, self.usessl)
        if (response == None):
            return False
        # if ('response' in response):
        if (('response' in response) and (response['response'] != 'OK')):
            raise IP2LocationAPIError(response['response'])
        return response

    def getcredit(self):
        '''Get the remaing credit in your IP2Location web service account.'''
        parameters = urlencode((("key", self.apikey), ("check", True)))
        response = httprequest(parameters, self.usessl)
        if (response == None):
            return 0
        if ('response' in response is False):
            return 0
        return response['response']
  
class IP2LocationAPIError(Exception):
    """Raise for IP2Location API Error Message"""