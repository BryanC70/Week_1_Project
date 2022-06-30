from  pyyoutube import Api

API_KEY = "AIzaSyCklFcu9yBlbmh3FQQFB7Jcndps5U35_zc"
api = Api(api_key=API_KEY)
api.get_authorization_url()

def get_videos(channel_name):
    channel = api.get_channel_info(channel_name=channel_name)

    playlist_id = channel.contentDetails.relatedPlaylists.uploads

    playlist_items, _=api.get_playlist_item(playlist_id=playlist_id, count=10, limit=6)

    videos = []
    for item in playlist_items:
        video_id = item.contentDetails.videoId
        video_info = api.get_video_info(video_id=video_id)
    return videos

