def scrap(wiki):
	from bs4 import BeautifulSoup
	
	import requests
	
	#response = requests.get("https://en.wikipedia.org/wiki/Education")
	response = requests.get(wiki)
	html_data = response.text
	soup2 = BeautifulSoup(html_data)
	
	toc_div = soup2.find('div', id="toc", class_="toc")
	# open file
	target = open("scraped.html", 'w')
	#  delete content
	target.truncate()
	# write to file
	
	target.write(r'<!DOCTYPE html>')
	target.write(r'<html lang="en" dir="ltr" class="client-nojs">'
             r'<head></head>'
             r'<body>')
	target.write(str(toc_div))
	target.write("</body>")
	target.write("</html>")
	target.close()
	return str(toc_div)
scrap("https://en.wikipedia.org/wiki/Education")


