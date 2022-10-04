import pandas as pd
# url = r'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
url = r'C:\Users\Rene\github\temp\Bibel\Textkritik\manus.html'
tables = pd.read_html(url) # Returns list of all tables on page
sp500_table = tables[0] # Select table of interest

print(sp500_table)
