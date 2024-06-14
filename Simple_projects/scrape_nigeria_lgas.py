import requests
from bs4 import BeautifulSoup
import json

# URL of the page to scrape
url = "https://www.legit.ng/1163676-number-local-governments-state-nigeria.html"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Get request successful")
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Initialize an empty list to store the data
    states_data = []

    # Find all the state names in h3 tags
    state_headers = soup.find_all('h3')

    for state_header in state_headers:
        state_name = state_header.get_text().strip()
        
        # Find the next sibling ul element which contains the LGAs
        lga_list = []
        next_element = state_header.find_next_sibling('ul')
        
        if next_element:
            # Extract all li elements in the ul
            lgas = next_element.find_all('li')
            for lga in lgas:
                lga_list.append(lga.get_text().strip())
        
        # Append the state and its LGAs to the list
        states_data.append({
            "state": state_name,
            "LGA": lga_list
        })
    
    # Write the data to a JSON file
    with open("nigeria_states_lgas_legit.json", "w") as json_file:
        json.dump(states_data, json_file, indent=4)
    
    print("Data has been scraped and saved to nigeria_states_lgas_legit.json")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")