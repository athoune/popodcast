Popodcast
=========

Handling podcast without bloated software

Install it
----------

You need feedparser. You can fetch it from [feed parser](http://feedparser.org/) or install it from package or python install tools

	sudo pip install feedparser

chmod it

	chmod +x popodcast.py

Configure it
------------

Create a _popodcast.ini_ file with such line for each podcast :

	[2000 ans d'histoire]
	rss: http://radiofrance-podcast.net/podcast09/rss_14864.xml

Use it
------

	./popodcast.py

You can use a crontab or just do it manualy. One folder per feed is created, containing entries, with sortable name.