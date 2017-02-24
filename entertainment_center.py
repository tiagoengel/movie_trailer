"""A full (not really) entertainment center

Use this module to see a pretty web page with a list of
must watch movies.

Examples:
    List the must watch movies (opinionated)

        $ python entertainment_center.py
"""
from media import Movie
from fresh_tomatoes import open_movies_page

MUST_WATCH = [
    Movie(title="Batman Begins",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BNTM3OTc0MzM2OV5BMl5BanBnXkFtZTYwNzUwMTI3._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=neY2xVmOfUM"),
    Movie(title="Her",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=WzV6mXIOVl4"),
    Movie(title="Rush",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BOWEwODJmZDItYTNmZC00OGM4LThlNDktOTQzZjIzMGQxODA4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=lzNbGH1oZJc"),
    Movie(title="Ex Machina",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=EoQuVnKhxaM"),
    Movie(title="Room",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjE4NzgzNzEwMl5BMl5BanBnXkFtZTgwMTMzMDE0NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=E_Ci-pAL4eE"),
    Movie(title="Interstellar",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=zSWdZVtXT7E"),
    Movie(title="Inception",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=YoHD9XEInc0"),
    Movie(title="Donnie Darko",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BZWQyN2ZkODktMTBkNS00OTBjLWJhOGYtNGU4YWVkNTY0ZDZkXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=ZZyBaFYFySk"),
    Movie(title="Predestination",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTAzODc3NjU1NzNeQTJeQWpwZ15BbWU4MDk5NTQ4NTMx._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=jcQacCfi_pw"),
    Movie(title="Oldboy",
          poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTI3NTQyMzU5M15BMl5BanBnXkFtZTcwMTM2MjgyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
          trailer_youtube_url="https://www.youtube.com/watch?v=2HkjrJ6IK5E")]

open_movies_page(MUST_WATCH)
