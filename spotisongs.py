import sys

import spotipy
import spotipy.util as util

scope = 'user-library-read playlist-modify-public'
READ_LIMIT = 50


def create_playlist():
    # Creating the new playlist (delete the old one if present)
    playlists = sp.user_playlists(username)
    playlist_name = username + "'s Music"
    for playlist in playlists['items']:
        if (playlist['name'] == playlist_name):
            sp.user_playlist_unfollow(username, playlist['id'])
    # Return the playlist id of the newly created playlist
    return sp.user_playlist_create(username, playlist_name)['id']


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    playlist_id = create_playlist()
    print 'Playlist created'

    offset = 0
    results = sp.current_user_saved_tracks(READ_LIMIT, offset)
    while len(results['items']) > 0:
        tracks = list()
        for item in results['items']:
            tracks.append(item['track']['uri'])
        sp.user_playlist_add_tracks(username, playlist_id, tracks)
        offset += len(results['items'])
        results = sp.current_user_saved_tracks(READ_LIMIT, offset)

    print 'Done! ' + str(sp.user_playlist(username, playlist_id)['tracks']['total']) + ' songs were copied'
else:
    print "Can't get token for", username

