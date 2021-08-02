import requests  

# for xml & html scrapping 
from bs4 import BeautifulSoup 

# for table analysis
import pandas as pd

# write to csv
import csv







# url of wikipedia page from which you want to scrap tabular data.
url1 = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"

# Session helps to object allows you to persist certain parameters across requests
# By default, Request will keep waiting for a response indefinitely. Therefore, it is advised to set the timeout parameter.
# If the request was successful, you should see the reponse output as '200'.
s = requests.Session()
response = s.get(url1, timeout=10)
#response2 = s.get(url2, timeout=5)
response


# parse response content to html
soup = BeautifulSoup(response.content, 'html.parser')

# to view the content in html format
pretty_soup = soup.prettify()


soup.title.string

right_table=soup.find('table', {"class":'wikitable sortable'})


filename = 'road_safety_facts_and_figures.csv'
f = open(filename,'w')
csv_writer = csv.writer(f)


for tr in right_table.find_all('tr'):
    header = []
    data = []


    for th in tr.find_all('th'):
        header.append(th.text.strip())
        
    if header:
        csv_writer.writerow(header)
        
    for td in tr.find_all('td'):
      data.append(td.text.strip())
        
    if data:
      csv_writer.writerow(data)
csv_writer      
f.close()  

# read_csv function which is used to read the required CSV file
data = pd.read_csv('road_safety_facts_and_figures.csv')

  
# del function which is used in removing or deleting rows or columns from the CSV files
del data['Number of Seriously Injured in 2017/2018[30]']
del data['Number of People Killed\n'+'per Billion km[30]']
data.to_csv('road_safety_facts_and_figures.csv', index=False, na_rep='Unknown')
  
# display
print ("CSV with specified columns")
print (data)


sorted_data = data.sort_values(by=["Road deaths\n"+"per Million Inhabitants in 2018[30]"], ascending=True)
sorted_data.to_csv('road_safety_facts_and_figures.csv', index=False, na_rep='Unknown')
print ("CSV with sorted 'Road deaths per Million Inhabitants in 2018'\n")
print (sorted_data)