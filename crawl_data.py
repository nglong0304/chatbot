import requests
from bs4 import BeautifulSoup


response = requests.get(
	url="https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data",
)

soup = BeautifulSoup(response.content, 'html.parser')

# all_rows = soup.find(id="thetable").find_all("tr")

all_rows = soup.find(id="thetable").find("tbody")
all_rows = all_rows.find_all(("tr"))

for row in all_rows[2:-2]:
	print("!!!!!!!!!!!!!!!! end a row !!!!!!!!!!!!!!!")

	# cases=row.find_all("td")
	# for element in cases :
	# 	if ("</span>" in str(element.contents[0])) :
	# 		print("no data")
	# 	elif not "</sup>"  in str(element.contents[0]):
	# 		print(element.contents[0][:-1])

	country=row.find_all("th")
	country= country[-1].find("a")
	if "</i>" in str(country.contents[0]):
		country=country.find("i")
	print(country.contents[0])
	
# for row in all_rows:
# 	print(row.contents)
