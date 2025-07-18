# Spotify API 연동 모듈 예시
import requests

def get_access_token(client_id, client_secret):
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={'grant_type': 'client_credentials'},
        auth=(client_id, client_secret)
    )
    return response.json()['access_token']

def search_tracks_by_bpm(access_token, bpm):
    headers = {'Authorization': f'Bearer {access_token}'}
    query = f'tempo:{bpm}'
    response = requests.get(
        f'https://api.spotify.com/v1/search?q={query}&type=track',
        headers=headers
    )
    return response.json()
