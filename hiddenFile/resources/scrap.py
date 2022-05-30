from bs4 import BeautifulSoup
import requests
def findFlag(url):
    html_text = requests.get(url).text
    #print(url)

    if (url.find('README') != -1 and html_text.find('Moi') == -1 and html_text.find('Toujours') == -1 and html_text.find('du') == -1 and html_text.find('toujours') == -1 and html_text.find('gauche') == -1 and html_text.find('Demande') == -1):
        print(url)
        print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    links = soup.find_all('a')
    for link in links:
        if (link.text.find('..') == -1):
            findFlag(url + link.text)
    
html_text = requests.get("http://10.12.100.119/.hidden/").text
soup = BeautifulSoup(html_text, 'lxml')
links = soup.find_all('a')
for link in links:
       if (link.text.find('README') == -1 and link.text.find('..') == -1):
            findFlag("http://10.12.100.119/.hidden/" + link.text)
