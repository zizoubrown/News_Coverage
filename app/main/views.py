from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_news,get_everything,search_news

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and it's data
    '''

    # Getting news artiles
    news_articles = get_everything('bbc-news')
    #top_headlines_news = get_everything('headlines')
    #latest_news = get_everything('latest')

    title = 'Home - Welcome to the best news website online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('main.search',news_name=search_news))
    else:
        return render_template('index.html', title=title, article=news_articles) #headlines=top_headlines_news, latest=latest_news)

@main.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the specific news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'
    return render_template('news.html',title=title, news=news)

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