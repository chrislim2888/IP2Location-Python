# IP2Location 8.10.0


This is a IP2Location Python library that enables the user to find the country, region or state, city, latitude and longitude, ZIP code, time zone, Internet Service Provider (ISP) or company name, domain name, net speed, area code, weather station code, weather station name, mobile country code (MCC), mobile network code (MNC) and carrier brand, elevation, usage type, address type and IAB category by IP address or hostname originates from. The library reads the geo location information from **IP2Location BIN data** file.

Supported IPv4 and IPv6 address.

For more details, please visit:
[https://www.ip2location.com/developers/python](https://www.ip2location.com/developers/python)

** Requires Python 3.5 and above.**

# Online Documentation
Online documentation is available at here: [https://ip2location-python.readthedocs.io/en/latest/index.html](https://ip2location-python.readthedocs.io/en/latest/index.html).

# Installation

1. Unzip the package.
2. Execute python setup.py build
3. Execute python setup.py install

or

To install this module type the following (for PyPI):

```bash
pip install IP2Location
```

# Usage

You can check the **sample.py** file to learn more about usage. To learn more on the classes and functions available, you can find out at here: [https://ip2location-python.readthedocs.io/en/latest/code.html](https://ip2location-python.readthedocs.io/en/latest/code.html).

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
