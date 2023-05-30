import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# Base URL for the search results
base_url = "https://www.11880.com/suche/Handwerk/deutschland?page="

# Number of pages to scrape
total_pages = 3

# List to store all the extracted emails
emails = []

# Loop through each page
for page in range(1, total_pages + 1):
    # Construct the URL for the current page
    url = base_url + str(page)
    
    # Make a request to the page and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the script tags containing the JSON data
    script_tags = soup.find_all('script', attrs={'type': 'application/ld+json', 'data-cookieconsent': 'ignore'})

    # Extract the emails from the JSON data
    for script_tag in script_tags:
        json_data = json.loads(script_tag.string)
        itemList = json_data['mainEntity']['itemListElement']
        for item in itemList:
            email = item['item'].get('email')
            if email:
                emails.append(email)

# Create a pandas DataFrame from the emails list
df = pd.DataFrame({'Email': emails})

# Export the DataFrame to an Excel file
df.to_excel('emails.xlsx', index=False)
