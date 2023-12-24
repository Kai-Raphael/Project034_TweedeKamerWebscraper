import requests
from getMotionList import getMotionList
from bs4 import BeautifulSoup

# Function to scrape moties from the Tweede Kamer website
def get_motion_data():
    
    # set a max for the testing of the model (real pages contains over ~5.0000 results)
    Max_number_of_motion_pages  = 2

    # URL of the moties home page
    base_url = "https://www.tweedekamer.nl/kamerstukken/moties"

    # Send an HTTP request to the website of the tweede kamer
    response = requests.get(base_url)

    # retrieve all page links
    all_page_links = []

    target_page = response

    # Test the function for 2 pages
    for i in range(Max_number_of_motion_pages):

        motie_hyperlinks_resultset, next_page_hyperlink = retrieve_hyperlinks_of_moties_page(target_page)
        target_page = requests.get(next_page_hyperlink)
        all_page_links.append(motie_hyperlinks_resultset)

    print(f"RETRIEVED PAGE LINKS: \n {all_page_links}")
       
def retrieve_hyperlinks_of_moties_page(response):
        # Check if the request was successful (status code 200) (and if so continue)
        if response.status_code == 200:
            print(f"\u2705 request successful: {response.status_code}")

            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # URL of the moties home page
            base_url = "https://www.tweedekamer.nl/kamerstukken/moties"

            motie_hyperlink_count = 0
            # Find all the hyperlinks of the different moties
            motie_hyperlinks_resultset = soup.find_all('h4', class_='u-mt--collapse')

            for result in motie_hyperlinks_resultset:

                hyperlink = base_url + result.find('a')['href']
                print(f" {str(motie_hyperlink_count).zfill(3)} Motie Hyperlink: {hyperlink}" )
                motie_hyperlink_count += 1

            # Retrieve the hyperlink of the next page
            next_page_hyperlink = base_url + soup.find('li', class_='m-pager__item m-pager__item--next').find('a')['href']
            print(f"next page link: {next_page_hyperlink} \n")

            return motie_hyperlinks_resultset, next_page_hyperlink

            # Also creat an object of the motion itself (although this might not be necessary)
            #motie_objects = getMotionList(motie_cards)

        else:
            print(f"\u274C Failed to retrieve the page. Status Code: {response.status_code}")
 