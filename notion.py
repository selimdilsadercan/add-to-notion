from dotenv import load_dotenv
from utils import *
import requests
import os

load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
VIDEO_DATABASE= os.getenv('VIDEO_DATABASE')
CHANNEL_DATABASE = os.getenv('CHANNEL_DATABASE')
WEBSITE_DATABASE = os.getenv('WEBSITE_DATABASE')
VSCODE_ADDON_DATABASE = os.getenv('VSCODE_ADDON_DATABASE')
CHROME_ADDON_DATABASE = os.getenv('CHROME_ADDON_DATABASE')
REPO_DATABASE = os.getenv('REPO_DATABASE')
NPM_DATABASE = os.getenv('NPM_DATABASE')

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


# VIDEOS

def get_video(videoId):
    url = f"https://api.notion.com/v1/databases/{VIDEO_DATABASE}/query"

    payload = {"page_size": 1, "filter": {"property": "Link", "url": {"contains": videoId}}}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    videoeNotionId = data["results"][0]["id"]

    return videoeNotionId


def create_video(properties, cover_url, icon_url):
    cover =  {
        "type": "external", 
        "external": {
            "url": cover_url
        }
    }

    icon =  {
        "type": "external", 
        "external": {
            "url": icon_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": VIDEO_DATABASE}, "properties": properties, "cover": cover, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)
    return res, res.json()["id"]
    

# CHANNELS

def get_kanal(link):
    url = f"https://api.notion.com/v1/databases/{CHANNEL_DATABASE}/query"

    payload = {"page_size": 1, "filter": {"property": "URL", "url": {"contains": link}}}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return data["results"][0]["id"]


def create_channel(properties, icon_url):
    icon =  {
        "type": "external", 
        "external": {
            "url": icon_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": CHANNEL_DATABASE}, "properties": properties, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)
    return res, res.json()["id"]



# WEBSITES

def get_website(link):
    url = f"https://api.notion.com/v1/databases/{WEBSITE_DATABASE}/query"

    payload = {"page_size": 1, "filter": {"property": "Web", "url": {"contains": link}}}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return data["results"][0]["id"]

def create_website(properties, icon_url):
    icon =  {
        "type": "external", 
        "external": {
            "url": icon_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": WEBSITE_DATABASE}, "properties": properties, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)
    return res, res.json()["id"]


## VSCODE EKLENTİLERİ

def get_vscode_eklenti(link):
    url = f"https://api.notion.com/v1/databases/{VSCODE_ADDON_DATABASE}/query"

    payload = {"page_size": 1, "filter": {"property": "Link", "url": {"contains": link}}}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return data["results"][0]["id"]

def create_vscode_eklenti(properties, icon_url):
    icon =  {
        "type": "external", 
        "external": {
            "url": icon_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": VSCODE_ADDON_DATABASE}, "properties": properties, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)
    return res, res.json()["id"]


## CHROME EKLENTİLERİ

def get_chrome_eklenti(link):
    url = f"https://api.notion.com/v1/databases/{CHROME_ADDON_DATABASE}/query"

    payload = {"page_size": 1, "filter": {"property": "Link", "url": {"contains": link}}}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return data["results"][0]["id"]


def create_chrome_eklenti(properties, icon_url):
    icon =  {
        "type": "external", 
        "external": {
            "url": icon_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": CHROME_ADDON_DATABASE}, "properties": properties, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)
    return res, res.json()["id"]


# REPOS

def get_repo(link):
    url = f"https://api.notion.com/v1/databases/{REPO_DATABASE}/query"

    payload = {"page_size": 1, "filter": {"property": "Link", "url": {"contains": link}}}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return data["results"][0]["id"]

def create_repo(properties):
    icon =  {
        "type": "external", 
        "external": {
            "url": "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": REPO_DATABASE}, "properties": properties, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)
    return res, res.json()["id"]


# NPM PACKAGES

def get_npm_package(link):
    url = f"https://api.notion.com/v1/databases/{NPM_DATABASE}/query"

    payload = {"page_size": 1, "filter": {"property": "Npm Url", "url": {"contains": link}}}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return data["results"][0]["id"]

def create_npm_package(properties, icon_url):
    icon =  {
        "type": "external", 
        "external": {
            "url": icon_url
        }
    }

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": NPM_DATABASE}, "properties": properties, "icon": icon}

    res = requests.post(create_url, headers=headers, json=payload)

    return res, res.json()["id"]



if __name__ == "__main__":
    print(create_npm_package(
        {'İsim': {'title': [{'text': {'content': '@editorjs/editorjs'}}]}, 'Npm Url': {'url': 'https://www.npmjs.com/package/@editorjs/editorjs'}, 'assets': {'rich_text': [{'text': {'content': 'https://editorjs.io/og-image.png - https://editorjs.io/favicon.png'}}]}, 'selim': {'checkbox': True}},
        "https://editorjs.io/og-image.png"
    ))