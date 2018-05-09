# N4xD0rk

Listing subdomains about a main domain using the technique called Hacking with search engines.

# Instalation

You can download the latest version of N4xD0rk by cloning the GitHub repository:

<pre> git clone https://github.com/n4xh4ck5/N4xD0rk.git</pre>

Install the dependencies via pip:

<pre> pip install -r requirements.txt </pre>

To install properly phantomJS follow the next steps:

<pre>
Linux (Debian, Ubuntu, Kali)

apt-get update && apt-get install phantomjs

Linux (other distributions)

Get the latest phantomjs program. The current version was 2.1.1 at the time of writing this tutorial.

http://phantomjs.org/download.html

https://bitbucket.org/ariya/phantomjs/downloads


Download it on your system (choose 32 or 64bits) and untar it wherever you want, let's say /opt

$ cd /opt

$ wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

$ tar xvf phantomjs-2.1.1-linux-x86_64.tar.bz2

Make a symlink to the phantomjs binary in your /usr/local/bin directory

$ ln -s /opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs

Execute the binary with the -v option to check that everything works

$ phantomjs -v

2.1.1</pre>

# Usage

<pre>usage: n4xd0rk.py [-h] -t TARGET -n NUMBER [-e EXPORT] [-l LANGUAGE]
                  [-c CAPTURE]

This script searchs the subdomains about a domain using the results indexed of Google and Bing search.

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        The domain or IP which wants to search.
  -n NUMBER, --number NUMBER
                        Indicate the number of the search which you want to do.
  -e EXPORT, --export EXPORT
                        Export the results to a json file (Y/N)
                         Format available:
                        	1.json
                        	2.xlsx
  -l LANGUAGE, --language LANGUAGE
                        Indicate the language of the search
                        	(es)-Spanish(default)
  -c CAPTURE, --capture CAPTURE
                        Indicate if you want to take a screenshot of each web (y/n)
</pre>

# Example
<pre>
python n4xd0rk.py -t apple.com -n 1

	   _   _ _  _        _____   ___       _ 
	  | \ | | || |      |  __ \ / _ \     | |
	  |  \| | || |___  _| |  | | | | |_ __| | __
	  | . ` |__   _\ \/ / |  | | | | | '__| |/ /
	  | |\  |  | |  >  <| |__| | |_| | |  |   < 
	  |_| \_|  |_| /_/\_\_____/ \___/|_|  |_|\_\  



	** Tool to search the subdomains about a domain using the results indexed of Google and Bing search
    ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
    ** DISCLAMER This tool was developed for educational goals. 
    ** The author is not responsible for using to others goals.
    ** A high power, carries a high responsibility!
    ** Version 2.1
 
This script obtains the IP associated a domain

 			Example of usage: python n4xd0rk.py -t apple.com -n 5 

Looking domains and subdomains of target apple.com

 Domains and subdomains of apple.com are:


	- www.apple.com [23.XXX.XX.83]


	- communities.apple.com [23.XXX.XXX.242]


	- selfsolve.apple.com [88.XXX.XXX.168]


	- checkcoverage.apple.com [88.XXX.XXX.168]


	- support.apple.com [104.XXX.XXX.98]


	- itunes.apple.com [23.XXX.XXX.95]


	- araes.apple.com [17.XXX.XXX.53]
  
  </pre>

# Author

Ignacio Brihuega Rodríguez aka n4xh4ck5

Twitter:  @n4xh4ck5

Web: fwhibbit.es

# Disclamer

The use of this tool is your responsability. I hereby disclaim any responsibility for actions taken with this tool.
