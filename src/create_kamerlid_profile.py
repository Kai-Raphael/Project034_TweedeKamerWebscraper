from make_soup import make_http_request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from create_kamerleden_dictionary import get_kamerleden_links
import random

def test_create_kamerlid_profile_function():
    # take (5 samples of) the link(list)
    selected_hyperlinks = get_kamerleden_links()[9]
    # random_selection = random.sample(get_kamerleden_links, 5)

    print(f'Hyperlink: {selected_hyperlinks}')

    for hyperlink_to_lid_profile in selected_hyperlinks[1]:
        create_kamerlid_profile(hyperlink_to_lid_profile)

def create_kamerlid_profile(personal_hyperlink):
    print(f'Hyperlink: {personal_hyperlink}')
    print(f'profile made')


test_create_kamerlid_profile_function()