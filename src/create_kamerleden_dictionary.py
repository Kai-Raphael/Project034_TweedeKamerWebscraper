from make_http_request import make_http_request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
    # kamerleden_list = [KAMERLEDEN_PAGE_URL + result.find('a')['href'] for result in kamerleden_cards_resultset]

    #print(f'{kamerleden_links}')
    for element in kamerleden_links:
        lid_naam = element.find('a',class_='u-text-size--large u-text-weight--bold u-text-color--primary u-text-decoration--none u-text-line-height--tiny')
        lid_partij = element.find('span',class_="u-text-size--small u-text-color--primary").get_text(strip=True)
        lid_link = lid_naam['href']
        full_lid_link = urljoin(KAMERLEDEN_PAGE_URL,lid_link)

        print(f'{30 * "-"}')
        print(f'\U0001F393 lid:     {lid_naam.get_text(strip=True)}')
        print(f'\U0001F389 partij:  {lid_partij}')
        print(f'\U0001F517 link:    {full_lid_link}')
        
#test run
get_kamerleden()