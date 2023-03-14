import requests
from bs4 import BeautifulSoup

# Make a GET request to the URL
url = "https://we.umg.edu.pl/ktm/konsultacje"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content)

# Find all the rows in the table
rows = soup.find_all('tr')

emptyList = []

# Loop through each row and extract the data
for row in rows:
    # Find all the cells in each row
    cells = row.find_all("td")

    # check if cells isn't empty
    if bool(cells):
        print(cells)
        
    # Extrac    t the text from each cell
#    name = cells[0].text.strip()
#    time = cells[1].text.strip()
#    room = cells[2].text.strip()
    # Display the data
#    print(f"{name}: {time} ({room})")