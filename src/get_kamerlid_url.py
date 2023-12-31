from make_soup import make_http_request, make_soup
from bs4 import BeautifulSoup
from urllib.parse import urljoin

KAMERLEDEN_PAGE_URL = 'https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden'

def get_kamerleden_url_list():
    
    soup = make_soup(make_http_request(KAMERLEDEN_PAGE_URL))

    kamerleden_url_list = []

     # Find all the hyperlinks of the different moties
    kamerleden_cards = soup.find_all('div', class_='u-display--flex u-flex-direction--column')
    aantal_leden_cards = len(kamerleden_cards)

    if aantal_leden_cards < 150:
        print(f'\U000F2757  Not everybody is there!')
   
    #print(f'{kamerleden_links}')
    for element in kamerleden_cards:
        lid_naam = element.find('a',class_='u-text-size--large u-text-weight--bold u-text-color--primary u-text-decoration--none u-text-line-height--tiny')
        lid_partij = element.find('span',class_="u-text-size--small u-text-color--primary").get_text(strip=True)
        lid_link = lid_naam['href']
        full_lid_link = urljoin(KAMERLEDEN_PAGE_URL,lid_link)

        #print(f'{30 * "-"}')
        #print(f'\U0001F393 lid:     {lid_naam.get_text(strip=True)}')
        #print(f'\U0001F389 partij:  {lid_partij}')
        #print(f'\U0001F517 link:    {full_lid_link}')
        
        kamerleden_url_list.append(full_lid_link)

    #print(f'{kamerleden_url_list}')

    return kamerleden_url_list