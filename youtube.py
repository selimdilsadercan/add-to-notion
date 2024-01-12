from googleapiclient.discovery import build
from utils import *
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api)


def get_video_infos(video_url:str):
    video_id:str = get_video_id(video_url)

    request = youtube.videos().list(
        part = "snippet, contentDetails",
        id = video_id,
    )

    response = request.execute()
   
    title = response["items"][0]["snippet"]["title"]

    durationRaw = response["items"][0]["contentDetails"]["duration"]
    duration = convert_to_int(durationRaw)

    channel_name = response["items"][0]["snippet"]["channelTitle"]
    channel_id = response["items"][0]["snippet"]["channelId"]
    channel_url = f"https://www.youtube.com/channel/{channel_id}"

    cover_img_url = get_thumbnail(video_url)

    return title, duration, channel_url, channel_name, cover_img_url



def get_video_duration(video_id):

    request = youtube.videos().list(
        part = "contentDetails",
        id = video_id,
    )

    response = request.execute()
    durationRaw = response["items"][0]["contentDetails"]["duration"]

    duration = convert_to_int(durationRaw)
    return duration



def get_playlist_infos(playlist_url:str):
    playlist_id = get_playlist_id(playlist_url)

    request = youtube.playlistItems().list(
        part = "snippet, contentDetails",
        playlistId = playlist_id[0],
    )
    response = request.execute()

    request2 = youtube.playlists().list(
        part = "snippet",
        id = playlist_id,
    )
    response2 = request2.execute()

    playlist_title = response2["items"][0]["snippet"]["title"]
    playlist_image = response2["items"][0]["snippet"]["thumbnails"]["high"]["url"]

    totalDuration = 0

    channel_name = response["items"][0]["snippet"]["videoOwnerChannelTitle"]

    channel_id = response["items"][0]["snippet"]["videoOwnerChannelId"]
    channel_url = f"https://www.youtube.com/channel/{channel_id}"

    return playlist_title, totalDuration, channel_url, channel_name, playlist_image

if __name__ == '__main__':
    print(get_playlist_infos("https://www.youtube.com/playlist?list=PLruhrmh5oDvx4gsN3DtTW9cIl82Y3HXdo"))
