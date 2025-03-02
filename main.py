import pandas as pd
from chembl_webresource_client.new_client import new_client

target = new_client.target
target_query = target.search('coronavirus')
targets = pd.DataFrame.from_dict(target_query)
targets