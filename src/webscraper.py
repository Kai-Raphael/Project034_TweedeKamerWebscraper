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

        motie_links = []  # Create an empty list to store motie links

        for element in motie_elements:
            motie = element.text.strip()
            motie_link = element['href'].split("moties/",1)
            motie_link = "https://www.tweedekamer.nl/kamerstukken/moties/" + motie_link[1].strip()


            # Print the information (optional)
            print(f"Titel: {motie} \n Link: {motie_link}\n{'=' * 30}\n")

            # Append the motie_link to the list
            motie_links.append(motie_link)

        # Print the list of motie_links
        print("List of Motie Links:")
        for link in motie_links:
            print(link)

    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")
