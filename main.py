from googleapiclient.discovery import build
import requests
import json

class YTstats:
  def __init__(self,api_key,channel_id):
    self.api_key = api_key
    self.channel_id = channel_id
    self.channel_statistics = None

  def get_channel_statistics(self):
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
    json_url = requests.get(url)
    data = json.loads(json_url.text)
    try: 
      data = data["items"][0]['statistics']
    except:
      data = None
    return data

API_KEY = "AIzaSyCklFcu9yBlbmh3FQQFB7Jcndps5U35_zc"
youtube = build('youtube', 'v3', developerKey=API_KEY)
channelId = 'UCenK8SmNW_vOKmDUTjbjamw'

yt = YTstats(API_KEY, channelId)
data = yt.get_channel_statistics()
print(data)