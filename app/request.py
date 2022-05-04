from app import app
import urllib.request,json
from .models import news
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    print(get_news_url)


    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        print(get_news_response)
        new_articles = None


        if get_news_response['articles']:
            new_articles_list = get_news_response['articles']
            new_articles = process_articles(new_articles_list)




    return new_articles

# left it here

def process_articles(new_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        new_list: A list of dictionaries that contain news details

    Returns :
        new_results: A list of news objects
    '''
    new_articles = []
    for new_item in new_list:
        title = new_item.get('title')
        author = new_item.get('author')
        description = new_item.get('description')
        url = new_item.get('url')
        urlToImage = new_item.get('urlToImage')
        publishedAt = new_item.get('publishedAt')
        content = new_item.get('content')
        if url:
            new_object = News(title,author,description,url,urlToImage,publishedAt,content)
            new_articles.append(new_object)
    return new_articles

# def get_movie(id):
#     get_movie_details_url = base_url.format(id,api_key)
#
#     with urllib.request.urlopen(get_movie_details_url) as url:
#         movie_details_data = url.read()
#         movie_details_response = json.loads(movie_details_data)
#
#         movie_object = None
#         if movie_details_response:
#             id = movie_details_response.get('id')
#             title = movie_details_response.get('original_title')
#             overview = movie_details_response.get('overview')
#             poster = movie_details_response.get('poster_path')
#             vote_average = movie_details_response.get('vote_average')
#             vote_count = movie_details_response.get('vote_count')
#
#             movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
#
#     return movie_object
