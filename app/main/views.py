from flask import render_template,request,redirect,url_for
from .import main
#from ..request import get_news,get_everything,search_news
from ..request import get_news,get_article
from ..models import Articles,News

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    # getting general news sources
    general_news = get_news()
    title ='News Highlights - Homepage'
    return render_template('index.html', title = title, new = general_news)


@main.route('/news/<id>')
def news_news(id):

    '''
    View news page function that returns the news details page and its data
    '''

    results = get_article(id)
    return render_template('news.html', data = results)

@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news=searched_news)


#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    # getting general news sources
    general_news = get_news()
    title ='News Highlights - Homepage'
    return render_template('index.html', title = title, new = general_news)


@main.route('/news/<id>')
def news_news(id):

    '''
    View news page function that returns the news details page and its data
    '''

    results = get_article(id)
    return render_template('news.html', data = results)