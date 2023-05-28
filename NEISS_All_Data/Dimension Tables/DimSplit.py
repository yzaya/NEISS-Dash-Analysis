import pandas as pd

df = pd.read_excel('ProductDim.xlsx')
df2 = pd.DataFrame()
df2[['PRODUCTNum','PRODUCT2']] = df['PRODUCT'].str.split(" - ",1,expand=True)
df2['Code'] = df['Code']
df2['PRODUCT'] = df2['PRODUCT2']
df2 = df2.drop(columns=['PRODUCT2', 'PRODUCTNum'])
df2.to_excel('ProductDim2.xlsx',index=False)
