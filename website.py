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
            raise Exception("Title tag not found")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return url.split(".")[0].split("://")[1].title() if "www." not in url else url.split(".")[1]


def get_eklenti_infos(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('span', class_="ux-item-name").text
    imageUrl = soup.find('img', class_="image-display")["src"]

    return title, imageUrl


def get_repo_infos(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    title = url.split("github.com/")[1]  
    about_h2 = soup.find("h2", string="About")
    description = about_h2.find_next_sibling("p").text.strip()

    return title, description