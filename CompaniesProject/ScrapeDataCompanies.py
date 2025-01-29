import requests
from bs4 import BeautifulSoup
import csv

#url
url = 'https://www.forbes.com/lists/worlds-best-employers/'

#saving data to csv
with open("CompainesEmployee.csv", mode='w', newline='', encoding='utf-8') as file:
    
    writer = csv.writer(file)
    writer.writerow(['name', 'industry', 'country', 'employess'])
    
    try:
        #entering to website
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        companys = soup.find_all('a', class_='table-row')

        for company in companys:
            #extracting name, industry, country, nb_employess
            name = company.find('div', class_='organizationName').text 
            industry = company.find('div', class_='industry').text 
            country = company.find('div', class_='country/territory').text 
            employess = company.find('div', class_='employees').text 
            writer.writerow([name, industry, country, employess])

    except Exception as e:
        print(f"error: {e}")
    
print("Done! :)")