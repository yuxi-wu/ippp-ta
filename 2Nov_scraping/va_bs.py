from bs4 import BeautifulSoup
import requests

url_va = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'

# just things you do every time
req_va = requests.get(url_va)
html_va = req_va.content #getting the contents of the website
soup = BeautifulSoup(html_va,'html.parser') #turning it into a soup object so you can manipulate in python

#open the html of url_va (you can do this if you right click anywhere on page and select 'view page source'
#search for '80871' when you look at the HTML of the page.
#what kind of tag comes in front?:

#find 'tr' tags with class 'election_item because these contain the ID'
tags = soup.find_all('tr','election_item')

#if you just want to look at 2016's data
lastyear = tags[0]
lastyear_id = lastyear['id'] #text of id
lastyear_id = lastyear['id'][-5:] #you only want the last five characters

#printing all of the year/id pairs
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    print(year, year_id)
#...now do the same thing, but put it all in a list called ELECTION_ID
#maybe you can do this with a list comprehension!

#the base URL that all downloads pages have
base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'

#the url for 2016
lastyear_url = base.format('80871')
lastyear_text = requests.get(lastyear_url).text

#writing 2016 to a csv
with open('2016.csv', 'w') as output:
    output.write(requests.get(lastyear_url).text)
