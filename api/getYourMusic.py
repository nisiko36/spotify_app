import pprint as p
from tqdm import tqdm
from get_token import get_token

sp = get_token()

# userid
user=sp.me()["id"]
print(user)

# お気に入り　全曲　取得
def getYourMusic():
    limit = 50
    for i in tqdm(range(limit)):
        for j in range(len(sp.current_user_saved_tracks(limit=limit,offset=i*limit)['items'])):
            #  tracks name and id
            track_name = sp.current_user_saved_tracks(limit=limit,offset=i*limit)['items'][j]['track']['name']
            track_id = sp.current_user_saved_tracks(limit=limit,offset=i*limit)['items'][j]['track']['id']
            print(track_name, track_id)
            #  artists name and id
            artist_name = sp.current_user_saved_tracks(limit=limit,offset=i*limit)['items'][j]['track']['artists'][0]['name']
            artist_id = sp.current_user_saved_tracks(limit=limit,offset=i*limit)['items'][j]['track']['artists'][0]['id']
            print(artist_name, artist_id)
    return track_name,track_id,artist_name,artist_id


result = getYourMusic()
print(result)
