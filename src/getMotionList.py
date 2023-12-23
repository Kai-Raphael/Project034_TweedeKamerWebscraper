def getMotionList(motie_cards): # Geef motie_cards een type.
     
     #create an empty list
     motie_links =[]

    # loop through the motion cards adding the links to the list
     for element in motie_cards:
            motie = element.text.strip()
            motie_link = element['href'].split("moties/",1) # Maak element even een duidelijke naam.
            
            # Over het algemen wil je nooit strings splitten. 
            # Als je dit wel moet doen dan heb je vaak een andere fout gemaakt.
            
            # Process eerst de motie_card in een object 
            #om er vervolgens met een 'getter' de data(wat je wilt hebben) uit te halen . 
            #Nu doe je twee dingen tegelijkertijd in dezelfde functie.
            motie_link = "https://www.tweedekamer.nl/kamerstukken/moties/" + motie_link[1].strip()


            # Print the information (optional)
            print(f"Titel: {motie} \n Link: {motie_link}\n{'=' * 30}\n")

            # Append the motie_link to the list
            motie_links.append(motie_link)
            

            return motie_links
     
     