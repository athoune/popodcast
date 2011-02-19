#!/usr/bin/env python

import ConfigParser
import feedparser

conf = ConfigParser.ConfigParser()
conf.read('./popodcast.ini')
for section in conf.sections():
	d = feedparser.parse(conf.get(section, 'rss'))
	print d