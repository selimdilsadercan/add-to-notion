import isodate
import math
from urllib.parse import urlparse, parse_qs

def get_video_id(video_url):
    parsed_url = urlparse(video_url)
    
    if parsed_url.netloc == "www.youtube.com" and parsed_url.path == "/watch":
        query_parameters = parse_qs(parsed_url.query)
        video_id = query_parameters.get("v", None)
        return video_id[0] if video_id else None
    
    elif parsed_url.netloc == "youtu.be":
        video_id = parsed_url.path.strip('/')
        return video_id
    
    return None


def convert_to_int(duraion_ptype: str):
    duration = isodate.parse_duration(duraion_ptype)
    minutes = math.floor(duration.total_seconds() / 60)
    return minutes



def get_playlist_id(video_url):
    parsed_url = urlparse(video_url)
    query_parameters = parse_qs(parsed_url.query)
    playlist_id = query_parameters.get("list", None)
    return playlist_id



def get_thumbnail(url: str):
    video_id = get_video_id(url)

    img_url = f"https://i3.ytimg.com/vi/{video_id}/hqdefault.jpg"
    return img_url



def get_dataabase_id(url: str):
    database_id = url.split(".so/")[1]
    database_id = database_id.split("?v")[0]
    return database_id



def get_channel_url(channel_id):
    channel_url = f"https://www.youtube.com/{channel_id}"
    return channel_url

