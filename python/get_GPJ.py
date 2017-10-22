#!/usr/bin/python
import re
import urllib.request
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

def get_html(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html

def get_image(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	image = re.compile(reg)
	html = html.decode('utf-8') #python3
	imglist = re.findall(image, html)
	return imglist

html = get_html("http://www.163.com/")
url = get_image(html)
print (url)