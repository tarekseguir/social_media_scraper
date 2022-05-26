import logging
from scrapers import Fb_scraper
from es_data.es_connection import EsManagement

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
logging.basicConfig(filename="file.log", level=logging.INFO)

class Scraping_option(BaseModel):
    pages: int
    """
    this list can be longuer
    """



@app.post("/facebook/{page_name}")
def get_posts(page_name: str, options: Scraping_option):
    """
    :param page_name: facebook page that we want to scrap they're posts
    :param options: the options that we want to define for scraping
    """
    logging.info(f"Start scraping posts from {page_name}")
    scraper = Fb_scraper(page_name=page_name)
    data = scraper.get_posts_info(options.pages)
    logging.info(f"Scraping completed!")
    index_name = f"{page_name}_facebook_posts"
    es = EsManagement()
    es.create_index(index_name)
    es.populate_index(data, index_name)
    
    return None