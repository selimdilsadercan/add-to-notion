from notion import *
from youtube import *
from utils import *
from scraper import *
from website import *
from gpt import *
from pyperclip import waitForNewPaste
import webbrowser

load_dotenv()
selim = True if os.getenv('AUTHOR') == "selim" else False

print("Bir URL kopyala (yeni olması lazım)")
url = waitForNewPaste()


if "youtube" in url or "youtu.be" in url:
    print("işlem: youtube")
    if "playlist?list" in  url:
        video_id = url.split("?list=")[1]
        url = url
        print(url)
        title, duration, channel_url, channel_name, image = get_playlist_infos(url)
        channel_img_url, _, _ = get_channel_infos(channel_url)


    elif "youtu.be" in url or "watch?v=" in url:
        video_id = get_video_id(url)
        url = f"https://youtu.be/{video_id}"
        print(url)
        title, duration, channel_url, channel_name, image = get_video_infos(url)
        channel_img_url, _, _ = get_channel_infos(channel_url)
    
    else:
        channel_img_url, channel_url, channel_name = get_channel_infos(url)

    created_channel_id = ""
    try:
        created_channel_id = get_kanal(channel_url);

    except:
        kanal_data = {
            "İsim": {"title": [{"text": {"content": channel_name}}]},
            "URL": {"url": channel_url},
            "selim": {"checkbox": selim},
        }

        res1, created_channel_id = create_channel(kanal_data, channel_img_url)
        print(res1)


    if  "playlist?list" in url or "youtu.be" in url or "watch?v=" in url:
        created_data_id = ""
        try:
            created_data_id = get_video(video_id);

        except:
            data = {
                "Name": {"title": [{"text": {"content": title}}]},
                "Link": {"url": url},
                "Dakika": {"number": duration},
                "Kanal": {"relation": [{"id": created_channel_id}]},
                "youtubeId": {"rich_text": [{"text": {"content": video_id}}]},
                "selim": {"checkbox": selim},
            }

            icon_url = "https://cdn-icons-png.flaticon.com/512/1384/1384060.png"
            res, created_data_id = create_video(data, image, icon_url)
            print(res)

        created_data_id = created_data_id.replace("-", "")
        webbrowser.open(f"https://www.notion.so/selimdilsadercn/Youtube-Videolar-aded04bff7814ef6ad418f8873cbcad2?p={created_data_id}&pm=c")

    else: 
        created_channel_id = created_channel_id.replace("-", "")
        webbrowser.open(f"https://www.notion.so/selimdilsadercn/Kanallar-4ce985c43cf149a285a417307baf4f3f?p={created_channel_id}&pm=c")



elif "marketplace.visualstudio.com" in url:
    print("işlem: vscode eklentisi")
    title, imageUrl = get_eklenti_infos(url)
    print(title)

    created_data_id = ""
    try:
        created_data_id = get_eklenti(url)

    except:
        data = {
            "İsim": {"title": [{"text": {"content": title}}]},
            "Link": {"url": url},
            "Tags": {"multi_select": [{"name": "Diğer", "color": "default"}]},
            "selim": {"checkbox": selim},
        }

        res, created_data_id = create_eklenti(data, imageUrl)
        print(res)

    created_data_id = created_data_id.replace("-", "")
    webbrowser.open(f"https://www.notion.so/selimdilsadercn/Vs-Code-Eklentileri-531399ee6fed46aba2c9ae1211fbc355")


elif "npmjs" in url:
    print("işlem: npm paketi")
    title = url.split("package/")[1]
    print(title)

    website_url = get_website_from_npm(url)
    favicon, assets = get_favicon(website_url)

    print(favicon)

    created_data_id = ""
    try:
        created_data_id = get_npm_package(url)

    except:
        data = {
            "İsim": {"title": [{"text": {"content": title}}]},
            "Npm Url": {"url": url},
            "Assets": {"rich_text": [{"text": {"content": assets}}]},
            "selim": {"checkbox": selim},
        }

        print(data, favicon)

        res, created_data_id = create_npm_package(data, favicon)
        print(res)

    created_data_id = created_data_id.replace("-", "")
    webbrowser.open(f"https://www.notion.so/selimdilsadercn/Npm-K-t-phaneleri-0e11fd8e50554ec9b3d9ebef52213f30?p={created_data_id}&pm=c")


elif "github.com" in url:
    print("işlem: github")
    title, description = get_repo_infos(url)
    print(title)

    created_data_id = ""

    try:
        created_data_id = get_repo(url)

    except:
        data = {
            "Name": {"title": [{"text": {"content": title}}]},
            "Link": {"url": url},
            "Description": {"rich_text": [{"text": {"content": description}}]},
            "selim": {"checkbox": selim},
        }

        res, created_data_id = create_repo(data)
        print(res)

    created_data_id = created_data_id.replace("-", "")
    webbrowser.open(f"https://www.notion.so/selimdilsadercn/Github-Repositories-6b85365429944cd3b0a19ceb1ecdf2a8?p={created_data_id}&pm=c")


else:
    print("işlem: website")
    favicon, assets = get_favicon(url)
    titleTag = get_website_name(url)
    title, description = get_website_title_and_description(titleTag, url)

    if url[-1] == "/":
        url = url[:-1]

    print(title + " - " + description)

    created_data_id = ""
    try:
        created_data_id = get_website(url)

    except:
        data = {
            "İsim": {"title": [{"text": {"content": title}}]},
            "Description": {"rich_text": [{"text": {"content": description}}]},
            "assets": {"rich_text": [{"text": {"content": assets}}]},
            "Web": {"url": url},    
            "Tür": {"multi_select": [{"name": "Web", "color": "default"}]},
            "selim": {"checkbox": selim},
        }

        res, created_data_id = create_website(data, favicon)
        print(res)

    created_data_id = created_data_id.replace("-", "")
    webbrowser.open(f"https://www.notion.so/selimdilsadercn/Uygulamalar-e40ccc17932a429587e93d2336713d3a?p={created_data_id}&pm=c")
