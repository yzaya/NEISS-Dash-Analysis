#%%
import os, time
import pandas as pd
#%%
fact_directory = 'NEISS_All_Data/Fact Tables/'

dfs = []
start_time = time.time()
for filename in os.listdir(fact_directory):
    filename_l = filename.lower()
    if filename_l.endswith('xlsx'):
        filepath = os.path.join(fact_directory, filename)
        df = pd.read_excel(filepath)
        dfs.append(df)
data_load_finish = time.time() - start_time
print(data_load_finish)