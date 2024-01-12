from dotenv import load_dotenv
from utils import *
import requests
import os

load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
VIDEO_DATABASE= os.getenv('VIDEO_DATABASE')
CHANNEL_DATABASE = os.getenv('CHANNEL_DATABASE')

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_path_list():
    url = f"https://api.notion.com/v1/databases/{VIDEO_DATABASE}/query"

    payload = {"page_size": 9999000}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    # with open('db.json', "w", encoding='utf8') as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]

    return results


def find_database_id(index):
    url = f"https://api.notion.com/v1/databases/{VIDEO_DATABASE}/query"

    payload = {"page_size": 200}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    database_id = data["results"][index]["id"]

    return database_id


def find_database_id_video(index):
    url = f"https://api.notion.com/v1/databases/{VIDEO_DATABASE}/query"

    payload = {"page_size": 200}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    database_id = data["results"][index]["id"]

    return database_id


def get_kanal_list():
    url = f"https://api.notion.com/v1/databases/{VIDEO_DATABASE}/query"

    payload = {"page_size": 200}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()  

    # with open('db.json', "w", encoding='utf8') as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    
    urlList = []
    for result in results:
        try:
            resultUrl = result["properties"]["Youtube URL"]["url"]
            urlList.append(resultUrl)
        except: 
            pass

    return urlList


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
    

def create_kanal(properties, icon_url):
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


