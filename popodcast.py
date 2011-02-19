#!/usr/bin/env python

import ConfigParser
import feedparser

conf = ConfigParser.ConfigParser()
conf.read('./popodcast.ini')
for section in conf.sections():
	d = feedparser.parse(conf.get(section, 'rss'))
	print d.feed.title
	for entry in d.entries:
		print "\t", entry.title
		for mp3 in [link for link in entry.links if link.type == u'audio/mpeg']:
			print mp3
