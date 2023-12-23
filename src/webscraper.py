import requests
from getMotionList import getMotionList
from bs4 import BeautifulSoup

# Function to scrape moties from the Tweede Kamer website
def get_motion_data():
    # URL of the moties page
    tweede_kamer_moties_home_page = "https://www.tweedekamer.nl/kamerstukken/moties"

    # Send an HTTP request to the website
    response = requests.get(tweede_kamer_moties_home_page)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"request successful: {response.status_code}")

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # get all the cards (div elements) from the first gitpage
        motie_cards = soup.find_all('div', class_='u-mt--large u-break-inside--avoid-at-print m-card m-card--auto-height')
        next_page_link = tweede_kamer_moties_home_page + soup.find('li', class_='m-pager__item m-pager__item--next').find('a')['href']
        
        motie_objects = getMotionList(motie_cards)

        print(f"Motie Elements: {motie_cards}")
        print(f"next page link: {next_page_link}")

    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")




#<li class="m-pager__item m-pager__item--next">
#          <a href="?cfg=tksearch&amp;fld_prl_kamerstuk=Moties&amp;fld_prl_soort=Motie%20%28gewijzigd/nader%29&amp;fld_tk_categorie=Kamerstukken&amp;qry=%2A&amp;srt=date%3Adesc%3Adate&amp;sta=1&amp;page=1" rel="next">
#            Volgende pagina
#          </a>
#        </li>

