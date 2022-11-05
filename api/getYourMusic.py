import pprint as p
from tqdm import tqdm
from get_token import get_token

sp,user = get_token()


# お気に入り　全曲　取得
def getYourMusic():
    limit = 50
    for i in tqdm(range(limit)):
        for j in range(len(sp.current_user_saved_tracks(limit=limit,offset=i*limit)['items'])):
            #  track_id を取得してから曲名、歌手名、歌手id取得
            track_id = sp.current_user_saved_tracks(limit=limit,offset=i*limit)['items'][j]['track']['id']
            track_name = sp.track(track_id)['name']
            artist_name = sp.track(track_id)['artists'][0]['name']
            artist_id = sp.track(track_id)['artists'][0]['id']
            print(track_name, track_id)
            print(artist_name, artist_id)
    return track_name,track_id,artist_name,artist_id


result = getYourMusic()
print(result)
