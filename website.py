import favicon
import requests
from bs4 import BeautifulSoup

def get_favicon(url):
    icons = favicon.get(url)
    icon = icons[0]
    urls = [icon.url for icon in icons]
    allFavicons = ' - '.join(urls)
    return icon.url, allFavicons


def get_website_name(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('title')

        if title_tag:
            return title_tag.text.strip()
        else:
            return url.split(".")[1]

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return url.split(".")[1]
