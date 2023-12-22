import requests
from bs4 import BeautifulSoup

# Function to scrape moties from the Tweede Kamer website
def scrape_moties():
    # URL of the moties page
    url = "https://www.tweedekamer.nl/kamerstukken/moties"

    # Send an HTTP request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        print(f"request succesfull: {response.status_code}")

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'a' tags with class 'h-link-inverse'
        motie_elements = soup.find_all('a', class_='h-link-inverse')
        print(motie_elements)

        # Retrieve and print the href attribute for each link
        for element in motie_elements:
            motie_titel = element.text.strip()
            motie_link = element['href']
            print(f"Titel: {motie_titel} \n Link: {motie_link}\n{'=' * 30}\n")
            
    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")
