#%%
import pandas as pd 
import numpy as np 
import re
import requests
from bs4 import BeautifulSoup


# %%
url_to_open = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
html = requests.get(url_to_open)

soup = BeautifulSoup(html.content, 'lxml')
table = soup.find("table").find("tbody").find_all("tr")

postalCodes_list = []
borough_list = []
neighbourhood_list = []

# chars to remove
bad_chars = '()'
i = 0
for row in table:
    rows = row.find_all('td')
    for x in rows:
        x_clean = x.get_text().strip()
        postalCodes_list.append(x_clean[:3])
        borough = (x_clean[3:]).split('(')[0]
        borough_list.append(borough)
        match = re.search(r"\([^)]+\)", x_clean)
        if match:
            match_text = match.group(0)
            for c in bad_chars: match_text = match_text.replace(c, "")
            match_text = match_text.replace('/', ",")
            neighbourhood_list.append(match_text)
        else:
            neighbourhood_list.append(borough.replace('/', ","))

postalCodes = {"Postal Code" : postalCodes_list}
boroughs = {"Boroughs" : borough_list}
neighbourhoods = {"Neighbourhoods" : neighbourhood_list}

# %%
dict_list = [postalCodes, boroughs, neighbourhoods]
df1  = pd.DataFrame.from_dict(postalCodes)
df2 = pd.DataFrame.from_dict(boroughs)
df3 = pd.DataFrame.from_dict(neighbourhoods)
df = pd.concat([df1, df2, df3], axis=1, sort=False)
df = df[~df.Boroughs.str.contains('Not assigned')].reset_index(drop=True)


# %%
df.shape

# %%
