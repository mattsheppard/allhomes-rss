#!/usr/bin/python

"""allhomes-rss
A very basic screen scraper for allhomes.com.au

See http://code.google.com/p/allhomes-rss/ for details

Copyright (c) 2008, Matthew Sheppard
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
 and/or other materials provided with the distribution.

Neither the name of the Matthew Sheppard nor the names of its contributors
may be used to endorse or promote products derived from this software
without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import urllib
import re
from BeautifulSoup import BeautifulSoup
import cgi
import sys

def main(argv=sys.argv):
	
	url = "test.html"
	if len(argv) > 1:
		url = argv[1]
	
	data = urllib.urlopen(url).read()
	soup = BeautifulSoup(data)
	
	messySuburb = soup.find(id="breadCrumbs").contents[-1]
	suburb = re.compile('^&nbsp;&gt;&nbsp;\s*([\w\s\']+)\s*$', re.M).search(messySuburb).groups()[0]
	
	print """<?xml version="1.0" encoding="utf-8"?>
	<rss version="2.0">
	<channel>
		<title>All Homes : """ + suburb + """</title>
		<link>""" + url + """</link>
	"""
	
	for table in soup.findAll('tbody'):
		for row in table.findAll('tr'):
			
			tds = row.findAll('td');
			if len(tds) < 1:
				continue
			
			td = row.findAll('td')[0]
			if td is None:
				continue
			
			a = td.find('a')
			if a is None:
				continue
			
			print "<item>"
			
			print "<title>"
			print suburb + " : " + str(a.contents[0])
			print "</title>"
			
			print "<link>"
			print "http://www.allhomes.com.au/ah/" + a['href']
			print "</link>"
			
			print "<description>"
			description = ""
			for td in tds:
				description += "".join(["%s" % (v) for v in td.contents])
			description = description.replace("image/camera.gif", "http://www.allhomes.com.au/ah/image/camera.gif")
			description = description.replace("href=\"", "href=\"http://www.allhomes.com.au/ah/")
			print cgi.escape(description)
			print "</description>"
			
			print "</item>"
	
	print """	</channel>
	</rss>
	"""

if __name__ == "__main__":
    main()