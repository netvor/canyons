#!/usr/bin/python3

print("Content-type: text/html\n")
print("<html><body><h1>Canyons</h1>")
print("<table border=1>")
print("")

import requests
from lxml import html

url='https://www.canyon.com/en-cz/gravel-bikes/adventure/grizl/?prefn1=pc_federung_rr&prefv1=No&prefn2=pc_rahmengroesse&prefv2=S&prefn3=pg_weight&prefv3=10%20-%2011%20kg%7C9%20-%2010%20kg&srule=sort_price_ascending&format=ajax&showFilters=false&pmin=25.000%2C00&pmax=69.000%2C00'
response = requests.get(url)
page = html.fromstring(response.content)

for div in page.xpath('//li[@class="productGrid__listItem xlt-producttile"]/div'):
  print("<tr><td>")
  print(html.tostring(div, encoding=str))
  print("</td></tr>")
  print("")

print("</table>\n</body></html>")
