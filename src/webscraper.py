import requests
from getMotionList import getMotionList
from bs4 import BeautifulSoup

# Function to scrape moties from the Tweede Kamer website
def scrape_moties():
    # URL of the moties page
    url = "https://www.tweedekamer.nl/kamerstukken/moties"

    # Send an HTTP request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"request successful: {response.status_code}")

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'a' tags with class 'h-link-inverse'
        motie_elements = soup.find_all('div', class_='u-mt--large u-break-inside--avoid-at-print m-card m-card--auto-height')
        print(f"Motie Elements: {motie_elements}")

        motie_objects = getMotionList(motie_elements)

    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")