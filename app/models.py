class News:
    '''
    News class to define News objects
    '''

    def __init__(self,id,author,title,description,image_url,published_at):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.image_url = image_url
        self.published_at = published_at
