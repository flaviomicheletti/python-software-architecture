# Existing MediaPlayer interface
class MediaPlayer:
    def play(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass


# New AdvancedMediaPlayer interface
class AdvancedMediaPlayer:
    def playVideo(self):
        pass

    def playAudio(self):
        pass


# Adapter class that implements the AdvancedMediaPlayer interface
# and internally uses the existing MediaPlayer
class MediaPlayerAdapter(AdvancedMediaPlayer):
    def __init__(self, media_player):
        self.media_player = media_player

    def playVideo(self):
        self.media_player.play()

    def playAudio(self):
        self.media_player.play()

# Example usage
media_player = MediaPlayer()
media_adapter = MediaPlayerAdapter(media_player)

media_adapter.playVideo()  # Internally calls media_player.play()
media_adapter.playAudio()  # Internally calls media_player.play()

"""
In the example, the `MediaPlayer` class represents the existing interface 
with methods `play()`, `pause()`, and `stop()`. The `AdvancedMediaPlayer` 
class represents the new interface with methods `playVideo()` and `
playAudio()`. The `MediaPlayerAdapter` class is the adapter that implements 
the `AdvancedMediaPlayer` interface by internally using the `MediaPlayer` 
object. 

By using the adapter, you can now call the `playVideo()` and `playAudio()` 
methods on the `MediaPlayerAdapter` instance, and they will be translated to 
the corresponding `play()` method calls on the `MediaPlayer` object. 
"""