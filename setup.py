import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="IP2Location",
	version="8.10.2", 
	author="IP2Location",
	author_email="support@ip2location.com",
	description="This is an IP geolocation library that enables the user to find the country, region, city, latitude and longitude, ZIP code, time zone, ISP, domain name, area code, weather info, mobile info, elevation, usage type, address type and IAB category from an IP address. It supports both IPv4 and IPv6 lookup.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/chrislim2888/ip2location-python",
	packages=setuptools.find_packages(),
	tests_require=['pytest>=3.0.6'],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
