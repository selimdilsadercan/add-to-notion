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


def get_website_from_npm(url):
    request1 = requests.get(url).text
    soup1 = BeautifulSoup(request1, "lxml")

    github_url = "https://" + soup1.body.find("span", id="repository-link").text

    request2 = requests.get(github_url).text
    soup2 = BeautifulSoup(request2, "lxml")

    website_url = soup2.body.find("h2", text="About").find_next("a", {"class": "text-bold"})["href"]
    return website_url


if __name__ == "__main__":
    print(get_website_from_npm("https://www.npmjs.com/package/@editorjs/editorjs"))
