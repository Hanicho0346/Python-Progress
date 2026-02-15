from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def play(self):
        """All media must implement this method."""

class Movie(Media):
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director

    def play(self):
        print(f"Playing movie: {self.title} directed by {self.director}")

class Song(Media):
    def __init__(self, title, artist):
        super().__init__(title)
        self.artist = artist

    def play(self):
        print(f"Playing song: {self.title} by {self.artist}")

class Podcast(Media):
    def __init__(self, title, host):
        super().__init__(title)
        self.host = host

    def play(self):
        print(f"Playing podcast: {self.title} hosted by {self.host}")

medias = [
    Movie("Inception", "Christopher Nolan"),
    Song("Shape of You", "Ed Sheeran"),
    Podcast("The Daily", "Michael Barbaro")
]


for media in medias:
    media.play()
