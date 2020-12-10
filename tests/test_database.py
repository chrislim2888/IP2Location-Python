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

def testipv4countrycode():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_all("8.8.8.8")
    assert rec.country_short == "US", "Test failed because country code not same."

def testipv4countryname():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_all("8.8.8.8")
    assert rec.country_long == "United States of America", "Test failed because country name not same."

def testipv4unsupportedfield():
    database = IP2Location.IP2Location(ipv4database)
    rec = database.get_all("8.8.8.8")
    assert rec.city == None, "Test failed because city name not same."

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