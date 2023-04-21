import spotify_connect as sptf

token = sptf.get_token()

def get_playlist_id(json_playlist):
    return json_playlist["playlists"]["items"][0]["id"]

playlist = sptf.search_playlist(token, "Emo Forever")
playlist_id = get_playlist_id(playlist)
