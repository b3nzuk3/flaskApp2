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

    # print(tesla_news)
    title = 'Home - News Today Hot Content'
    return render_template('index.html',title =title,  tesla = tesla_news )

@app.route('/apple')
def apple():
    apple_news = get_news('apple')

    title = "Apple news"

    return render_template('apple.html',title=title, apple=apple_news)

@app.route('/google')
def google():
    google_news = get_news('google')

    title = "Google news"

    return render_template('google.html',title=title, google=google_news)
