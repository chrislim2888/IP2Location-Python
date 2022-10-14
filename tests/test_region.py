# -*- coding: utf-8 -*-

import pytest

import os, IP2Location

region = IP2Location1.Region(os.path.join("data", "IP2LOCATION-ISO3166-2.CSV")

def test_region_code():
    region_code = region.get_region_code("US", "California")
    assert "US-CA" == region_code