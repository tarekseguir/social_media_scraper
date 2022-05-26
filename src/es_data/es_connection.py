import logging
import os

import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch import helpers

from utils import doc_generator, safe_date, safe_value

logging.basicConfig(filename="file.log", level=logging.INFO)


class EsManagement:
    def __init__(self):
        self.es_client = Elasticsearch(
            hosts=os.environ["HOSTS"],
            port=os.environ["PORTS"]
        )
        logging.info(self.es_client.ping())

    def create_index(self, index_name: str) -> None:
        """
        Create an ES index.
        :param index_name: Name of the index.
        :param mapping: Mapping of the index.
        """
        if self.es_client.indices.exists(index=index_name):
            logging.info(f"The index {index_name} already exist")
        else:
            logging.info(f"Creating index {index_name}")
            self.es_client.indices.create(index=index_name)

    def populate_index(self, df, index_name: str) -> None:
        """
        Populate an index from a CSV file.
        :param path: The path to the CSV file.
        :param index_name: Name of the index to which documents should be written.
        """
        #df = df.replace({np.nan: None})
        logging.info(f"Writing {len(df.index)} documents to ES index {index_name}")
        df['time'] = df['time'].apply(safe_date)
        df['fetched_time'] = df['fetched_time'].apply(safe_date)
        helpers.bulk(self.es_client, doc_generator(df))
