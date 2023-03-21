import requests
import json
from bs4 import BeautifulSoup

# Make a GET request to the URL
url = 'https://we.umg.edu.pl/ktm/konsultacje'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# List for data scraped
data = []

for p in soup.select('tr:has(h3)'):
    d = {
        'prof': p.h3.contents[0].strip(),
        'room': p.h3.contents[-1].string.strip(),
        'times': []
    }

    for e in p.find_next_siblings('tr'):
        if e.h3:
            break
        if len(e.text.strip()) > 1 and not e.h5:
            d['times'].append(e.get_text('|',strip=True))
    data.append(d)

json_object = json.dumps(data, indent = 4, ensure_ascii = False) 
print(json_object)