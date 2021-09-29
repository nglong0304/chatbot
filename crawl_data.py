import requests
from bs4 import BeautifulSoup
import csv
# get the requests from the wiki page
response = requests.get(
	url="https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data",
)
soup = BeautifulSoup(response.content, 'html.parser')

# open the file in the write mode
f = open('covid_data.csv', 'w')
# create the csv writer
writer = csv.writer(f)

#get data from the world row
world_case = soup.find(id="thetable").find_all("tr")[1]
world_case = world_case.find_all("th")[2:-1]
world_case_data=list()
for element in world_case :
		if ("</span>" in str(element.contents[0])) :
			world_case_data.append("no data")
		elif not "</sup>"  in str(element.contents[0]):
			world_case_data.append(str(element.contents[0][:-1]))

all_rows = soup.find(id="thetable").find("tbody")
all_rows = all_rows.find_all("tr")

writer.writerow(["Location","Cases","Deaths","Recoveries"])
writer.writerow(list(["World"]+world_case_data))

for row in all_rows[2:-2]:
	#get all the cases of a country
	cases=row.find_all("td")
	cases_data=list()
	for element in cases :
		if ("</span>" in str(element.contents[0])) :
			cases_data.append("no data")
		elif not "</sup>"  in str(element.contents[0]):
			cases_data.append(str(element.contents[0][:-1]))
	#get the name of a country
	country=row.find_all("th")
	country= country[-1].find("a")
	if "</i>" in str(country.contents[0]):
		country=country.find("i")	
	# write a row to the csv file
	writer.writerow(list([country.contents[0]]+cases_data))

# close the file
f.close()
