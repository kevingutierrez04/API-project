import requests
import re
import os

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'
track_id = input('Enter track id: ')
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
print(r.json())

#CODE FROM SLACK
def extract_track_id(url):
    match = re.search(r'track/([a-zA-Z0-9]+)', url)
    if match:
        return match.group(1)
    else:
        return None
# Collect up to 5 track URLs from the user
def get_user_tracks():
    track_ids = []
    for i in range(5):
        url = input(f"Enter track URL {i+1} (or 'done' to finish): ").strip()
       
# checks if the user input is 'done' (case-insensitive). If the user types 'done', the loop breaks, stopping further input requests.
       
        if url.lower() == 'done':
            break
        track_id = extract_track_id(url)
        if track_id:
            track_ids.append(track_id)
    
        else:
            print("Invalid URL. Please try again.")
  # After the loop finishes, this line returns the track_ids list, which contains all the valid track IDs entered by the user.
    return track_ids
# Main logic
track_ids = get_user_tracks()
if not track_ids:
    print("No valid track IDs entered.")
else:
    seed_tracks = ','.join(track_ids)
    print('seed_tracks: ' + seed_tracks + '\n')
    # Make the API request to get recommendations
    response = requests.get(
        BASE_URL + 'recommendations',
        params={'seed_tracks': seed_tracks},
        headers=headers
    )
    # Print the response
    if response.status_code == 200:
        recommendations = response.json()
        for track in recommendations.get('tracks', []):
            print(f"Recommended Track: {track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")
            print(f"URL: {track['external_urls']['spotify']}\n")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())