# Copyright (C) 2005-2016 IP2Location.com
# All Rights Reserved
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the MIT license

import os
import IP2Location

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
