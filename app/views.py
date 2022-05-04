from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting tesla new
    tesla_news = get_news('tesla')
    apple_news = get_news('apple')
    # print(tesla_news)
    title = 'Home - News Today Hot Content'
    return render_template('index.html',title =title,  tesla = tesla_news, apple = apple_news )
