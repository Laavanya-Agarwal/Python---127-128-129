from bs4 import BeautifulSoup as bs #tried installing bs4 but its showing some error
import requests
import pandas as pd

#opening website
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Confirmed_brown_dwarfs_orbiting_primary_stars"
page = requests.get(START_URL)
print(page)

#reading it and finding data from the table
soup = bs(page.text, 'html.parser')
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')

# staring it
temp_list = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

# creating all arrays
Star = []
Constellation = []
Right_ascension = []
Declination = []
App_mag = []
Distance = []
Spectral_type = []
Brown_dwarf = []
Mass = []
Radius = []
Orbital_period = []
Semimajor_axis = []
Ecc = []
Discovery_year = []

for i in range(1,len(temp_list)):
    Brown_dwarf.append(temp_list[i][0])
    
df2 = pd.DataFrame(list(zip(Star,Constellation,Right_ascension,Declination,App_mag,Distance,Spectral_type,Brown_dwarf,Mass,Radius,Orbital_period,Semimajor_axis,Ecc,Discovery_year)), columns=['Star','Constellation','Right_ascension','Declination','App_mag','Distance,Spectral_type','Brown_dwarf','Mass','Radius','Orbital_period','Semimajor_axis','Ecc','Discovery_year'])
print(df2)

df2.to_csv('dwarf_stars.csv')