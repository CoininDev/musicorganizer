import spotify_connect as sptf

token = sptf.get_token()

sptf.search_playlist(token, "Emo Forever")
