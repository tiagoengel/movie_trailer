class Movie():
    """
    Represents a movie with an image url and youtube url than can be used
    to watch the movie's trailer.

    Args:
        title (str): The movie title
        poster_image_url (str): Url pointing to a poster image
        trailer_youtube_url (str): Url poiting to an youtube trailer

    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
