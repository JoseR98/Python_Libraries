"""Module that construct the data frame with messages info"""

import pandas as pd
from parse_chat import parsedData

def newDataFrame():
    df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message'])
    return df
