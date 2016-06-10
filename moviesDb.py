# Download the required libraries
import media
import webbrowser
import fresh_tomatoes
import json
import urllib

'''This method calls theMovieDB api and get the list of top rated movies
   which is rendered in a JSON format.
   The JSON message is parsed we create Movie
   objects out of it.
   The mehtod returns a list of movie objects'''


def get_top_rated_movies():
    BASE_URL = "https://api.themoviedb.org/3/movie/"
    API_KEY = "api_key=14f6f23935d5f6396544342f801e171d"
    IMAGE_URL = "http://image.tmdb.org/t/p/w500"
    YOUTUBE_URL = "https://youtu.be/"
    json_data = urllib.urlopen(BASE_URL + "top_rated?" + API_KEY)
    movies_json_data = json.loads(json_data.read())  # JSON to Python Dict
    movies_list = []
    # iniate a counter to count the movie objects being created
    iMovieCount = 0
    for movieObj in movies_json_data['results']:
        title = str(movieObj['title'])
        poster = str(movieObj['poster_path'])
        # encoded version of the string
        overview = str(movieObj['overview'].encode('utf-8'))
        movie_id = str(movieObj['id'])
        trailer = ''
        videos_data = urllib.urlopen(BASE_URL + movie_id+"/videos?" + API_KEY)
        video_json_data = json.loads(videos_data.read())
        '''Inner for loop recieves a list of movie trailers and we just
        need one of them and only from Youtube break when link to one video
        is retreived'''
        for videoObj in video_json_data['results']:
            if videoObj['site'] == 'YouTube':
                trailer = str(videoObj['key'])
                break

        # Create a Movie object and push it to a List
        movies_list.append(media.Movie(
            title,
            overview,
            IMAGE_URL + poster + "?" + API_KEY,
            YOUTUBE_URL + trailer)
            )
        '''Since we are only displaying only Top 15 movies break the loop once we
        have created 15 movie objects'''
        iMovieCount += 1
        if iMovieCount == 15:
            break
    return movies_list

fresh_tomatoes.open_movies_page(get_top_rated_movies())
