#!/usr/bin/env python

import ConfigParser
import feedparser
import urllib
import time
import os
import os.path
import shutil

def download(block, size, total_size):
	print 100 * block * size / total_size

conf = ConfigParser.ConfigParser()
conf.read('./popodcast.ini')
for section in conf.sections():
	d = feedparser.parse(conf.get(section, 'rss'))
	print d.feed.title
	if not os.path.exists(d.feed.title):
		os.makedirs(d.feed.title)
	for entry in d.entries:
		print "\t", entry.title
		if not os.path.exists(entry.title):
			os.makedirs(entry.title)
		for mp3 in [link for link in entry.links if link.type == u'audio/mpeg']:
			print mp3
			file = os.path.join(d.feed.title, "%s_%s.mp3" % (entry.title, time.strftime("%Y-%m-%d_%H-%M-%S", entry.updated_parsed)))
			if not os.path.exists(file):
				urllib.urlretrieve(mp3.href, 'tmp.mp3', download)
				shutil.move('tmp.mp3', file)
