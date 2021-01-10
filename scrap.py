from bs4 import BeautifulSoup
import requests
page = requests.get(
    "http://dataquestio.github.io/web-scraping-pages/simple.html")
#print(page.status_code)
#print(page.content)

# parse with BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

""" Navigating Tags """
#print(list(soup.children))
#print([type(item) for item in list(soup.children)] )
html = list(soup.children)[2] # html tag
body = list(html.children)[3] # body tag
p = list(body.children)[1] # p tag
#print(p.get_text())

""" Find all instances of a tag at once """
soup = BeautifulSoup(page.content, 'html.parser')
# find all instances of p tag
p_instances = soup.find_all('p')
#print(p_instances[0].get_text())

# find the first instance of the p tag
#print(soup.find('p'))

# Seaching tags by class and id
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content,'html.parser')

# Find all p tags with the class tag of "outer-text"
p_tags = soup.find_all("p",class_='outer-text')
#print(p_tags[0].get_text().strip())

# Look for any tag that has class="outer-text"
all_tags = soup.find_all(class_='outer-text')
#print(all_tags)

# Search elements by id
soup.find_all(id='first')

# CSS Selectors - select method - return all instances
css1 = soup.select("div p")
#print(css1)

css2 = soup.select('.outer-text')
print(css2)