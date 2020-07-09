'''
class News:
    #add docstring quotes here
    News class to define News objects
    #add docstring quotes here

    def __init__(self,id,author,title,description,image_url,published_at):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.image_url = image_url
        self.published_at = published_at
'''

##############Testing##############
class Articles:
    '''
    articles class to define article objects
    '''
    def __init__(self,id,author,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        
class News:
    '''
    News class to define news objects
    '''

    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = "https://www.youtube.com/watch?v=RN75zSpYp7M"+ url
        self.category = category
        self.country = country