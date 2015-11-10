# -*- coding: cp1252 -*-

import webbrowser


class Movie():
    """This class initializes the movie related infos"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """Opens the trailer´s youtube-link in the webbrowser"""

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# webbrowser always has to be imported
