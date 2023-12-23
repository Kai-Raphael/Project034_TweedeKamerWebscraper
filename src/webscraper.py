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

        # get all the cards (div elements) from the first page
        motie_cards = soup.find_all('div', class_='u-mt--large u-break-inside--avoid-at-print m-card m-card--auto-height')
        next_page_link = soup.find_all('li', class_='m-pager__item m-pager__item--next')
        
        print(f"Motie Elements: {motie_cards}")
        print("next page link: {next_page_link}")

        motie_objects = getMotionList(motie_cards)

    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")




#<li class="m-pager__item m-pager__item--next">
#          <a href="?cfg=tksearch&amp;fld_prl_kamerstuk=Moties&amp;fld_prl_soort=Motie%20%28gewijzigd/nader%29&amp;fld_tk_categorie=Kamerstukken&amp;qry=%2A&amp;srt=date%3Adesc%3Adate&amp;sta=1&amp;page=1" rel="next">
#            Volgende pagina
#          </a>
#        </li>

