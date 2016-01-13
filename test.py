# Copyright (C) 2005-2013 IP2Location.com
# All Rights Reserved
#
# This library is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; If not, see <http://www.gnu.org/licenses/>.
from __future__ import with_statement

import os
import sys
import IP2Location

database = IP2Location.IP2Location()

passed = 0
failed = 0
test_num = 0

database.open(os.path.join("data", "IP-COUNTRY.BIN"))
for line in open(os.path.join("data", "country_test_ipv4_data.txt")):
    addr, country_short = line.strip().split()
    rec = database.get_all(addr)

    test_num += 1
    if rec is not None:
        if rec.country_short != country_short:
            failed += 1
            print("Test IP Address %s (Test %d) failed. We got %s but expected %s" \
                    % (addr, test_num, rec and rec.country_short or 'None', country_short))
        else:
            passed += 1

database.open(os.path.join("data", "IPV6-COUNTRY.BIN"))
for line in open(os.path.join("data", "country_test_ipv6_data.txt")):
    addr, country_short = line.strip().split()
    rec = database.get_all(addr)

    test_num += 1
    if rec is not None:
        if rec.country_short != country_short:
            failed += 1
            print("Test IP Address %s (Test %d) failed. We got %s but expected %s" \
                    % (addr, test_num, rec and rec.country_short or 'None', country_short))
        else:
            passed += 1

test_num += 1
try:
    database.close()
except:
    failed += 1
    print("Test DB closing (Test %d) failed." % (test_num))
else:
    passed += 1

test_num += 1
try:
    with database:
        pass
except ValueError:
    passed += 1
else:
    failed += 1
    print("Test 'with' statement with closed db failed (Test %d)" % (test_num))


test_num += 1
try:
    with IP2Location.IP2Location(os.path.join("data", "IP-COUNTRY.BIN")) as db:
        rec = db.get_all('19.5.10.1')
except:
    failed += 1
    print("Test With statement failed (Test %d)" % (test_num))
    raise
else:
    passed += 1

print('PASS: %d' % (passed))
print('FAIL: %d' % (failed))
