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
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the elements containing moties information
        moties_elements = soup.find_all('div', class_='moties')
        
        # Extract and print moties details
        for motie in moties_elements:
            title = motie.find('h3').text.strip()
            details = motie.find('p').text.strip()

            print(f"Title: {title}\nDetails: {details}\n{'=' * 30}\n")
    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")

# Run the scraper function
scrape_moties()

If __name__ == "__main__":
    Call main