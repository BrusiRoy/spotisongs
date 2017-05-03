# spotisongs
#### Creates a public playlist with "Your Music" in it (so your friends can see it!)

To run this script, you are going to need the [Spotipy](https://spotipy.readthedocs.io/en/latest/#installation) library.

Then you need to [register the app](https://spotipy.readthedocs.io/en/latest/#authorized-requests) with your Spotify account.

After the registration, you will need to set these environment variables
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

You can finally launch the script with the following command `python spotisongs.py username`
