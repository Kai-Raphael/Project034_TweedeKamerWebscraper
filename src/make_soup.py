import requests
from bs4 import BeautifulSoup

def make_http_request(target_page):

    # Make the request
    response = requests.get(target_page)

    # If the request is succesfull, return the page content 
    if response.status_code == 200:
        print(f"\u2705 Request successful: {response.status_code}")
        html_content = response.text
        return html_content
    else:
        print(f"\u274C Failed to retrieve the page. Status Code: {response.status_code}")
        return None

def make_soup(html_content):
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')
    print(f'\U0001F372 Soup made')
    return soup