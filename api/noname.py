from .get_token import get_token
import pprint as p

sp, user= get_token()
# ズルい女      3P5xrT2QevrFfjTXTkJOcC
# Sharam Q     1kK9HRCnY3kiEgiEZIjHVH

def test():
    zuruionna_id = '3P5xrT2QevrFfjTXTkJOcC'
    zuruionna = sp.track(zuruionna_id)
    # zuruionna = sp.track(zuruionna_id)['duration_ms']
    # images = sp.track(zuruionna_id)['album']['images']

    # p.pprint(zuruionna['name'])
    # p.pprint(zuruionna['artists'][0]['name'])
    return zuruionna
zuruionna=test()


# どうせ、愛だ feat. クリープハイプ 5CRQuINnKZ5ElgKpgwETCX
# 空音 3rTxb36W3M1BCxx00iiwMU

#  tracks name and id
track_name = sp.current_user_saved_tracks()['items'][0]['track']['name']
track_id = sp.current_user_saved_tracks()['items'][0]['track']['id']
print(track_name, track_id)
#  artists name and id
artist_name = sp.current_user_saved_tracks()['items'][0]['track']['artists'][1]['name']
artist_id = sp.current_user_saved_tracks()['items'][0]['track']['artists'][1]['id']
# print(artist_name,artist_id)

# # 時間
# p.pprint(sp.track('3P5xrT2QevrFfjTXTkJOcC')['duration_ms'])

# # # 写真
# p.pprint(sp.track('3P5xrT2QevrFfjTXTkJOcC')['album']['images'])

# # 踊りやすさとか
# p.pprint(sp.audio_features('3P5xrT2QevrFfjTXTkJOcC'))
# p.pprint(sp.audio_analysis('3P5xrT2QevrFfjTXTkJOcC'))


# playlistshutoku
# p.pprint(sp.user_playlists(user,10))


# プレイリストを作成,id取得
# playlist = sp.user_playlist_create(user, name=)
# playlist_id = playlist['id']



# playlist_id取得
# my_playlist=sp.user_playlists(user)
# p.pprint(my_playlist)
# track = sp.playlist_items(playlist_id="3JKA75EOGdqTZnKpbsEw1Q")

p.pprint(sp.track(track_id)['id'])
p.pprint(sp.track(track_id)['artists'][0]['name'])
p.pprint(sp.track(track_id)['artists'][0]['id'])

