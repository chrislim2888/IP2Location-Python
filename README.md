# IP2Location 8.4.1


This is a IP2Location Python library that enables the user to find the country, region or state, city, latitude and longitude, ZIP code, time zone, Internet Service Provider (ISP) or company name, domain name, net speed, area code, weather station code, weather station name, mobile country code (MCC), mobile network code (MNC) and carrier brand, elevation, and usage type by IP address or hostname originates from. The library reads the geo location information from **IP2Location BIN data** file.

Supported IPv4 and IPv6 address.

For more details, please visit:
[https://www.ip2location.com/developers/python](https://www.ip2location.com/developers/python)

# Method

Below are the methods supported in this library.

| Method Name       | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| open              | Open the IP2Location BIN data for lookup. Default mode: File I/O. |
| close             | Close and clean up the file pointer.                         |
| get_all           | Return the geolocation information in array.                 |
| get_country_short | Return the ISO3166-1 country code (2-digits) of the IP address. |
| get_country_long  | Return the ISO3166-1 country name of the IP address.         |
| get_region        | Return the ISO3166-2 region name of the IP address. Please visit [ISO3166-2 Subdivision Code](https://www.ip2location.com/free/iso3166-2) for the information of ISO3166-2 supported |
| get_city          | Return the city name of the IP address.                      |
| get_latitude      | Return the city latitude of the IP address.                  |
| get_longitude     | Return the city longtitude of the IP address.                |
| get_isp           | Return the ISP name of the IP address.                       |
| get_domain        | Return the domain name of IP address.                        |
| get_zipcode       | Return the zipcode of the city.                              |
| get_timezone      | Return the UTC time zone (with DST supported).               |
| get_netspeed      | Return the Internet connection type. Please see [Internet Connection Type](https://github.com/[chrislim2888/IP2Location-Python](https://github.com/chrislim2888/IP2Location-Python)#internet-connection-type) for details. |
| get_idd_code      | Return the IDD prefix to call the city from another country. |
| get_area_code     | Return the area code of the city.                            |
| get_weather_code  | Return the nearest weather observation station code.         |
| get_weather_name  | Return the nearest weather observation station name.         |
| get_mcc           | Return the Mobile Country Codes (MCC).                       |
| get_mnc           | Return the Mobile Network Code (MNC).                        |
| get_mobile_brand  | Commercial brand associated with the mobile carrier. Please visit [Mobile Carrier Coverage](https://www.ip2location.com/mobile-carrier-coverage) to view the coverage report. |
| get_elevation     | Return average height of city above sea level in meters (m). |
| get_usage_type    | Return the ISP's usage type of IP address. Please see [Usage Type](https://github.com/[chrislim2888/IP2Location-Python](https://github.com/chrislim2888/IP2Location-Python)#usage-type) for details. |
|                   |                                                              |

# Requirements

1. Python 2.2 and above

# Installation
1. Unzip the package.
2. Execute python setup.py build
3. Execute python setup.py install

or

To install this module type the following (for PyPI):

```bash
pip install IP2Location
```

# Testing
    python sample.py
    python test.py
    python lookup.py <ip_address>

# Sample BIN Databases
* Download free IP2Location LITE databases at [https://lite.ip2location.com](https://lite.ip2location.com)  
* Download IP2Location sample databases at [https://www.ip2location.com/developers](https://www.ip2location.com/developers)

# IPv4 BIN vs IPv6 BIN
* Use the IPv4 BIN file if you just need to query IPv4 addresses.
* Use the IPv6 BIN file if you need to query BOTH IPv4 and IPv6 addresses.

# Internet Connection Type

| Internet Connection Type | Description                  |
| ------------------------ | ---------------------------- |
| DIAL                     | Dial Up                      |
| DSL                      | Broadband/Cable/Fiber/Mobile |
| COMP                     | Company/T1                   |

# Usage Type

| Usage Type | Description                     |
| ---------- | ------------------------------- |
| COM        | Commercial                      |
| ORG        | Organization                    |
| GOV        | Government                      |
| MIL        | Military                        |
| EDU        | University/College/School       |
| LIB        | Library                         |
| CDN        | Content Delivery Network        |
| ISP        | Fixed Line ISP                  |
| MOB        | Mobile ISP                      |
| DCH        | Data Center/Web Hosting/Transit |
| SES        | Search Engine Spider            |
| RSV        | Reserved                        |

# Support

Email: support@ip2location.com.  
URL: [https://www.ip2location.com](https://www.ip2location.com)
