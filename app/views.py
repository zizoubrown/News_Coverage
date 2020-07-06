from flask import render_template
from app import app
from .request import get_everything

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and it's data
    '''

    # Getting news artiles
    news_articles = get_everything('articles')
    sports_news = get_everything('sports')
    business_news = get_everything('business')
    title = 'Home - Welcome to the best news website online'
    return render_template('index.html', title=title articles=news_articles, sports=sports_news, business=business_news)

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the specific news details page and its data
    '''
    return render_template('news.html',id=news_id)