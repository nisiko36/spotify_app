from .get_token import get_token

sp, user = get_token()

def create_playlist():
    sp.user_playlist_create(user, 'test')
