import requests

def make_http_request(target_page):

    # Make the request
    response = requests.get(target_page)

    # If the request is succesfull, return the page content 
    if response.status_code == 200:
        print(f"\u2705 Request successful: {response.status_code}")
        html_content = response.text
        return html_content
    else:
        print(f"\u274C Failed to retrieve the page. Status Code: {response.status_code}")
        return None
