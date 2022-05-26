import logging
import pandas as pd
from facebook_scraper import get_posts

logging.basicConfig(filename="file.log", level=logging.INFO)

class Fb_scraper:
    """ facebook page scraper"""

    def __init__(self, page_name):
        self.page_name = page_name

    def get_posts_info(self, nb_pages):
        """
        scrape the given facebook page.
        :param nb_pages: The number of pages to scrape from 
        return: Pandas dataframe as the result of the web scraping
        """
        list_of_posts = []
        for post in get_posts(self.page_name,pages= nb_pages):
            list_of_posts.append(post)
        df = pd.DataFrame(list_of_posts)
        return df