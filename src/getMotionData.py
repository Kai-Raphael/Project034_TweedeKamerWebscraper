import requests
from bs4 import BeautifulSoup

base_url = "https://www.tweedekamer.nl"
moties_page_url = base_url + "/kamerstukken/moties"

def retrieve_hyperlinks_of_moties_page(target_moties_page):
    response = requests.get(target_moties_page.url)
    
    if response.status_code == 200:
        print(f"\u2705 Request successful: {response.status_code}")
        html_content = response.text
    else:
        print(f"\u274C Failed to retrieve the page. Status Code: {response.status_code}")
        return None, None

    # Parse the HTML content of the page
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the hyperlinks of the different moties
    motie_hyperlinks_resultset = soup.find_all('h4', class_='u-mt--collapse')

    # Retrieve each motion page link using list comprehension
    list_of_motie_links = [base_url + result.find('a')['href'] for result in motie_hyperlinks_resultset]

    # Retrieve the hyperlink of the next page
    next_page_hyperlink = moties_page_url + soup.find('li', class_='m-pager__item m-pager__item--next').find('a')['href']

    return list_of_motie_links, next_page_hyperlink

def get_motion_data(number_of_motion_pages):
    # Send an HTTP request to the website of the tweede kamer
    target_page = requests.get(moties_page_url)

    # retrieve all page links in a list
    all_page_links = []

    # Test the function for the specified number of pages
    for _ in range(number_of_motion_pages):
        # Retrieve the hyperlinks of the moties and of the next page of the current page
        motie_hyperlinks_resultset, next_page_hyperlink = retrieve_hyperlinks_of_moties_page(target_page)

        target_page = requests.get(next_page_hyperlink)

        all_page_links.append(motie_hyperlinks_resultset)

    return all_page_links