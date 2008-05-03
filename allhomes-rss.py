#!/usr/bin/python

"""allhomes-rss
A very basic screen scraper for allhomes.com.au
Copyright (c) 2008, Matthew Sheppard

See http://code.google.com/p/allhomes-rss/ for details
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