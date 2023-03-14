import requests
from bs4 import BeautifulSoup

# Make a GET request to the URL
url = "https://we.umg.edu.pl/ktm/konsultacje"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the rows in the table
rows = soup.find_all('tr')

# Loop through each row and extract the data
for row in rows:

    # Find all the cells in each row
    cells = row.find_all("td")

    # check if cells isn't empty
    if bool(cells):
        for cell in cells:
            tag = soup.new_tag("br")
            tag.string = "\n"
            cell.replace_with(tag)
            
            clearCell = cell.text

            clearCell = clearCell.replace('\t', '')
            #clearCell = clearCell.replace('\n', '')
            
            print(clearCell)