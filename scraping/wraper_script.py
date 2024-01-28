import requests
from bs4 import BeautifulSoup
import json

base_url = "https://avocatalgerien.com/listings/page/{}/"
output_file = "lawyers.json"

start_page = 1
end_page = 73

data_list = []

for page_number in range(start_page, end_page + 1):
    url = base_url.format(page_number)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            lawyer_data = {}

            lawyer_data["Name"] = article.find("h2", class_="entry-title").text.strip()
            lawyer_data["Categories"] = article.find("p", class_="listing-cat").text.strip()
            lawyer_data["Address"] = article.find("p", class_="listing-address").text.strip()
            lawyer_data["Phone"] = article.find("p", class_="listing-phone").text.strip().replace("Tel:", "")
            email= article.find("li", id="listing-email")
            lawyer_data["Email"]  = email.find("a").text.strip() if email else None
            rating_element = article.find("div", class_="stars-cont")
            lawyer_data["Rating"] = int(rating_element.find("div", class_="stars")["class"][1][-1]) if rating_element else None
            description = article.find("section", id="overview")
            lawyer_data["Description"] = description.find("p").text.strip() if description else None

            data_list.append(lawyer_data)

    else:
        print(f"Failed to retrieve page {page_number}. Status code: {response.status_code}")

with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=2)

print("Scraping completed. Data saved to lawyers.json.")