import pandas as pd
from chembl_webresource_client.new_client import new_client

target = new_client.target
target_query = target.search('coronavirus')
targets = pd.DataFrame.from_dict(target_query)
targets

selected_target = targets.target_chembl_id[4]
selected_target

activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")
