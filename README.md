This is just a very simple screen scraper I hacked up (back in 2008) on top of Beautiful Soup so I could watch new property listing one allhomes.com.au (pages like http://www.allhomes.com.au/ah/ah0069?lstype=res&divid=10008) in my RSS reader. Obviously this will only be of even the remotest interest to you if you live in Canberra, Australia, and are interested in buying a house.

For now, I'm just using it with NetNewsWire's script subscription option. It could probably be deployed on a web server pretty simply, but the all homes guys might get a bit touchy if too much traffic starts coming from one place. I suppose you could just have the script dump it's output for each URL you're interested in to a static file every hour or something.

Anyway, you can run it with...

allhomes-rss.py <url of suburb listing page>, and it will return a feed of each listing.

(Automatically exported from code.google.com/p/allhomes-rss)
