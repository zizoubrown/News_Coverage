import urllib.request,json
from  .models import News,Articles

#Getting api key
api_key = None

# Getting the news base url
base_url = None
#Getting the articles base url
articles_base_url = None

def configure_request(app):
    global api_key,base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_base_url = app.config['ARTICLE_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

        return news_results


def process_results(news_list):
    '''
    Function that processes the news results and transforms them into a list of objects
    Args:
        news_list:A list fo dictionaries that contain news details

    Returns :
        news_results : a list of news objects

    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        if id:
            news_object = News(id, name, description, url, category, country)
            news_results.append(news_object)

    return news_results


def get_article(id):
    get_news_details_url = articles_base_url.format(id, api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        if news_details_response['articles']:
            news_news_article = news_details_response['articles']
            news_news_results = process_article(news_news_article)
    return news_news_results


def process_article(article_response_list):
    '''
    A function that returns the article respons list
    '''
    articles_results = []
    for responses in article_response_list:
        print(responses)
        id = responses.get('id')
        author = responses.get('author')
        description = responses.get('decription')
        url = responses.get('url')
        urlToImage = responses.get('urlToImage')
        publishedAt = responses.get('publishedAt')
        content = responses.get('content')

        if urlToImage:
            article_object = Articles(
                id,author,description, url, urlToImage, publishedAt, content)
            articles_results.append(article_object)

    return articles_results



