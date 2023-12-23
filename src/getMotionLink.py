from bs4 import BeautifulSoup

class PageLinkExtractor:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def find_next_page_link(self, class_name):
        next_page_links = self.soup.find_all('li', class_=class_name)

        # Extract the href attribute from the 'a' tag
        for link in next_page_links:
            href = link.find('a')['href']
            return href  # Assuming there is only one link, you can modify as needed

# Example usage
html = """
<li class="m-pager__item m-pager__item--next">
  <a href="?qry=%2A&amp;fld_tk_categorie=Kamerstukken&amp;fld_prl_kamerstuk=Moties&amp;srt=date%3Adesc%3Adate&amp;page=1" rel="next">
    Volgende pagina
  </a>
</li>
"""

# Creating an instance of the PageLinkExtractor class
page_link_extractor = PageLinkExtractor(html)

# Finding the next page link using the class name
class_name = 'm-pager__item m-pager__item--next'
next_page_link = page_link_extractor.find_next_page_link(class_name)

# Print the result
print("Next page link:", next_page_link)
