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

print(rec.country_short)
print(rec.country_long)
print(rec.region)
print(rec.city)
print(rec.isp)	
print(rec.latitude)
print(rec.longitude)			
print(rec.domain)
print(rec.zipcode)
print(rec.timezone)
print(rec.netspeed)
print(rec.idd_code)
print(rec.area_code)
print(rec.weather_code)
print(rec.weather_name)
print(rec.mcc)
print(rec.mnc)
print(rec.mobile_brand)
print(rec.elevation)
print(rec.usage_type)
print("\nYou may download the DB24 sample BIN at http://www.ip2location.com/downloads/sample6.bin.db24.zip for full data display.")

# Web Service
ws = IP2Location.IP2LocationWebService("demo","WS24",True)
rec = ws.lookup("8.8.8.8", ["continent", "country", "region", "city", "geotargeting", "country_groupings", "time_zone_info"], "en")
print (rec)
print ("\n")
print ("Credit Remaining: {}\n".format(ws.getcredit()))

