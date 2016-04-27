mport requests
# import re 
from bs4 import BeautifulSoup
import wget

def get_image_url(num):
	"""Returns image URL from a number."""
	url = 'http://www.xkcd.com/' + str(num)
	r = requests.get(url)
	data = r.text
	if '404' in data:
		print('Page not found for',num+'.')
		exit()
	soup = BeautifulSoup(data)
	d = str(soup.find_all('div',{'id':'comic'})[0])
	arr = d.split()
	s = ''
	for string in arr:
		if 'src' in string:
			s = string
			s = s[7:-1]
	return s

def download_image(img_url):
	"""Downloads image using wget."""
	arr = img_url.split('/')
	wget.download('http://'+img_url,arr[-1])
	print('\n\nDownloaded image for',arr[-1])

if __name__ == '__main__':
	num = 1
	while(True):
		try:
			download_image(get_image_url(num))
		except Exception:
			pass
		num += 1
