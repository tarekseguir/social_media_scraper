import pandas as pd
from datetime import datetime

def safe_date(date_value):
    return (
        pd.to_datetime(date_value) if not pd.isna(date_value)
            else  datetime(1970,1,1,0,0)
    )

def safe_value(field_val):
    return field_val if not pd.isna(field_val) else "Empty"

def doc_generator(df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        yield {
                "_index": 'your_index',
                "_type": "_doc",
                "_id" : f"{document['postid']}",
                "_source": document.to_dict(),
            }
    raise StopIteration
