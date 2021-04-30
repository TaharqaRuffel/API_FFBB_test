# import libraries
from bs4 import BeautifulSoup
import urllib3.request
import urllib.request
import urllib.parse
import csv

#urlpage = 'https://resultats.ffbb.com/championnat/equipe/2263.html'
urlpage = 'https://resultats.ffbb.com/championnat/equipe/2263.html'

http = urllib3.PoolManager()

# specify the url
r = http.request('GET',urlpage)
soup = BeautifulSoup(r.data,'html5lib')
table = soup.find('select', attrs={'id': 'idCompetitionsSelect'})
#results = table.find_all('tr')
print(table)

#f = urllib.request.urlopen(urlpage)
#print(f.read().decode('utf-8'))


#
# http = urllib3.PoolManager()
# #r = http.request('GET', 'https://resultats.ffbb.com/championnat/equipe/2263.html')
# r = http.request('GET', 'https://resultats.ffbb.com/championnat/equipe/division/b5e6211f20d0b5e6212069de2263.html')
#
# # query the website and return the html to the variable 'page'
# #page = urllib3.request.urlopen(urlpage)
#
# # parse the html using beautiful soup and store in variable 'soup'
# soup = BeautifulSoup(r.data,'html5lib')
#
#
# # find results within table
# table = soup.find('table', attrs={'class': 'liste'})
#
# test = BeautifulSoup(r.data,'lxml')
#
# print(len(BeautifulSoup(r.data, 'html.parser').find_all('table', attrs={'class': 'liste'})))
# print(len(BeautifulSoup(r.data, 'lxml').find_all('table', attrs={'class': 'liste'})))
# print(len(BeautifulSoup(r.data, 'xml').find_all('table', attrs={'class': 'liste'})))
# print(len(BeautifulSoup(r.data, 'html5lib').find_all('table', attrs={'class': 'liste'})))
#
#
# # results = table.find_all('tr')
# print('Number of results', len(results))

