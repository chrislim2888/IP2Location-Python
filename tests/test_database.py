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
    functions_list = ['open', 'close', 'get_all', 'get_country_short', 'get_country_long', 'get_region', 'get_city', 'get_latitude', 'get_longitude', 'get_isp', 'get_domain', 'get_zipcode', 'get_timezone', 'get_netspeed', 'get_idd_code', 'get_area_code', 'get_weather_code', 'get_weather_name', 'get_mcc', 'get_mnc', 'get_mobile_brand', 'get_elevation', 'get_usage_type', 'get_district', 'get_asn', 'get_as', 'get_asdomain', 'get_asusagetype', 'get_ascidr']
    for x in range(len(functions_list)): 
        assert hasattr(database, functions_list[x]) == True, f"Function {functions_list[x]} did not exist."

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
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetcity():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_city("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetlatitude():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_latitude("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetlongitude():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_longitude("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetisp():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_isp("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetdomain():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_domain("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetzipcode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_zipcode("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgettimezone():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_timezone("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetnetspeed():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_netspeed("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetiddcode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_idd_code("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetareacode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_area_code("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetweathercode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_weather_code("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetweathername():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_weather_name("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetmcc():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_mcc("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetmnc():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_mnc("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetmobilebrand():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_mobile_brand("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetelevation():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_elevation("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetusagetype():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_usage_type("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetdistrict():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_district("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetasn():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_asn("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetas():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_as("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetasdomain():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_asdomain("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetasusagetype():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_asusagetype("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

def testgetascidr():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_ascidr("8.8.8.8")
    assert rec == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.'

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
    assert rec.city == 'This parameter is unavailable in selected .BIN data file. Please upgrade data file.', "Test failed because city name not same."