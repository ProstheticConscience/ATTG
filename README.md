#Autonomous Tor Traffic Generator

**Autonomous Tor Traffic Generator** or **A.T.T.G.** It is a set of python script's for generating http requests sent over the Tor network.
This tool will allow the user to request data from websites periodically, simulating traffic to various international and multi-interest websites.

## Purpose

The Autonomous Tor Traffic Generator is designed and developed to create http requests from specific urls and routing 
the traffic through the Tor network. Web traffic routed over Tor can protect your anonymity and privacy by masking what
websites you are visiting, but certain usage patterns can be derived from when you are and are not using the Tor network.
A.T.T.G. will request basic http traffic from multiple websites and serve a simple response simulating usage of Tor.

The purpose of this software is as follows:

* Stimulate the Tor network with traffic to simulate usage of Tor

* Protect the user from certain usage pattern correlations.

The purpose of this software is **not**:

* To harm the Tor network or any of its Users in anyway.

* To be considered any extra protection Tor or similar software would offer.

* To be used for any malicious/illegal purpose .

## Required Software

* Python Version v3+:	https://www.python.org/

	* Requests v2.10:	https://pypi.python.org/pypi/requests

	* SocksiPy v1.0:	https://pypi.python.org/pypi/SocksiPy

* Tor Browser:			https://www.torproject.org

Recommend Using pip with Python to install the external packages.

Tor browser is required to use A.T.T.G. The Tor browser must be installed and running correctly for A.T.T.G. to route traffic over the Tor network.

Please ensure all security concerns when downloading and installing the Tor browser, such as verification of signed signatures.

## Usage

Please ensure you have Python 3 or great and all requisite software/packages installed.

To check which version of python you are running type into command line/terminal
```
python -v
```

Download, Verify and Install

* Python Version 3
* Requests
* SocksiPy
* Tor browser

Run the Tor browser.

Open and run the scripts from your Python IDE, such as IDLE the default basic Python IDE.

Script can also be run from the terminal by navigating to the folder and running,
```python
Python3 -main0.4.py
```
or equivalent for your Operating System. Please ensure Python3 is in your environment path if using Windows OS.

The delay time between calls can be changed by navigating to and changing the variable assigned to timeDel.
```python
def runTimer():
	global timeDel
	timedel = 1
```

This will create a one second delay between successive URL calls and will ensure the script runs as quickly as possible, roughly 20-30 minutes.
A value of 10 will create a 10 second delay between calls and will ensure the script takes approximately one hour to run.

By default A.T.T.G. only does one iteration of the whole test suit of URL's. 
To simply increase the number of times the lists will cycle by duplicating the URLrequest variable with mainControl.
```python
def mainControl():
	print('Starting A.T.T.G.')
	print('Generating Requests')
	runTimer()
	time.sleep(2)
	URLrequest()
	'''
	print('second cycle')
	time.sleep(2)
	URLrequest()
	'''
```	

URLrequest can be called as many times as you wish with mainControl to rerun the requests increasing the total time A.T.T.G. runs before exiting. 
Combined with a 10second delay from above, this can simulate multiple hours.

## Version

Version 0.4

## Author

Prosthetic.Conscience 

## Contact

prosthetic.conscience@riseup.net

###GPG
Key ID = F46F7399

A copy of the public key can be found on keyservers or in F46F7399.asc

## License

Licensed under the GPLv3: https://www.gnu.org/licenses/gpl-3.0.html

    Autonomous Tor Traffic Generator. A tool to generate web traffic over the Tor network.
    Copyright (C) 2016  Prosthetic.Conscience

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
