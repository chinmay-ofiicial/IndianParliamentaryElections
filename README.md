# Indian Parliamentary Election
With the 2024 Indian Parliamentary Elections right around the corner, I overviewed the history of the winners of parliamentary election seats from 1962.
Along with the overview, I also dived deep into the most recent 2019 elections to get each party's performance.
The dataset for the overview which is in the 'Loksabha_1962-2019.csv' file is taken from [Kaggle](https://www.kaggle.com/datasets/prabinraj/india-loksabha-elections-data19622019?select=Loksabha_1962-2019+.csv) documented by Prabin Raj. 
The interactive dashboard is done using PowerBi which you can find in the 'Lok_Sabha_Overview.pbix' file. The non-interactive version of this dashboard can be found in 'Lok_Sabha_Overview.pdf'.
The dataset for the party performance is scraped from the [IndiaVotes](/www.indiavotes.com). BeautifulSoup, requests, pandas and selenium Python libraries are used for this web scraping. You can find the code used for web scraping in 'ElectionDataScrape.py' with the output in 'Election_2019_Partywise.csv'.
