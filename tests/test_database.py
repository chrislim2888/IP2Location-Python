# -*- coding: utf-8 -*-

import pytest

import os, IP2Location

ipv4database = os.path.join("data", "IP2LOCATION-LITE-DB1.BIN")

ipv6database = os.path.join("data", "IP2LOCATION-LITE-DB1.IPV6.BIN")

def testinvaliddatabase():
    try:
        database = IP2Location.IP2Location(os.path.join("data", "NULL.BIN"))
    except ValueError as e:
        assert "The database file does not seem to exist." == str(e)

def testfunctionexist():
    database = IP2Location.IP2Location(ipv4database)
    functions_list = ['open', 'close', 'get_all', 'get_country_short', 'get_country_long', 'get_region', 'get_city', 'get_latitude', 'get_longitude', 'get_isp', 'get_domain', 'get_zipcode', 'get_timezone', 'get_netspeed', 'get_idd_code', 'get_area_code', 'get_weather_code', 'get_weather_name', 'get_mcc', 'get_mnc', 'get_mobile_brand', 'get_elevation', 'get_usage_type']
    for x in range(len(functions_list)): 
        assert hasattr(database, functions_list[x]) == True, "Function did not exist."

def testipv4countrycode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_all("8.8.8.8")
    assert rec.country_short == "US", "Test failed because country code not same."

def testipv4countryname():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_all("8.8.8.8")
    assert rec.country_long == "United States of America", "Test failed because country name not same."

def testgetcountryshort():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_country_short("8.8.8.8")
    assert rec == "US", "Test failed because country code not same."

def testgetcountrylong():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_country_long("8.8.8.8")
    assert rec == "United States of America", "Test failed because country name not same."

def testgetregion():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_region("8.8.8.8")
    assert rec == None

def testgetcity():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_city("8.8.8.8")
    assert rec == None

def testgetlatitude():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_latitude("8.8.8.8")
    assert rec == None

def testgetlongitude():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_longitude("8.8.8.8")
    assert rec == None

def testgetisp():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_isp("8.8.8.8")
    assert rec == None

def testgetdomain():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_domain("8.8.8.8")
    assert rec == None

def testgetzipcode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_zipcode("8.8.8.8")
    assert rec == None

def testgettimezone():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_timezone("8.8.8.8")
    assert rec == None

def testgetnetspeed():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_netspeed("8.8.8.8")
    assert rec == None

def testgetiddcode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_idd_code("8.8.8.8")
    assert rec == None

def testgetareacode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_area_code("8.8.8.8")
    assert rec == None

def testgetweathercode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_weather_code("8.8.8.8")
    assert rec == None

def testgetweathername():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_weather_name("8.8.8.8")
    assert rec == None

def testgetmcc():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_mcc("8.8.8.8")
    assert rec == None

def testgetmnc():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_mnc("8.8.8.8")
    assert rec == None

def testgetmobilebrand():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_mobile_brand("8.8.8.8")
    assert rec == None

def testgetelevation():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_elevation("8.8.8.8")
    assert rec == None

def testgetusagetype():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_usage_type("8.8.8.8")
    assert rec == None

def testipv6countrycode():
    database = IP2Location.IP2Location(ipv6database)
    rec = database.get_all("2001:4860:4860::8888")
    assert rec.country_short == "US", "Test failed because country code not same."

def testipv6countryname():
    database = IP2Location.IP2Location(ipv6database)
    rec = database.get_all("2001:4860:4860::8888")
    assert rec.country_long == "United States of America", "Test failed because country name not same."

def testipv6unsupportedfield():
    database = IP2Location.IP2Location(ipv6database)
    rec = database.get_all("2001:4860:4860::8888")
    assert rec.city == None, "Test failed because city name not same."