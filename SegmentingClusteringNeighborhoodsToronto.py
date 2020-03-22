#%%
import pandas as pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup


# %%
url_to_open = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
html = requests.get(url_to_open)

soup = BeautifulSoup(html.content, 'lxml')
table = soup.find("table").find("tbody").find_all("tr")

postalCodes = {}
i = 0
for row in table:
    rows = row.find_all('td')
    for x in rows:
        key = x.get_text().strip()[:3]
        value = x.get_text().strip()[3:]
        postalCodes[key] = value

column_names = ['Postal Code', 'Borough', 'Neighbourhood']
df  = pd.DataFrame.from_dict(data=postalCodes, orient='index')
df.head()
    




# %%
