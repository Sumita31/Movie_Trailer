import webbrowser


class Movie(object):
    """This is the data structure for Movies
        Attributes:
        movie_title (str): title of the movie.
        movie_description (str): movie storyline.
        movie_art_imagery (url str): movie poster image.
        movie_trailer_url (url str): you tube url for the movie.
    """
    def __init__(self, movie_title, movie_description, movie_art_imagery,
                 movie_trailer_url):
        self.title = movie_title
        self.description = movie_description
        self.poster_image_url = movie_art_imagery
        self.trailer_youtube_url = movie_trailer_url

    def show_trailer(self):
        # open youtube movie trailer in browser
        webbrowser.open(self.trailer_youtube_url)