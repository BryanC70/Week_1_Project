from googleapiclient.discovery import build

api_key = "AIzaSyCklFcu9yBlbmh3FQQFB7Jcndps5U35_zc"
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
  part = 'statistics',
  forUsername='sentdex'
)

response = request.execute()

print(response)