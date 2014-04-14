import struct
import socket

class IP2LocationRecord:
    ''' IP2Location record with all fields from the database '''
    ip = None
    country_short = None
    country_long = None
    region = None
    city = None
    isp = None
    latitude = None
    longitude = None
    domain = None
    zipcode = None
    timezone = None
    netspeed = None
    idd_code = None
    area_code = None
    weather_code = None
    weather_name = None
    mcc = None
    mnc = None
    mobile_brand = None
    elevation = None
    usage_type = None

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

_COUNTRY_POSITION             = (0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
_REGION_POSITION              = (0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
_CITY_POSITION                = (0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)
_ISP_POSITION                 = (0, 0, 3, 0, 5, 0, 7, 5, 7, 0, 8, 0, 9, 0, 9, 0, 9, 0, 9, 7, 9, 0, 9, 7, 9)
_LATITUDE_POSITION            = (0, 0, 0, 0, 0, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
_LONGITUDE_POSITION           = (0, 0, 0, 0, 0, 6, 6, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)
_DOMAIN_POSITION              = (0, 0, 0, 0, 0, 0, 0, 6, 8, 0, 9, 0, 10,0, 10, 0, 10, 0, 10, 8, 10, 0, 10, 8, 10)
_ZIPCODE_POSITION             = (0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 7, 7, 7, 0, 7, 0, 7, 7, 7, 0, 7)
_TIMEZONE_POSITION            = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 7, 8, 8, 8, 7, 8, 0, 8, 8, 8, 0, 8)
_NETSPEED_POSITION            = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 11,0, 11,8, 11, 0, 11, 0, 11, 0, 11)
_IDDCODE_POSITION             = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 12, 0, 12, 0, 12, 9, 12, 0, 12)
_AREACODE_POSITION            = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10 ,13 ,0, 13, 0, 13, 10, 13, 0, 13)
_WEATHERSTATIONCODE_POSITION  = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 14, 0, 14, 0, 14, 0, 14)
_WEATHERSTATIONNAME_POSITION  = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 15, 0, 15, 0, 15, 0, 15)
_MCC_POSITION                 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 16, 0, 16, 9, 16)
_MNC_POSITION                 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,17, 0, 17, 10, 17)
_MOBILEBRAND_POSITION         = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11,18, 0, 18, 11, 18)
_ELEVATION_POSITION           = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 19, 0, 19)
_USAGETYPE_POSITION           = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 20)

_IPV4 = 0
_IPV6 = 1

class IP2Location(object):
    ''' IP2Location database '''

    def __init__(self, filename=None):
        if filename:
            self.open(filename)

    def open(self, filename):
        self._f = open(filename, 'rb')
        self._dbtype = struct.unpack('B', self._f.read(1))[0]
        self._dbcolumn = struct.unpack('B', self._f.read(1))[0]
        self._dbyear = struct.unpack('B', self._f.read(1))[0]
        self._dbmonth = struct.unpack('B', self._f.read(1))[0]
        self._dbday = struct.unpack('B', self._f.read(1))[0]
        self._dbcount = struct.unpack('<I', self._f.read(4))[0]
        self._dbaddr = struct.unpack('<I', self._f.read(4))[0]
        self._ipversion = struct.unpack('<I', self._f.read(4))[0]

    def get_country_short(self, ip):
        ''' Get country_short '''
        rec = self.get_all(ip)
        return rec and rec.country_short
    def get_country_long(self, ip):
        ''' Get country_long '''
        rec = self.get_all(ip)
        return rec and rec.country_long
    def get_region(self, ip):
        ''' Get region '''
        rec = self.get_all(ip)
        return rec and rec.region
    def get_city(self, ip):
        ''' Get city '''
        rec = self.get_all(ip)
        return rec and rec.city
    def get_isp(self, ip):
        ''' Get isp '''
        rec = self.get_all(ip)
        return rec and rec.isp
    def get_latitude(self, ip):
        ''' Get latitude '''
        rec = self.get_all(ip)
        return rec and rec.latitude
    def get_longitude(self, ip):
        ''' Get longitude '''
        rec = self.get_all(ip)
        return rec and rec.longitude
    def get_domain(self, ip):
        ''' Get domain '''
        rec = self.get_all(ip)
        return rec and rec.domain
    def get_zipcode(self, ip):
        ''' Get zipcode '''
        rec = self.get_all(ip)
        return rec and rec.zipcode
    def get_timezone(self, ip):
        ''' Get timezone '''
        rec = self.get_all(ip)
        return rec and rec.timezone
    def get_netspeed(self, ip):
        ''' Get netspeed '''
        rec = self.get_all(ip)
        return rec and rec.netspeed
    def get_idd_code(self, ip):
        ''' Get idd_code '''
        rec = self.get_all(ip)
        return rec and rec.idd_code
    def get_area_code(self, ip):
        ''' Get area_code '''
        rec = self.get_all(ip)
        return rec and rec.area_code
    def get_weather_code(self, ip):
        ''' Get weather_code '''
        rec = self.get_all(ip)
        return rec and rec.weather_code
    def get_weather_name(self, ip):
        ''' Get weather_name '''
        rec = self.get_all(ip)
        return rec and rec.weather_name
    def get_mcc(self, ip):
        ''' Get mcc '''
        rec = self.get_all(ip)
        return rec and rec.mcc
    def get_mnc(self, ip):
        ''' Get mnc '''
        rec = self.get_all(ip)
        return rec and rec.mnc
    def get_mobile_brand(self, ip):
        ''' Get mobile_brand '''
        rec = self.get_all(ip)
        return rec and rec.mobile_brand
    def get_elevation(self, ip):
        ''' Get elevation '''
        rec = self.get_all(ip)
        return rec and rec.elevation
    def get_usage_type(self, ip):
        ''' Get usage_type '''
        rec = self.get_all(ip)
        return rec and rec.usage_type
    def get_all(self, ip):
        ''' Get all '''
        return self._get_record(ip)

    def find(self, ip):
        ''' Find IP record '''
        return self._get_record(ip)

    def _reads(self, offset):
        self._f.seek(offset - 1)
        n = struct.unpack('B', self._f.read(1))[0]
        return str(self._f.read(n))

    def _readi(self, offset):
        self._f.seek(offset - 1)
        return struct.unpack('<I', self._f.read(4))[0]

    def _readf(self, offset):
        self._f.seek(offset - 1)
        return struct.unpack('<f', self._f.read(4))[0]

    def _readip(self, offset):
        if self._ipversion == _IPV4:
            return self._readi(offset)
        elif self._ipversion == _IPV6:
            a, b, c, d = self._readi(offset), self._readi(offset + 4), self._readi(offset + 8), self._readi(offset + 12) 
            return (d << 96) | (c << 64) | (b << 32) | a

    def _readips(self, offset):
        if self._ipversion == _IPV4:
            return socket.inet_ntoa(struct.pack('!L', self._readi(offset)))
        elif self._ipversion == _IPV6:
            return str(self._readip(offset))

    def _read_record(self, mid):
        baseaddr = self._dbaddr
        rec = IP2LocationRecord()
        rec.ip = self._readips(baseaddr + (mid) * self._dbcolumn * 4)

        if self._ipversion == _IPV4:
            off = 0
        elif self._ipversion == _IPV6:
            off = 12

        def calc_off(what, mid):
            return self._dbaddr + mid * (self._dbcolumn * 4 + off) + off + 4 * (what[self._dbtype]-1)

        if _COUNTRY_POSITION[self._dbtype] != 0:
            rec.country_short = self._reads(self._readi(calc_off(_COUNTRY_POSITION, mid)) + 1)
            rec.country_long =  self._reads(self._readi(calc_off(_COUNTRY_POSITION, mid)) + 4)

        if _REGION_POSITION[self._dbtype] != 0:
            rec.region = self._reads(self._readi(calc_off(_REGION_POSITION, mid)) + 1)
        if _CITY_POSITION[self._dbtype] != 0:
            rec.city = self._reads(self._readi(calc_off(_CITY_POSITION, mid)) + 1)
        if _ISP_POSITION[self._dbtype] != 0:
            rec.isp = self._reads(self._readi(calc_off(_ISP_POSITION, mid)) + 1)

        if _LATITUDE_POSITION[self._dbtype] != 0:
            rec.latitude = self._readf(calc_off(_LATITUDE_POSITION, mid))
        if _LONGITUDE_POSITION[self._dbtype] != 0:
            rec.longitude = self._readf(calc_off(_LONGITUDE_POSITION, mid))

        if _DOMAIN_POSITION[self._dbtype] != 0:
            rec.domain = self._reads(self._readi(calc_off(_DOMAIN_POSITION, mid)) + 1)

        if _ZIPCODE_POSITION[self._dbtype] != 0:
            rec.zipcode = self._reads(self._readi(calc_off(_ZIPCODE_POSITION, mid)) + 1)

        if _TIMEZONE_POSITION[self._dbtype] != 0:
            rec.timezone = self._reads(self._readi(calc_off(_TIMEZONE_POSITION, mid)) + 1)
                
        if _NETSPEED_POSITION[self._dbtype] != 0:
            rec.netspeed = self._reads(self._readi(calc_off(_NETSPEED_POSITION, mid)) + 1)

        if _IDDCODE_POSITION[self._dbtype] != 0:
            rec.idd_code = self._reads(self._readi(calc_off(_IDDCODE_POSITION, mid)) + 1)

        if _AREACODE_POSITION[self._dbtype] != 0:
            rec.area_code = self._reads(self._readi(calc_off(_AREACODE_POSITION, mid)) + 1)

        if _WEATHERSTATIONCODE_POSITION[self._dbtype] != 0:
            rec.weather_code = self._reads(self._readi(calc_off(_WEATHERSTATIONCODE_POSITION, mid)) + 1)

        if _WEATHERSTATIONNAME_POSITION[self._dbtype] != 0:
            rec.weather_name = self._reads(self._readi(calc_off(_WEATHERSTATIONNAME_POSITION, mid)) + 1)

        if _MCC_POSITION[self._dbtype] != 0:
            rec.mcc = self._reads(self._readi(calc_off(_MCC_POSITION, mid)) + 1)

        if _MNC_POSITION[self._dbtype] != 0:
            rec.mnc = self._reads(self._readi(calc_off(_MNC_POSITION, mid)) + 1)

        if _MOBILEBRAND_POSITION[self._dbtype] != 0:
            rec.mobile_brand = self._reads(self._readi(calc_off(_MOBILEBRAND_POSITION, mid)) + 1)
                
        if _ELEVATION_POSITION[self._dbtype] != 0:
            rec.elevation = self._reads(self._readi(calc_off(_ELEVATION_POSITION, mid)) + 1)

        if _USAGETYPE_POSITION[self._dbtype] != 0:
            rec.usage_type = self._reads(self._readi(calc_off(_USAGETYPE_POSITION, mid)) + 1)

        return rec

    def __iter__(self):
        low = 0
        high = self._dbcount

        while low <= high:
            yield self._read_record(low)
            low += 1
  
    def _get_record(self, ip):
        baseaddr = self._dbaddr
        low = 0
        high = self._dbcount

        if self._ipversion == _IPV4:
            ipno = struct.unpack('!L', socket.inet_aton(ip))[0]
            off = 0
        elif self._ipversion == _IPV6:
            a, b = struct.unpack('!QQ', socket.inet_pton(socket.AF_INET6, ip))
            ipno = (a << 64) | b
            off = 12

        while low <= high:
            mid = int((low + high) / 2)
            ipfrom = self._readip(baseaddr + (mid) * (self._dbcolumn * 4 + off))
            ipto = self._readip(baseaddr + (mid + 1) * (self._dbcolumn * 4 + off))

            if ipfrom <= ipno < ipto:
                return self._read_record(mid)
            else:
                if ipno < ipfrom:
                    high = mid - 1
                else:
                    low = mid + 1
