import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import pprint as p

# アクセストークン取得
def get_token():
    #認証パート Authentication part
    username = 'nisikou'
    client_id ='c075fec56bf3410a81739af5c63448aa'
    client_secret = 'd07afb0d788247f192f295dddc9b0389'
    redirect_uri = 'http://127.0.0.1:8000/'

    #アプリの権限付与に使用する
    scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private'
    # 絶対必要なやつ
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = client_id,
                                                    client_secret=client_secret,
                                                    redirect_uri=redirect_uri,
                                                    scope=scope))
    user=sp.me()["id"]
    return sp, user
