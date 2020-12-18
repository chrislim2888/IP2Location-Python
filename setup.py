import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="IP2Location",
	version="8.5.1", 
	author="IP2Location",
	author_email="support@ip2location.com",
	description="Python API for IP2Location database.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	py_modules=['IP2Location'],
	url="https://github.com/ip2location/ip2location-python",
	packages=setuptools.find_packages(),
	tests_require=['pytest>=3.0.6'],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
