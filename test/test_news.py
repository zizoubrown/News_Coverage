import unittest
from models import news
from main import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("techcrunch", "Jordan Crook", 'Killings in Kibera', 'The events that caused panic', "https://techcrunch.com/wp-content/uploads/2020/07/Mariam-Naficy.jpg?w=400","2020-07-06T14:19:14Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()