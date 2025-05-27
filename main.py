import yfinance as yf
import pandas as pd
import numpy as np

class RollSpreadCalculator:
    def __init__ (self, ticket: str) -> None:
        self.ticket = ticket


    def download_from_yfinance(self, price_type:str = 'Close') -> pd.Series:
        data = yf.download(self.ticket, period="1mo", interval="1d")
        data_type = data[price_type]
        print(data)
        print(data.shape)

    def returns_from_ticket(self) -> pd.DataFrame:
        returns = np.log(self.download_from_yfinance()
                         / self.download_from_yfinance().shift(1)).dropna()
        print(returns)
        return returns
    
    def roll_spread() -> float:
        #Actividad de mañana
        spread = 1
        return spread
    


    

if __name__ == "__main__":
    ticket = 'MSFT'
    msft = RollSpreadCalculator(ticket)
    #msft.download_from_yfinance()
    msft.returns_from_ticket()
    









