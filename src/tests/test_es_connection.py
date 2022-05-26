import sys
sys.path.append('../')
import unittest
import pandas as pd
from es_data.es_connection import EsManagement

class EsconnectionTests(unittest.TestCase):

    def test_create_index(self):

        index_name = "test"
        es = EsManagement()
        es.create_index(index_name)
        self.assertTrue(es.es_client.indices.exists(index_name))
    

    def test_populate_index(self):

        index_name = "test"
        data = pd.read_csv('test_data/test1.csv')
        es=EsManagement()

        number_of_doc = int(es.es_client.cat.count(index_name, params={"format": "json"})[0]['count'])
        
        es.populate_index(data, index_name)
        es.es_client.indices.refresh(index_name)
        new_number_of_doc = int(es.es_client.cat.count(index_name, params={"format": "json"})[0]['count'])
        self.assertEqual(new_number_of_doc - number_of_doc, len(data.index))

if __name__ == '__main__':
    unittest.main()