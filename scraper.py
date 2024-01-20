from bs4 import BeautifulSoup
import requests
from utils import *

def get_channel_infos(channel_url):
    request = requests.get(channel_url).text
    soup = BeautifulSoup(request, "lxml")

    img= soup.body.find("link", rel="image_src")["href"]
    url = soup.body.find("link", rel="canonical")["href"]
    name = soup.body.find("meta", itemprop="name")["content"]
    return img, url, name

if __name__ == "__main__":
    print(get_channel_infos("https://www.youtube.com/@kriss_drummer"))
