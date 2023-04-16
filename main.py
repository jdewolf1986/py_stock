import pandas as pd

class Stock:

    def __init__(self,url,g_yahoo=10,g_zacks=10):
        self.df = None
        self.url = url
        self.g_yahoo = g_yahoo
        self.g_zacks = g_zacks
        self.r = 15/100 #discount rate
        self.tv = 15 #terminal value

    def get_df(self):
        # read all tables on page
        lst_dfs = pd.read_html(self.url)

        # get annual statements as df
        self.df = lst_dfs[0]

        return self.df
            
    def get_indexes(self):
        # get indexes of that df that match pars ['Avg.PE','EPS','ROIC']
        xs = []
        for x in self.df['Item Name']:
            xs.append(x)

        pars = ['Avg.PE','EPS','ROIC']
        self.pars_indx = {}
        for par in pars:
            i = 0
            while i < len(xs):
                if par == xs[i]:
                    self.pars_indx[par]= i
                i += 1
        return self.pars_indx
    
    def get_pars(self):

        self.pars_lst=[]
        for value in self.pars_indx.values():
            par_lst = self.get_df().iloc[value] 
            self.pars_lst.append(par_lst)
    
        return self.pars_lst
    

url = "https://www.stock2own.com/stockanalysis/stock/us/aapl?w=1903"

stock = Stock(url=url)
stock.get_df()
stock.get_indexes()
stock.get_pars()

print(stock.get_pars()[0])





