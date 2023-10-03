#!/usr/bin/python3

import requests
from lxml import html
from lxml.html import builder as E
from bs4 import BeautifulSoup as bs

print("Content-type: text/html\n")
#print("<html><body><h1>Canyons</h1>")
#print("<table border=1>")
#print("")

outpage = E.HTML(
  E.BODY(
  E.H1('Canyons'),
  E.TABLE(
)))
table = outpage.xpath('//table')[0]
table.set('border','1')
#table.text="\n\n"

url='https://www.canyon.com/en-cz/gravel-bikes/adventure/grizl/?prefn1=pc_federung_rr&prefv1=No&prefn2=pc_rahmengroesse&prefv2=S&prefn3=pg_weight&prefv3=8%20-%209%20kg%7C9%20-%2010%20kg&srule=sort_price_ascending&format=ajax&showFilters=false&pmin=25.000%2C00&pmax=74.000%2C00'
response = requests.get(url)
page = html.fromstring(response.content)

for div in page.xpath('//li[@class="productGrid__listItem xlt-producttile"]/div'):
  for comparediv in div.xpath('.//div[@class="productTileCompare__wrapper" or @class="productTile__priceMonthly"]'):
    comparediv.getparent().remove(comparediv)

  for a in div.xpath('.//a[@class="productTileDefault__productName link"]'):
    linkedpage = html.fromstring(requests.get(a.get('href')).content)
    for sizebox in linkedpage.xpath('//div[@class="productConfiguration__variantType js-productConfigurationVariantType" and normalize-space()="S"]/..'):
      div.xpath('.//li[@class="productBadges__listItem productBadges__listItem--availability"]')[0].append(sizebox)

#  print("<tr><td>")
  td = html.Element('td')
#  td.text = "\n\n"
  td.append(div)
  tr = html.Element("tr")
  tr.append(td)
#  tr.tail = "\n\n"
  table.append(tr)
#  print(html.tostring(div, encoding=str))
#  print("</td></tr>")
#  print("")

#print("</table>\n</body></html>")

#print(html.tostring(outpage, encoding=str))

outstr = html.tostring(outpage, encoding=str)
soup = bs(outstr, features='lxml')
print(soup.prettify())
