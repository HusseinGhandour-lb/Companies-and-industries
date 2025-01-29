import pandas as pd
import matplotlib.pyplot as plt

#open data and read
df = pd.read_csv('CompainesEmployee.csv')
pd.set_option('display.max_columns', None)

try:
    #cleaning data
    df['employess'] = df['employess'].str.replace('"', '')
    df['employess'] = df['employess'].str.replace(',', '')
    df['employess'] = pd.to_numeric(df['employess'], errors='coerce')
    df.drop(df[df['country'] == 'Israel'].index, inplace=True)
    
    #extracting needed data
    em_country =df.groupby('country')['employess'].sum()
    em_ind =df.groupby('industry')['employess'].sum()
    
    #calculating it companies in countries
    it = df[df['industry'] == 'IT Software & Services']
    itInCountry = it.groupby('country')['industry'].count()
    
    #saving data
    df1 = em_ind.to_frame().reset_index()
    df1.to_csv('employees_industry.csv')
    
    df2 = itInCountry.to_frame().reset_index()
    df2.to_csv('industry_ountry.csv')
    
    df3 = em_country.to_frame().reset_index()
    df3.drop(df3[df3['employess'] < 250000.0].index, inplace= True)
    df3.to_csv('employees_countries.csv')
      
    print('done')
    
except Exception as e:
    print(f"error: {e}")