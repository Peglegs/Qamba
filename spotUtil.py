import urllib
import time
import sys
import requests
import base64

CLIENT_ID="6d6dc214017b46be974deaa6db911002"
CLIENT_SECRET="01b6d36cb27a40b09dac489336299692"
REDIRECT_URI="http://127.0.0.1:5000/welcome"
scope = "playlist-read-private playlist-modify-private user-read-email"

OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"


class SpotifyOauthError(Exception):
    pass

def get_authorize_url():
    """ Gets the URL to use to authorize this app"""
    payload = {'client_id': CLIENT_ID,
        'response_type': 'code',
            'redirect_uri': REDIRECT_URI}
    payload['scope'] = scope
    payload['state'] = "34fFs29kd09"
    urlparams = urllib.urlencode(payload)

    return "%s?%s" % (OAUTH_AUTHORIZE_URL, urlparams)


def get_token(AuthCode):
    payload = {'redirect_uri': REDIRECT_URI,
            'code': AuthCode,
            'grant_type': 'authorization_code'}
    payload['scope'] = scope
    payload['state'] = "34fFs29kd09"
    auth_header = base64.b64encode(CLIENT_ID + ':' + CLIENT_SECRET)
    headers = {'Authorization': 'Basic %s' % auth_header}
    response = requests.post(OAUTH_TOKEN_URL,data = payload, headers=headers, verify=True)
    if response.status_code is not 200:
        raise SpotifyOauthError(response.reason)
    return response.json()

