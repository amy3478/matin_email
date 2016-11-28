import os, sys, subprocess, getopt
from bs4 import BeautifulSoup as BS
import image_scraper as IS
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Process Args
rss = ''
num = ''
tmp = ''
keyword = ''

try:
	opts, args = getopt.getopt(sys.argv[1:], "hu:n:t:k:", ["url=","num=","tmp=","keyword="])
except getopt.GetoptError:
	print('python3 scraper.py -u <rss-url> -n <num-of-article-to-fetch> -t <path-to-the-template> -k <keyword-to-filter-image>')
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print('python3 scraper.py -u <rss-url> -n <num-of-article-to-fetch> -t <path-to-the-template> -k <keyword-to-filter-image>')
		sys.exit()
	elif opt in ("-u", "--url"):
		rss = requests.get(arg)
	elif opt in ("-n", "--num"):
		num = arg
	elif opt in ("-t", "--tmp"):
		tmp = arg
	elif opt in ("-k", "--keyword"):
		keyword = arg

if (rss == ''):
	print (bcolors.FAIL + '\nPlease specify a correct URL' + bcolors.ENDC + bcolors.OKGREEN + '\n\npython3 scraper.py -u <rss-url> -n <num-of-article-to-fetch> -t <path-to-the-template> -k <keyword-to-filter-image>' + bcolors.ENDC)
	sys.exit()
elif (num == ''):
	print (bcolors.FAIL + '\nPlease specify the number of articles to fetch' + bcolors.ENDC + bcolors.OKGREEN + ' \n\npython3 scraper.py -u <rss-url> -n <num-of-article-to-fetch> -t <path-to-the-template> -k <keyword-to-filter-image>' + bcolors.ENDC)
	sys.exit()
elif (tmp == ''):
	print (bcolors.FAIL + '\nPlease specify a correct path to a template. It should look like "../pages/<filename>" ' + bcolors.ENDC + bcolors.OKGREEN + ' \n\npython3 scraper.py -u <rss-url> -n <num-of-article-to-fetch> -t <path-to-the-template> -k <keyword-to-filter-image>' + bcolors.ENDC)
	sys.exit()
elif (keyword == ''):
	keyword = 'master'

feed = BS(rss.content,'xml')

# print(root.attrib)
new_item = ''

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
