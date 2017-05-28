import media
import fresh_tomatoes

pulp_fiction = media.Movie("Pulp Fiction",
                           1994,
                           "Vincent Vega (John Travolta) and Jules Winnfield (Samuel L. Jackson) are hitmen with a penchant for philosophical discussions.",
                           "https://www.gstatic.com/tv/thumb/movieposters/15684/p15684_p_v8_ac.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

primer = media.Movie("Primer",
                     2004,
                     "Two engineers build a time machine",
                     "http://www.impawards.com/2004/posters/primer_xlg.jpg",
                     "https://www.youtube.com/watch?v=3nj5MMURCm8&t=3s")

twothousandandone = media.Movie("2001: A Space Odyssey",
                                1968,
                                "A computer becomes dangerous on a spaceship.",
                                "https://images-na.ssl-images-amazon.com/images/I/41%2BMbGYLI7L.jpg",
                                "https://www.youtube.com/watch?v=XHjIqQBsPjk")

drive = media.Movie("Drive",
                    2011,
                    "A getaway driver gets in trouble with a mob.",
                    "http://i.ebayimg.com/00/s/NTAwWDMzOA==/z/rh8AAOxycD9TVjek/$_35.JPG?set_id=2",
                    "https://www.youtube.com/watch?v=KBiOF3y1W0Y")

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               2014,
                               "A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies.",
                               "http://www.impawards.com/2014/posters/edge_of_tomorrow_ver11.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI")

seven = media.Movie("SEVEN",
                    1995,
                    "Two detectives, Mills and Somerset, hunt a serial killer.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNT"+
                    "NjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY1200_CR69,0,630,1200_AL_.jpg",
                    "https://www.youtube.com/watch?v=znmZoVkCjpI")

# Each movie is grouped into a single array, which is sorted by the year that it was released.
movies = [pulp_fiction, primer, twothousandandone, drive, edge_of_tomorrow, seven]
movies.sort(key=lambda x: x.year_released, reverse=True)

fresh_tomatoes.open_movies_page(movies)
