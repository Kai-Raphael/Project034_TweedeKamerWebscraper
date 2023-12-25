import requests
from bs4 import BeautifulSoup
from make_http_request import make_http_request

base_url = "https://www.tweedekamer.nl"
moties_page_url = base_url + "/kamerstukken/moties"

def get_motie_urls(number_of_motion_pages):
    # Define an empty list to hold all the page links
    all_page_links = []

    # Send an HTTP request to the website of the tweede kamer for the first moties page
    target_page = requests.get(moties_page_url)

    # Run for the specified amount of pages
    for _ in range(number_of_motion_pages):
        # Send an HTTP request to the moties page
        page_content = make_http_request(target_page.url)
        
        if page_content is not None:
            # Parse the HTML content of the page
            soup = BeautifulSoup(page_content, 'html.parser')

            # Find all the hyperlinks of the different moties
            motie_hyperlinks_resultset = soup.find_all('h4', class_='u-mt--collapse')

            # Retrieve each motion page link using list comprehension
            list_of_motie_links = [base_url + result.find('a')['href'] for result in motie_hyperlinks_resultset]

            # Retrieve the hyperlink of the next page
            next_page_hyperlink = moties_page_url + soup.find('li', class_='m-pager__item m-pager__item--next').find('a')['href']

            # Put all motie-links in a list
            all_page_links.append(list_of_motie_links)

            # Make the next page hyperlink the following target page
            target_page = requests.get(next_page_hyperlink)

    return all_page_links