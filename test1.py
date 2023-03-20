import requests
from bs4 import BeautifulSoup

# Make a GET request to the URL
url = "https://we.umg.edu.pl/ktm/konsultacje"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

roomsProfessors = soup.find_all('h3')

# Lists for sorted data
professors = []
rooms = []

for roomProfessor in roomsProfessors:
    professor = []

    for child in roomProfessor:
        if child.name == 'br':
            continue

        child = child.string.replace('\t', '').replace('\n', '')

        if 'pok.' in child:
            rooms.append(child)
        else:
            professor.append(child)
        
    professors.append(professor)

print('Count professors: ' + str(len(professors)))
print(professors)
print('=================')
print('Count rooms: ' + str(len(rooms)))
print(rooms)