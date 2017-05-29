import webbrowser


class Movie():
    """A Movie object has member elements: title, year released,
       sotryline, url to poster, and a url to a trailer"""

    def __init__(self, movie_title, movie_year_released, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.year_released = movie_year_released
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
