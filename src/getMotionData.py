import requests
from getMotionList import getMotionList
from bs4 import BeautifulSoup

# Function to scrape moties from the Tweede Kamer website
def get_motion_data(base_url):

    # Send an HTTP request to the website of the tweede kamer
    response = requests.get(base_url)

    # set a max for the testing of the model (real pages contains over ~5.0000 results)
    Max_number_of_motion_pages  = 2

    # retrieve all page links
    all_page_links = []

    # Loop through the last 
    for i in range(Max_number_of_motion_pages):

        # Check if the request was successful (status code 200) (and if so continue)
        if response.status_code == 200:
            print(f"request successful: {response.status_code}")

            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # get all the cards (div elements) from the first gitpage
            motie_cards = soup.find_all('div', class_='u-mt--large u-break-inside--avoid-at-print m-card m-card--auto-height')
            
            # Retrieve the hyperlink of the next page
            next_page_link = base_url + soup.find('li', class_='m-pager__item m-pager__item--next').find('a')['href']

            #append it to the page_links list
            all_page_links.append(next_page_link)

            # Also creat an object of the motion itsel (although this might not be necessary)
            motie_objects = getMotionList(motie_cards)

            # Print the cards and print the last link
            print(f"Motie Elements: {motie_cards}")
            print(f"next page link: {next_page_link}")

        else:
            print(f"Failed to retrieve the page. Status Code: {response.status_code}")
    
    return all_page_links

for link in all_page_links:
    print(link)