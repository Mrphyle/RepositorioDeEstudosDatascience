import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Formula_One_World_Constructors'_Champions"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.select_one('table.wikitable.sortable')

if table:
    rows = table.find_all('tr')
    dados = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 9:
            year = cols[0].find('a').get_text(strip=True)
            constructor = cols[1].get_text(strip=True)
            chassis = cols[2].get_text(strip=True)
            engine = cols[3].get_text(strip=True)
            tyres = cols[4].get_text(strip=True)
            wins = cols[5].get_text(strip=True)
            poles = cols[6].get_text(strip=True)
            podiums = cols[7].get_text(strip=True)
            points = cols[8].get_text(strip=True)
            
            dados.append([year, constructor, chassis, engine, tyres, wins, poles, podiums, points])

    for dado in dados:
        print(f"Year: {dado[0]}")
        print(f"Constructor: {dado[1]}")
        print(f"Chassis: {dado[2]}")
        print(f"Engine: {dado[3]}")
        print(f"Tyres: {dado[4]}")
        print(f"Wins: {dado[5]}")
        print(f"Poles: {dado[6]}")
        print(f"Podiums: {dado[7]}")
        print(f"Points: {dado[8]}")
        print('-' * 40)
else:
    print("Error: Could not find the data table on the page.")
    print("The page structure might have changed.")
