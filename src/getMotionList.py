class Motion:
    def __init__(self, title, link):
        self.title = title
        self.link = link

def getMotionList(motie_cards):
    motie_objects = []

    for card_information in motie_cards:
        motie_title = card_information.text.strip()
        print (card_information)
        #motie_link = card_information['href'].split("moties/", 1)[1].strip()
        #motie_link = "https://www.tweedekamer.nl/kamerstukken/moties/" + motie_link

        # Create a Motion object
        motion_object = Motion(title=motie_title, link=motie_link)

        # Print the information (optional)
        print(f"Titel: {motion_object.title} \n Link: {motion_object.link}\n{'=' * 30}\n")

        # Append the Motion object to the list
        motie_objects.append(motion_object)

    return motie_objects
