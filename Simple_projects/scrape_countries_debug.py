import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage to scrape
url = "https://worldpopulationreview.com/country-rankings/list-of-countries-by-continent"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("GET request successful")
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Initialize an empty list to store the data
    continents_data = []

    # Find the table element with the specific class
    table = soup.findAll('table', class_='tp-table-body is-narrow w-full min-w-full table-auto border-separate border-spacing-0 border bg-white')
    table = table[-1]
    print(table)

    # Check if the table is found
    if table:
        # Extract rows from the table
        rows = table.find('tbody').find_all('tr')

        for row in rows:
            # Extract the country name from the anchor tag in the th element
            th = row.find('th')
            print(th)
            if th:
                country = th.find('a').get_text().strip()
            else:
                continue
            
            # Extract the continent name from the span tag in the td element
            td = row.find_all('td')[0]  # The first td element contains the continent
            if td:
                span = td.find('span')
                if span:
                    continent = span.get_text().strip()
                else:
                    continue
            else:
                continue

            # Find or create the continent entry
            continent_entry = next((entry for entry in continents_data if entry["continent"] == continent), None)
            if not continent_entry:
                continent_entry = {"continent": continent, "countries": []}
                continents_data.append(continent_entry)

            # Add the country to the continent entry
            continent_entry["countries"].append(country)

        # Write the data to a JSON file
        with open("countries_by_continent.json", "w") as json_file:
            json.dump(continents_data, json_file, indent=4)

        print("Data has been scraped and saved to countries_by_continent.json")
    else:
        print("Table not found. Please check the class name and structure.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)