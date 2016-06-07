import media
import webbrowser
import fresh_tomatoes
import json
import urllib

def get_top_rated_movies():
    json_data =urllib.urlopen("https://api.themoviedb.org/3/movie/top_rated?page=1&api_key=14f6f23935d5f6396544342f801e171d")
    movies_json_data = json.loads(json_data.read())
    movies_list = []

    for movieObj in movies_json_data['results']:
        title =  str(movieObj['title'])
        poster =  str(movieObj['poster_path'])
        overview =  str(movieObj['overview'].encode('utf-8'))
        movie_id = str(movieObj['id'])
        trailer = ''

 
        videos_data = urllib.urlopen("https://api.themoviedb.org/3/movie/"+movie_id+"/videos?api_key=14f6f23935d5f6396544342f801e171d")
        video_json_data = json.loads(videos_data.read())

        for videoObj in video_json_data['results']:
            if videoObj['site'] == 'YouTube' :
                trailer = str(videoObj['key'])
                break

        
        movies_list.append(media.Movie(title,overview,
                       "http://image.tmdb.org/t/p/w500"+poster+"?api_key=14f6f23935d5f6396544342f801e171d" ,
                       "https://youtu.be/"+trailer))
        
    return movies_list



fresh_tomatoes.open_movies_page(get_top_rated_movies())
