import os, sys, subprocess
from bs4 import BeautifulSoup as BS
import image_scraper as IS
import requests

# feed = ET.parse('xml/feed.xml')
rss = requests.get(sys.argv[1])
num = sys.argv[2]
tmp = sys.argv[3]
keyword = sys.argv[4]
feed = BS(rss.content,'xml')

# print(root.attrib)

new_item = 1

with open(tmp,'r') as file:
	content = file.read()
	soup = BS(content, 'html.parser')
c = soup.find(id='primary')
n = 0
for item in feed.findAll('item', limit=int(num)):
	# Find the image URL
	url = item.find('link').text
	os.chmod("./imagescraper.sh", 0o755)
	image_urls_str = subprocess.check_output("./imagescraper.sh "+url, shell=True)[:-1].decode("utf-8")
	image_urls = image_urls_str.split()
	image_url = ""
	if keyword == "":
		keyword = "master"
	for this_image_url in image_urls:
		if keyword in this_image_url:
			image_url = this_image_url
	# Get title & description
	title = item.find('title').text
	description = item.find('description').text

	if (image_url == ""):
		new_item = ('<row class="item">'
					'<columns>'
					'<a href="'
					+url+
					'" target="_blank">'
					'<h4 class="title">'
					+title+
					'</h4>'
					'</a>'
					'<p class="description">'
					+description+
					'</p>'
					'<button href="'
					+url+
					'" class="matin radius" target="_blank">View more</button>'
					'</columns>'
					'</row>'
					'<spacer size="24"></spacer>')
	else:
		new_item = ('<row class="item">'
					'<columns>'
					'<a href="'
					+url+
					'" target="_blank">'
					'<h4 class="title">'
					+title+
					'</h4>'
					'</a>'
					'<row>'
					'<columns class="padding-right"  small="12" large="4">'
					'<span class="thumb-wrap">'
					'<img src="'
					+image_url+
					'"></span>'
					'</columns>'
					'<columns small="12" large="8">'
					'<p class="description">'
					+description+
					'</p>'
					'<button href="'
					+url+
					'" class="matin radius" target="_blank">View more</button>'
					'</columns>'
					'</row>'
					'</columns>'
					'</row>'
					'<spacer size="24"></spacer>')

	# template = ET.parse('../pages/index.html')
	new = BS(new_item,'html.parser')
	if n == 0:
		for old_item in c.find_all("row","item"):
			old_item.extract()
		for old_spacer in c.find_all("spacer"):
			old_spacer.extract()
		n = 1
	c.append(new)
with open(tmp, 'wb') as file:
	file.write(soup.prettify('utf-8'))
