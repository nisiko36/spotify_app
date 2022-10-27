from get_token import get_token
import pprint as p

sp = get_token()
# ズルい女      3P5xrT2QevrFfjTXTkJOcC
# Sharam Q     1kK9HRCnY3kiEgiEZIjHVH
p.pprint(sp.track('3P5xrT2QevrFfjTXTkJOcC')['duration_ms'])
p.pprint(sp.track('3P5xrT2QevrFfjTXTkJOcC')['album']['images'])
# p.pprint(sp.track('3P5xrT2QevrFfjTXTkJOcC'))
# p.pprint(sp.artist_albums('1kK9HRCnY3kiEgiEZIjHVH')['items'])
p.pprint(sp.artist_albums('1kK9HRCnY3kiEgiEZIjHVH',limit=1)['items'])



# p.pprint(sp.audio_features('3P5xrT2QevrFfjTXTkJOcC'))
# p.pprint(sp.audio_analysis('3P5xrT2QevrFfjTXTkJOcC'))




    # print(len(sp.current_user_saved_tracks(limit=50,offset=1100)['items']))




    # プレイリストを作成,id取得
    # playlist = sp.user_playlist_create(user, name=create_playlist)
    # playlist_id = playlist['id']



    # playlist_id取得
    # my_playlist=sp.user_playlists(user)
    # p.pprint(my_playlist)
    # track = sp.playlist_items(playlist_id="3JKA75EOGdqTZnKpbsEw1Q")

    # p.pprint(track['items'][0]['track']['artists'][0]['name'])
    # for playlist in my_playlist['items']:
    #     p.pprint(playlist['name'])
    #     p.pprint(playlist['id'])

    # saucydog_id = '37i9dQZF1DXcmREjonh06P'


    # for songname in sp.playlist(saucydog_id)['tracks']['items']:
    # p.pprint(sp.playlist(saucydog_id)['tracks']['items'][0]['track']['name'])
        # p.pprint(songname['track']['id']+songname['track']['name'])

    # p.pprint((sp.track('1Vqs0lXeJafYZz2sxnfB3V')).keys())
