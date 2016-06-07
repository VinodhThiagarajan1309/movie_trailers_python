import media
import webbrowser
import fresh_tomatoes
toyStory = media.Movie("ToyStory",
                       "Kid's toys comes to life" ,
                       "https://i.ytimg.com/vi/sKO4Rks0gPM/hqdefault.jpg",
                       "https://youtu.be/QW0sjQFpXTU")
avatar = media.Movie("Avatar",
                       "Story about Navis" ,
                       "https://c1.staticflickr.com/9/8416/8709006303_8fa8eae31b.jpg",
                       "https://youtu.be/5PSNL1qE6VY")

kabali = media.Movie("Kabali",
                       "Rajinikanth's movie after a looong time" ,
                       "https://i.ytimg.com/vi/NCBQo155wxc/maxresdefault.jpg",
                       "https://youtu.be/9mdJV5-eias")

visaranai = media.Movie("Visaranai",
                       "True story based on a novel" ,
                       "http://drop.ndtv.com/Movies/images/reviews/big/visaranai.jpg",
                       "https://youtu.be/4mnzK2KIz9U")

kutramKadidhal = media.Movie("Kuttram Kadidhal",
                       "Brahmaa" ,
                       "http://files.prokerala.com/movies/pics/1280/kuttram-kadithal-movie-design-45843.jpg",
                       "https://youtu.be/urarX9X0LjA")
       
papanasam = media.Movie("Papanasam",
                       "Kamalahaasan" ,
                       "http://behindwoods.com/tamil-movies-cinema-news-15/images/the-audio-launch-of-kamal-haasan-starrer-papanasam-will-happen-on-22nd-june-photos-pictures-stills.jpg",
                       "https://youtu.be/oWow766xmy4")
       
movies = [toyStory,avatar,kabali,visaranai,kutramKadidhal,papanasam]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__module__)
