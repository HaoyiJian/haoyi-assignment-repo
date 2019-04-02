import urllib2, csv
from bs4 import BeautifulSoup
#read files named urllib2 with format “.csv”. Using the python language BeautifulSoup to scrap the data.
outfile = open('jaildata.csv', 'w')
writer = csv.writer(outfile)
#open a file named ‘jaildata.csv’ and ________
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
html = urllib2.urlopen(url).read()
#address of url, html
soup = BeautifulSoup(html, "html.parser")
#open html and store
tbody = soup.find('tbody', {'class': 'stripe'})
#find all ‘tbody’ in soup and store them in tbody
rows = tbody.find_all('tr')
#find all ‘tr’ in tbody and store them in rows
for row in rows:

    cells = row.find_all('td')
#The first loop to repeat scrapping rows
    data = []
    for cell in cells:
        data.append(cell.text.encode('utf-8'))
#The second loop to repeat scrapping cells
    writer.writerow(data)
#write the data into computer
