from make_http_request import make_http_request
from bs4 import BeautifulSoup

KAMERLEDEN_PAGE_URL = 'https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden'

def get_kamerleden():
    kamerleden_page_content = make_http_request(KAMERLEDEN_PAGE_URL)

    if kamerleden_page_content is not None:
        # Parse the HTML content of the page
        soup = BeautifulSoup(kamerleden_page_content, 'html.parser')
        print(f'\U0001F372 Soup made')

    kamerleden_list = []

     # Find all the hyperlinks of the different moties
    kamerleden_links = soup.find_all('div', class_='u-display--flex u-flex-direction--column')


    # Retrieve each motion page link using list comprehension
    #kamerleden_list = [KAMERLEDEN_PAGE_URL + result.find('a')['href'] for result in kamerleden_cards_resultset]

    print(f'Resultset: \n {kamerleden_cards_resultset}')
#test run
get_kamerleden()