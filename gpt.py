import os
from strictjson import *
from dotenv import load_dotenv

load_dotenv()

def get_website_title_and_description(titleTag, url):
  api = os.getenv('OPENAI_API_KEY')
  os.environ['OPENAI_API_KEY'] = api

  try:
    res = strict_json(
      system_prompt = '''
        i will give you website titleTag with title and description and website url. 
        if the titleTag has NOT domain of the url than title is domain on the url and descipriton is titleTag, write title as Title Case and dont write thing like .com or www.
        if the titleTag has url domain than in general title and descripiton will be seperated with ["-", "|", ":"] and title is one word, 
        but this are not always like that you can use your mind to find which word or words are the title one, 
        determine the title and the description of the website, 
        dont change any descripiton text and syntax, 
        give your results in UTF-8
      ''',
      user_prompt = [titleTag, url],
      output_format = {
        'Title': 'website title as string',
        'Description': 'website description as string',
      }
    )
    return res["Title"], res["Description"]
  
  except Exception as e:
    print(e)
    return {"Title": titleTag, "Description": ""}
  