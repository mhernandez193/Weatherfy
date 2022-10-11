import tekore as tk
import environ

env = environ.Env()
environ.Env.read_env()


class Spotify:
    def __init__(self):
        self.spotify = self.setup()

    def setup(self):
        app_token = tk.request_client_token(
            env("SOCIAL_AUTH_SPOTIFY_KEY"), env("SOCIAL_AUTH_SPOTIFY_SECRET"))

        spotify = tk.Spotify(app_token)

        return spotify

    def fetchPlaylistByKeyword(self, keyword):
        response = self.spotify.search(keyword, ('playlist',))
        return response

    # def startPlayingPlaylist(self):
    #     self.spotify.playback_shuffle(True)

    # def stopPlayingPlaylist(self):
    #     self.spotify.playback_pause()

    # def favoritePlaylist(self):
    #     return
