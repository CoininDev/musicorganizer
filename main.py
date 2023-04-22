import spotify_connect as sptf

token = sptf.get_token()

def get_playlist_id(json_playlist):
    return json_playlist["playlists"]["items"][0]["id"]

def get_track_id(json_track):
    #TODO

#pesquisar todas as músicas da playlist
playlist = sptf.search_playlist(token, "Emo Forever")
playlist_id = get_playlist_id(playlist)

'''
lógica:
    pesquisar todas as músicas da playlist;
    criar lista de grupos #dicionário[nome do gênero, array com ID das músicas];
    pra cada música:
        pesquisar o gênero;
        se ainda não houver, criar um grupo com o nome do gênero

spotify_connect vai precisar:
    criar uma playlist;
    inserir uma música na playlist;
'''
