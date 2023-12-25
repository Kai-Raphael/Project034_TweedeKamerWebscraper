import requests
from bs4 import BeautifulSoup
from get_motie_url import make_http_request

def get_motie_page_content(motie_page_link):
    
    motie_fullpage_content = make_http_request(motie_page_link)

    if motie_fullpage_content is not None:
            # Parse the HTML content of the page
            soup = BeautifulSoup(motie_fullpage_content, 'html.parser')

    motie_title = soup.find('h1').get_text(strip=True)

    print(f'\U0001F4DC {motie_title}')
    
    #motie_indiener

    #motie_medeindiener
#
    #motie_stemmingsuitslag
#
    #motie_fractie_naam
#
    #motie_fractie_zetels
#
    #motie_fractie_stem
#
    #motie_fractie_deelname
#
    #motie_document_link
#

    return 

def get_motie_document_content(motie_document_link):
    
    motie_document_content = make_http_request(motie_document_link)

    return 