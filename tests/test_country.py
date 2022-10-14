# -*- coding: utf-8 -*-

import pytest

import os, IP2Location

country = IP2Location.Country(os.path.join("data", "IP2LOCATION-COUNTRY-INFORMATION-BASIC.CSV"))

def test_country_code_field():
    country_information = country.get_country_info("US")
    assert "country_code" in country_information

def test_country_code_value():
    country_information = country.get_country_info("US")
    assert country_information["country_code"] == "US"

def test_capital():
    country_information = country.get_country_info("MY")
    assert country_information["capital"] == "Kuala Lumpur"