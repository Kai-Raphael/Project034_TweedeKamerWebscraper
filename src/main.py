from getMotionData import get_motion_data

# set a max for the testing of the model (real pages contains over ~5.0000 results)
NUMBER_OF_PAGES_TO_GO_THROUGH = 2


#going from a machine learning perspective (C.R.I.S.P model)
def main():
    #Select Data
    List_of_Lists_of_page_links = get_motion_data(NUMBER_OF_PAGES_TO_GO_THROUGH)
    
    # Use list comprehension to create a link-list 
    links = [link for page_link_list in List_of_Lists_of_page_links for link in page_link_list]

    for each_link in links:
        # FYI
        print(f"\U0001F50D Link: {each_link}")

    # FYI: print the # of results 
    print(f"\U0001F517 Found {len(links)} Links on {NUMBER_OF_PAGES_TO_GO_THROUGH} pages: \n")

    #Clean data

    #Construct Data

    #Integrate Data

    #Model Data

if __name__ == "__main__":
    main()