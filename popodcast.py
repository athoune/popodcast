#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tiny podcast downloader
"""

__author__ = "Mathieu Lecarme <mathieu@garambrogne.net>"

import ConfigParser
import feedparser
import urllib
import time
import os
import os.path
import shutil

class Download(object):
	"Cute download display"
	value = 0
	def __init__(self, title):
		self.title = title
	def __call__(self, block, size, total_size):
 		v = 100 * block * size / total_size
		if v != self.value:
			self.value = v
			print "\033[1A\033[K%s [%i %%]" % (self.title, v)

conf = ConfigParser.ConfigParser()
conf.read('./popodcast.ini')
for section in conf.sections():
	d = feedparser.parse(conf.get(section, 'rss'))
	print d.feed.title
	if not os.path.exists(d.feed.title):
		os.makedirs(d.feed.title)
	for entry in d.entries:
		if not os.path.exists(section):
			os.makedirs(section)
		for mp3 in [link for link in entry.links if link.type == u'audio/mpeg']:
			file = os.path.join(section, "%s_%s.mp3" % (time.strftime("%Y-%m-%d_%H-%M-%S", entry.updated_parsed), entry.title))
			if not os.path.exists(file):
				urllib.urlretrieve(mp3.href, 'tmp.mp3', Download("%s: %s" % (d.feed.title, entry.title)))
				shutil.move('tmp.mp3', file)
