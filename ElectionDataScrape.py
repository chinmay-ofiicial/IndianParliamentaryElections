#Importing the necessary libraries.
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#Opening the URL in the given web browser (in this case Firefox).
driver = webdriver.Firefox()
driver.get("https://www.indiavotes.com/pc/party_list/0/17")
page_source = driver.page_source

#creates a 'Soup' object used to parse the HTML content.
soup = BeautifulSoup(page_source, 'html.parser')

# The 'find' feature is used to locate certain content from the HTML.
main = soup.find('div', class_='bodyBg').find('div', class_ = 'main').find('div', class_ = 'mianContent').find('div', class_ = 'mapTabData').find('div', class_='dataTables_wrapper')

#'find_all' finds all the matching elements compared to 'find' which outputs the first matching element. 
#Here find_all is used to find the HTML <th>(table header) element
t1 = main.find_all('th')

#Creates the list of table headers extracted from the previous code and removes unwanted headers. 
header = [title.text.strip() for title in t1]
header = header[13:]
print(header)

#A panda dataframe is created with headers from previous code as columns. Later another column is added to the '0th' position called 'Sr.No.'
df = pd.DataFrame(columns = header)
df.insert(0, 'Sr. No.', '')

#Individual rows(<tr>) and datapoints(<td>) are extracted and added to the dataframe which matches the length of the original dataframe.
t2 = main.find_all('tr', class_ = {'odd', 'even'})
for row in t2:
    r = row.find_all('td')
    ind_row = [data.text.strip() for data in r]
    #print(ind_row)
    length = len(df)
    df.loc[length] = ind_row


#CSV file is created in the end to complete the scraping.
df.to_csv('Election_2019_Partywise.csv', index=False)





