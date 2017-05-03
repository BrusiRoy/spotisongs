import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    offset = 0
    results = sp.current_user_saved_tracks(50, offset)
    print results
    print len(results['items']);
    while len(results['items']) > 0:
        for item in results['items']:
            track = item['track']
            print track['name'] + ' - ' + track['artists'][0]['name']
        offset += 50
        results = sp.current_user_saved_tracks(50, offset)
else:
    print "Can't get token for", username
