import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import time
def get_token():
    #認証パート Authentication part
    username = 'nisikou'
    client_id ='c075fec56bf3410a81739af5c63448aa'
    client_secret = 'd07afb0d788247f192f295dddc9b0389'
    redirect_uri = 'http://127.0.0.1:8000/'

    #アプリの権限付与に使用する(この4つじゃないとstart_playbackが使えない)
    scope = 'user-modify-playback-state user-read-playback-state user-read-currently-playing user-read-recently-played'

    # 絶対必要なやつ
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id,
                                                    client_secret=client_secret,
                                                    redirect_uri=redirect_uri,
                                                    scope=scope))
    user=sp.me()["id"]
    return sp, user


def wekeup():
    sp, user = get_token()

    hour = int(input('何時'))
    minute = int(input('何分'))
    while True:
        now = time.localtime()
        if now.tm_hour == hour and now.tm_min == minute:
            sp.start_playback(device_id='0ab4eaf89d92747733ff5e9c53e39fbff0b3b483',uris=['spotify:track:2FZXuCw75FYVfiNHtFQON9'])
            break

wekeup()
