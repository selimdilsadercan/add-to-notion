from notion import *
from youtube import *
from utils import *
from scraper import *
from pyperclip import waitForNewPaste
import webbrowser


print("Bir URL kopyala (yeni olması lazım)")
url = waitForNewPaste()


if "youtube" in url or "youtu.be" in url:
    video_id = url.split("?list=")[1] if "playlist?list=" in url else get_video_id(url)
    url = url if "playlist?list=" in url else f"https://youtu.be/{video_id}"
    print(url)

    title, duration, channel_url, channel_name, image = get_playlist_infos(url) if  "playlist?list=" in url else get_video_infos(url)
    channel_img_url = get_channel_infos(channel_url)


    urlList = get_kanal_list()
    try:
        index = urlList.index(channel_url)
        created_database_id = find_database_id(index)

    except:
        kanal_data = {
            "İsim": {"title": [{"text": {"content": channel_name}}]},
            "Youtube URL": {"url": channel_url},
        }

        status, created_database_id = create_kanal(kanal_data, channel_img_url)
        print(status)


    created_data_id = ""
    try:
        created_data_id = get_video(video_id);

    except:
        data = {
            "Name": {"title": [{"text": {"content": title}}]},
            "Link": {"url": url},
            "Dakika": {"number": duration},
            "Kanal": {"relation": [{"id": created_database_id}]},
            "youtubeId": {"rich_text": [{"text": {"content": video_id}}]},
        }

        icon_url = "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"
        res, created_data_id = create_video(data, image, icon_url)
        print(res)

    created_data_id = created_data_id.replace("-", "")
    webbrowser.open(f"https://www.notion.so/selimdilsadercn/Youtube-Videolar-aded04bff7814ef6ad418f8873cbcad2?p={created_data_id}&pm=c")

else:
    print("Yanlış URL")
