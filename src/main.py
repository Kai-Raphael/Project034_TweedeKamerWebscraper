from get_motie_url import get_motie_urls
from get_motie_content import get_motie_page_content,get_motie_document_content

# set a max for the testing of the model (real pages contains over ~5.0000 results)
NUMBER_OF_PAGES_TO_GO_THROUGH = 2


#going from a machine learning perspective (C.R.I.S.P model)
def main():
    #Select Data
    List_of_Lists_of_page_links = get_motie_urls(NUMBER_OF_PAGES_TO_GO_THROUGH)
    
    # Use list comprehension to create a link-list 
    links = [link for page_link_list in List_of_Lists_of_page_links for link in page_link_list]

    # FYI: print each link
    #for each_link in links:
        #print(f"\U0001F517 Link: {each_link}")

    # FYI: print the # of results 
    print(f"\U0001F50D Found {len(links)} Links on {NUMBER_OF_PAGES_TO_GO_THROUGH} pages: \n")
    
    #Now retrieve the motie page details
    print(f"\U0001F50D Search link: {links[4]}" )
    get_motie_page_content(links[4])

    #Then retrieve the motie document
    # https://www.tweedekamer.nl/downloads/document?id=2023D51182

    #Clean data

    #Construct Data

    #Integrate Data

    #Model Data

if __name__ == "__main__":
    main()