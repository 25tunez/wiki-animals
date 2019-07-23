from bs4 import BeautifulSoup
import urllib.request as ur

#scrape a wikipedia page for a list of animals

#parse the wiki page
urlToScrape = "https://en.wikipedia.org/wiki/List_of_animal_names"
r = ur.urlopen(urlToScrape).read()
soup = BeautifulSoup(r, "lxml") #transform URL to HTML that can be parsed

#extra step to make data more readable
soup = soup.prettify() 
soup = BeautifulSoup(soup, 'lxml')

table_rows = soup.find_all("tr") #get all the table row tags
animal_names = [] #to store the animal names

#info from first chart on wikipedia page
for table_row in table_rows[2:13]: ##make this more general
    table_data = table_row.contents[1] #second element of tr tag is a td
    animal_names.append(table_data.a["title"]) #find a tag under table data and use the title attribute to store as the animal name

print(animal_names)
