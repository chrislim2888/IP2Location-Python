# -*- coding: utf-8 -*-

import pytest

import IP2Location

apikey = "demo"
package = "WS24"
usessl = True
addons = ["continent", "country", "region", "city", "geotargeting", "country_groupings", "time_zone_info"]
language = "en"

ws = IP2Location.IP2LocationWebService(apikey,package,usessl)

def testcountrycode():
    # ws = IP2Location.IP2LocationWebService(apikey,package,usessl)
    rec = ws.lookup("8.8.8.8", addons, language)
    assert rec['country_code'] == "US", "Test failed because country code not same."

def testgetcredit():
    credit = ws.getcredit()
    assert str(credit).isdigit() == True, "Test failed because it is no a digit value."

def testfunctionexist():
    functions_list = ['lookup', 'getcredit']
    for x in range(len(functions_list)): 
        assert hasattr(ws, functions_list[x]) == True, "Function did not exist."