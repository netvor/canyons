#!/usr/bin/python3

print("Content-type: text/html\n")
print("<html><body><h1>Canyons</h1>")


import requests
mySizes=['M','L']
urls=[
 'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=2708&dwvar_2708_pv_rahmenfarbe=GN&dwvar_2708_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=2708&dwvar_2708_pv_rahmenfarbe=GY%2FBK&dwvar_2708_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=3243&dwvar_3243_pv_rahmenfarbe=YE&dwvar_3243_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=3243&dwvar_3243_pv_rahmenfarbe=GY%2FBK&dwvar_3243_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=3092&dwvar_3092_pv_rahmenfarbe=R062_P15&dwvar_3092_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=3092&dwvar_3092_pv_rahmenfarbe=YE%2FBK&dwvar_3092_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=3092&dwvar_3092_pv_rahmenfarbe=GN%2FBK&dwvar_3092_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=3093&dwvar_3093_pv_rahmenfarbe=R062_P15&dwvar_3093_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=3093&dwvar_3093_pv_rahmenfarbe=YE%2FBK&dwvar_3093_pv_rahmengroesse=&quantity=undefined'
,'https://www.canyon.com/on/demandware.store/Sites-RoW-Site/en_CZ/Product-Variation?pid=3093&dwvar_3093_pv_rahmenfarbe=GN%2FBK&dwvar_3093_pv_rahmengroesse=&quantity=undefined'
]

for url in urls:
  response = requests.get(url)
  j = response.json()

  detail_dict= j['gtmModel'][0]['ecommerce']['detail']['products'][0]
  header=', '.join([detail_dict[k] for k in detail_dict if k in ('name','dimension51')])
  content=["<dl><dt>{}</dt><dd>{}</dd></dl>".format(v['displayValue'],v['availability']['shippingInfo']) for v in j['productData']['variationAttributes'][1]['values'] if v['displayValue'] in mySizes ]

  print(f"<h2>{header}</h2>")
  print("\n".join(content))

print("</body></html>")
