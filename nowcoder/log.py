import pandas as pd

file = 'log.xlsx'
raw = pd.read_excel(file)
result = raw.drop_duplicates().groupby('URL').size()
print(result)


    
   