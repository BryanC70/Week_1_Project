from  pyyoutube import Api

API_KEY = "AIzaSyCklFcu9yBlbmh3FQQFB7Jcndps5U35_zc"
api = Api(api_key=API_KEY)
api.get_authorization_url()

playlists_by_id = api.get_playlist_by_id(playlist_id="PLOU2XLYxmsIKpaV8h0AGE05so0fAwwfTw")
playlists_by_id.items
print(playlists_by_id.items)
