# N4xD0rk
Listing subdomains about a main domain using the technique called Hacking with search engines.
# Usage
<pre>usage: n4xd0rk.py [-h] [-d DOMAIN] [-i IP] -o OPTION -n SEARCH [-e EXPORT]
                  [-l LANGUAGE]

This script searchs the subdomains about a domain using the results indexed of Bing search.

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        The domain which wants to search.
  -i IP, --ip IP        The IP which to kown the domains to contain.
  -o OPTION, --option OPTION
                        Select an option:
                        	1. Searching the subdomains about a domain using the results indexed.
                        	2. Searching the domains belong to an IP.
  -n SEARCH, --search SEARCH
                        Indicate the number of the search which you want to do.
  -e EXPORT, --export EXPORT
                        Export the results to a json file (Y/N)
                         Format available:
                        	1.json
                        	2.xlsx
  -l LANGUAGE, --language LANGUAGE
                        Indicate the language of the search
                        	(es)-Spanish(default)
                        	(en)-English
</pre>
