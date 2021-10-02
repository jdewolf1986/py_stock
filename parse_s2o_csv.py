import pandas as pd

filename = 'stock2own_scraped.csv'
substring = 'StockAnalysis/Stock'

# read csv to DataFrame
df = pd.read_csv(filename)
# write urls to series
urls = df.iloc[:,0]

urls_clean =[]
for url in urls:
    if substring in url:
        urls_clean.append(url)

dfs_url_clean =[]
for url_clean in urls_clean:
    print(url_clean)
    dfs = pd.read_html(url_clean)
    print(dfs)


#     dfs = pd.read_html(url)
#     # annual statements:
#     dfs[0]
#     # quarterly statements:
#     dfs[1]
#     # PE and EPS
#     dfs[2]
#     # Value Price & Investment Recovery Time
#     dfs[3]
