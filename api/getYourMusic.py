import pprint as p
from tqdm import tqdm
import datetime
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
            image_url = sp.track(track_id)['album']['images'][1]

            artist_id
            track_jouhou = sp.track(track_id)
            # print(track_name, track_id)
            # print(artist_name, artist_id)
            p.pprint(track_jouhou['duration_ms'])
    return track_name,track_id,artist_name,artist_id,track_jouhou


# result = getYourMusic()
# print(result)

duration_ms = int(238466)

def duration_ms_to_ms(duration_ms):
    ms = datetime.timedelta(seconds=(duration_ms/1000))
    # ms = ms.replace(microsecond = 0)
    ms_str = str(ms)
    print(ms_str[2:7])
    return ms
duration_ms_to_ms(238466)
