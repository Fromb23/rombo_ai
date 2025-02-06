import requests
from bs4 import BeautifulSoup
import time
import json

# Define base URL
base_url = "https://stackoverflow.com/questions/tagged/python?tab=newest&page="

# Number of pages to scrape
max_pages = 50  # Adjust as needed

headers = {"User-Agent": "Mozilla/5.0"}
data = []  # List to store extracted data

for page in range(1, max_pages + 1):
    url = base_url + str(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    print(f"Scraping Page {page}...\n")

    questions = soup.find_all("div", class_="s-post-summary")

    for q in questions:
        title = q.find("a", class_="s-link").text.strip()
        link = "https://stackoverflow.com" + q.find("a", class_="s-link")["href"]
        votes = q.find("span", class_="s-post-summary--stats-item-number").text.strip()

        # Append to list
        data.append({"title": title, "votes": votes, "link": link})

    time.sleep(2)  # Delay to prevent being blocked

# Save data to JSON file
with open("scraped.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ Scraping complete! Data saved to scraped.json")
