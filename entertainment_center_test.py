# -*- coding: cp1252 -*-
import media_test
import fresh_tomatoes


# import all the files
# (build a relation between the media_test file and this one)
toy_story = media_test.Movie("Der Schuh des Manitu",
                             "Is a parody of a typical American Western movie \
                              and one of the most viewd German movies of all \
                              time",
                             "http://assets.cdn.moviepilot.de/assets/store/"
                             "91bd11b8b3fbb47dfd60a432868e3bb46709e75829a40"
                             "8b9638a34dbac1d/Der_Schuh_des_Manitu.jpg",
                             "https://www.youtube.com/watch?v=60CbjEzIOTA")

bad_boys = media_test.Movie("Bad Boys 2",
                            "Action movie about 2 cool cops rescuing the world from \
                             crime with their own means.",
                            "http://www.geeksandcleats.com/wp-content/uploads/"
                            "2014/07/bad-boys-2-geeks-and-cleats.jpg",
                            "https://www.youtube.com/watch?v=hsuKq5pNOcM")

rush_hour = media_test.Movie("Rush Hour 1",
                             "Actionfilm mit Jackie Chan und Chris Tucker gegen die \
                              Welt des Bösens",
                             "http://cineplex.tv/uploads/posts/2015-07/"
                             "1437237696_001.jpg",
                             "https://www.youtube.com/watch?v=JMiFsFQcFLE")
# create all the instances that you need
# call them with the following statement:


movies = [toy_story, bad_boys, rush_hour]
# connect to all the Front-end coding.
# style changes are placed in fresh_tomato file.
fresh_tomatoes.open_movies_page(movies)
