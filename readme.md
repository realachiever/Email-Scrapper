# Email Scraper

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

The Email Scraper is a Python application that extracts email addresses from a website's search results. It utilizes web scraping techniques to parse the HTML content and extract the relevant information from the JSON data.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running the Email Scraper, make sure you have the following prerequisites installed:

- Python 3.x
- requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- pandas library (`pip install pandas`)

## Usage

1. Open the scrapper.py file in a text editor.
2. Modify the base_url and total_pages variables to match your desired website and the number of pages you want to scrape.
3. Run the script:
   ```shell
   python scrapper.py
4. The script will scrape the emails from each page and display them in the console.
5. The extracted emails will also be saved to an Excel file named emails.xlsx in the same directory.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please send me mail to am.dev.8080@gmail.com.
