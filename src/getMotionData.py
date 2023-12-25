import requests
from bs4 import BeautifulSoup

base_url = "https://www.tweedekamer.nl/kamerstukken/moties"

# send a request to a target url
def send_request(target_url):
    
    # Store the response in a variable
    response = requests.get(target_url)

    # If that response is good (200) return the text
    if response.status_code == 200:
        print(f"\u2705 Request successful: {response.status_code}")
        return response.text, response
    else:
        print(f"\u274C Failed to retrieve the page. Status Code: {response.status_code}")
        return None, response


# Function to scrape moties from the Tweede Kamer website
def get_motion_data(number_of_motion_pages):
    
    # URL of the moties home page
    base_url = "https://www.tweedekamer.nl/kamerstukken/moties"

    # Send an HTTP request to the website of the tweede kamer
    target_page = requests.get(base_url)

    # retrieve all page links in a list
    all_page_links = []

    # Test the function for 2 pages
    for i in range(number_of_motion_pages):

        #retrieve the hyperlinks of the moties and of the next page of the current page
        motie_hyperlinks_resultset, next_page_hyperlink = retrieve_hyperlinks_of_moties_page(target_page)

        target_page = requests.get(next_page_hyperlink)

        all_page_links.append(motie_hyperlinks_resultset)
    
    return all_page_links
       
def retrieve_hyperlinks_of_moties_page(target_moties_page):
    html_content, response = send_request(target_moties_page.url)

    print(f"Response: {response.url}")

    if html_content:
        # Parse the HTML content of the page
        soup = BeautifulSoup(html_content, 'html.parser')

        # URL of the moties home page
        base_url = "https://www.tweedekamer.nl"

        # Find all the hyperlinks of the different moties
        motie_hyperlinks_resultset = soup.find_all('h4', class_='u-mt--collapse')

        list_of_motie_links = []

        # Retrieve each motion page link
        motie_hyperlink_count = 0

        for result in motie_hyperlinks_resultset:
            hyperlink = base_url + result.find('a')['href']
            list_of_motie_links.append(hyperlink)
            print(f"{str(motie_hyperlink_count).zfill(3)} Motie Hyperlink: {hyperlink}")
            motie_hyperlink_count += 1
            


        # Retrieve the hyperlink of the next page
        next_page_hyperlink = base_url + "/kamerstukken/moties" + soup.find('li', class_='m-pager__item m-pager__item--next').find('a')['href']
        print(f"next page link: {next_page_hyperlink}\n")

        return list_of_motie_links, next_page_hyperlink

    else:
        # Handle the case where the request failed
        return None, None