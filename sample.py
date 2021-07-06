# Copyright (C) 2005-2019 IP2Location.com
# All Rights Reserved
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the MIT license

import os
import IP2Location

"""
    Cache the database into memory to accelerate lookup speed.
    WARNING: Please make sure your system have sufficient RAM to use this feature.
"""
# database = IP2Location.IP2Location(os.path.join("data", "IPV6-COUNTRY.BIN"), "SHARED_MEMORY")

# Default file I/O lookup
database = IP2Location.IP2Location(os.path.join("data", "IPV6-COUNTRY.BIN"))

rec = database.get_all("19.5.10.1")

print("Country Code          : " + rec.country_short)
print("Country Name          : " + rec.country_long)
print("Region Name           : " + rec.region)
print("City Name             : " + rec.city)
print("ISP Name              : " + rec.isp)
print("Latitude              : " + rec.latitude)
print("Longitude             : " + rec.longitude)
print("Domain Name           : " + rec.domain)
print("ZIP Code              : " + rec.zipcode)
print("Time Zone             : " + rec.timezone)
print("Net Speed             : " + rec.netspeed)
print("Area Code             : " + rec.idd_code)
print("IDD Code              : " + rec.area_code)
print("Weather Station Code  : " + rec.weather_code)
print("Weather Station Name  : " + rec.weather_name)
print("MCC                   : " + rec.mcc)
print("MNC                   : " + rec.mnc)
print("Mobile Carrier        : " + rec.mobile_brand)
print("Elevation             : " + rec.elevation)
print("Usage Type            : " + rec.usage_type)
print("Address Type          : " + rec.address_type)
print("Category              : " + rec.category)
print("\nYou may download the DB25 sample BIN at http://www.ip2location.com/downloads/sample6.bin.db25.zip for full data display.")

# Web Service
ws = IP2Location.IP2LocationWebService("demo","WS25",True)
rec = ws.lookup("8.8.8.8", ["continent", "country", "region", "city", "geotargeting", "country_groupings", "time_zone_info"], "en")
print (rec)
print ("\n")
print ("Credit Remaining: {}\n".format(ws.getcredit()))

