from make_soup import make_http_request, make_soup
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from get_kamerlid_url import get_kamerleden_url_list
import random

def test_create_kamerlid_profile_function():
    # take (5 samples of) the link(list)
    random_hyperlink_selection = random.sample(get_kamerleden_url_list, 5)

    for hyperlink_to_lid_profile in random_hyperlink_selection:
        print(f'Hyperlink: {selected_hyperlinks}')
        create_kamerlid_profile(hyperlink_to_lid_profile)
    
def miriam_bikker_test():
    create_kamerlid_profile(get_kamerleden_url_list()[9])

def create_kamerlid_profile(personal_hyperlink):

    # First, make the soup
    soup = make_soup(make_http_request(personal_hyperlink))

    # Secondly, retrieve every piece of usefull info
    get_socials(soup)



    #print(f'profile made')


def get_socials(soup):

    # Extract the social elements
    result_set = soup.find_all('a', class_='m-list-social__link')
    
    # Extract href attributes from each element in the result set
    links = [element['href'] for element in result_set]

    for link in links:
        print(f'Link: {link}')


    #return socials



miriam_bikker_test()
#test_create_kamerlid_profile_function()