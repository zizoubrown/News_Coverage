from app import app
import urllib.request,json
from  .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_everything(category):
    '''
    Function that gets the json response to our url request
    '''
    get_everything_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_everything_url) as url:
        get_everything_data = url.read()
        get_more_news_response = json.loads(get_everything_data)

        news_results = None

        if get_everything_response['results']:
            news_results_list = get_everything_response['results']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function that processes the movie result and transform them to a list of objects
    '''

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        authur = news_item.get('authur')
        title = news_item.get('title')
        description = news_item.get('description')
        image_url = news_item.get('image')
        published_at = news_item.get('published at')

        if image_url:
            news_object = News(id,authur,title,description,image_url,published_at)
            news_results.append(news_object)

        return news_results