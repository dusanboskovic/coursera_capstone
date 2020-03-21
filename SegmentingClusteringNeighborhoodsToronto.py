#%%
import pandas as pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup


# %%
url_to_open = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
html = requests.get(url_to_open)

soup = BeautifulSoup(html.content, 'lxml')
rows = soup.find("table").find("tbody").find_all("tr")
#print(rows)

postalCodes = []
i = 0
for row in rows:
    column = row.find_all('td')
    print(column[0].get_text())
    #i += 1
#    postalCodes.append(cells[i].get_text())
 #   print(postalCodes) 
    




# %%
