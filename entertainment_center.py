import media
import fresh_tomatoes

# create movie instances
apocalypto = media.Movie("Apocalypto",
                         "As the Mayan kingdom faces its decline, the rulers "
                         "insist the key to prosperity is to build more temples"
                         " and offer human sacrifices. Jaguar Paw, a young man "
                         "captured for sacrifice, flees to avoid his fate.",
                         "https://upload.wikimedia.org/wikipedia/en/6/62/Apocalypto-poster01.jpg",
                         "https://www.youtube.com/watch?v=ngWBddVNVZs")

gravity = media.Movie("Gravity",
                      "Two astronauts work together to survive after an accident"
                      " which leaves them alone in space.",
                      "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of "
                        "dream-sharing technology, is given the inverse task of "
                        "planting an idea into the mind of a CEO.",
                        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

troy = media.Movie("Troy",
                   "An adaptation of Homer's great epic, the film follows the "
                   "assault on Troy by the united Greek forces and chronicles "
                   "the fates of the men involved.",
                   "https://i.jeded.com/i/troy.11710.jpg",
                   "https://www.youtube.com/watch?v=znTLzRJimeY")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a "
                     "unique mission becomes torn between following his orders "
                     "and protecting the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in "
                           "space in an attempt to ensure humanity's survival.",
                           "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

spirited_away = media.Movie("Spirited Away",
                            "During her family's move to the suburbs, a sullen "
                            "10-year-old girl wanders into a world ruled by "
                            "gods, witches, and spirits, and where humans are "
                            "changed into beasts.",
                            "http://www.nausicaa.net/miyazaki/sen/poster_images/USA_full.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

finding_nemo = media.Movie("Finding Nemo",
                           "After his son is captured in the Great Barrier Reef"
                           " and taken to Sydney, a timid clownfish sets out on "
                           "a journey to bring him home.",
                           "http://fontmeme.com/images/Finding-Nemo-Poster.jpg",
                           "https://www.youtube.com/watch?v=yDPRaVX2p8c")



# create movie list
movies = [avatar, troy, apocalypto, gravity, inception, interstellar, spirited_away, finding_nemo]

# open webpage in browser
fresh_tomatoes.open_movies_page(movies)
