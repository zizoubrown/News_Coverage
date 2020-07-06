from flask import render_template
from app import app
from .request import get_more_news

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and it's data
    '''

    # Getting popular news
    latest_news = get_more_news('latest')
    print(latest_news)
    title = 'Home - Welcome to the best news website online'
    return render_template('index.html', title=title latest=latest_news)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the specific news details page and its data
    '''
    return render_template('news.html',id=news_id)