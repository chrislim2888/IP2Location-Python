# -*- coding: utf-8 -*-

import pytest

import IP2Location

ipTools = IP2Location.IP2LocationIPTools()

def testipv4():
    assert ipTools.is_ipv4('8.8.8.8') == True

def testinvalidipv4():
    assert ipTools.is_ipv4('8.8.8.555') == False

def testipv6():
    assert ipTools.is_ipv6('2001:4860:4860::8888') == True

def testinvalidipv6():
    assert ipTools.is_ipv6('2001:4860:4860::ZZZZ') == False

def testipv4decimal():
    assert ipTools.ipv4_to_decimal('8.8.8.8') == 134744072

def testdecimalipv4():
    assert ipTools.decimal_to_ipv4(134744072) == '8.8.8.8'

def testipv6decimal():
    assert ipTools.ipv6_to_decimal('2001:4860:4860::8888') == 42541956123769884636017138956568135816

def testdecimalipv6():
    assert ipTools.decimal_to_ipv6(42541956123769884636017138956568135816) == '2001:4860:4860::8888'

def testipv4tocidr():
    assert ipTools.ipv4_to_cidr('8.0.0.0', '8.255.255.255') == ['8.0.0.0/8']

def testcidrtoipv4():
    assert ipTools.cidr_to_ipv4('8.0.0.0/8') == {'ip_start': '8.0.0.0', 'ip_end': '8.255.255.255'}

def testipv6tocidr():
    assert ipTools.ipv6_to_cidr('2002:0000:0000:1234:abcd:ffff:c0a8:0000', '2002:0000:0000:1234:ffff:ffff:ffff:ffff') == ['2002::1234:abcd:ffff:c0a8:0/109', '2002::1234:abcd:ffff:c0b0:0/108', '2002::1234:abcd:ffff:c0c0:0/106', '2002::1234:abcd:ffff:c100:0/104', '2002::1234:abcd:ffff:c200:0/103', '2002::1234:abcd:ffff:c400:0/102', '2002::1234:abcd:ffff:c800:0/101', '2002::1234:abcd:ffff:d000:0/100', '2002::1234:abcd:ffff:e000:0/99', '2002:0:0:1234:abce::/79', '2002:0:0:1234:abd0::/76', '2002:0:0:1234:abe0::/75', '2002:0:0:1234:ac00::/70', '2002:0:0:1234:b000::/68', '2002:0:0:1234:c000::/66']

def testcidrtoipv6():
    assert ipTools.cidr_to_ipv6('2002::1234:abcd:ffff:c0a8:101/64') == {'ip_start': '2002:0000:0000:1234:abcd:ffff:c0a8:0101', 'ip_end': '2002:0000:0000:1234:ffff:ffff:ffff:ffff'}

def testcompressipv6():
    assert ipTools.compressed_ipv6('2002:0000:0000:1234:FFFF:FFFF:FFFF:FFFF') == '2002::1234:ffff:ffff:ffff:ffff'

def testexpandipv6():
    assert ipTools.expand_ipv6('2002::1234:FFFF:FFFF:FFFF:FFFF') == '2002:0000:0000:1234:ffff:ffff:ffff:ffff'
