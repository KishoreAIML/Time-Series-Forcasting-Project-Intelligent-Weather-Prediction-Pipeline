import os
import pandas as pd
import numpy as np


class clean_dataset:
    def __init__(self,data):
        self.data = data
    def drop_duplicate_record(self):
        self.data = self.data.drop_duplicates()
        return self.data
    def drop_null_records(self):
        data = self.data.dropna(inplace = True)
        return self.data
    def remove_noice(self):
        num_cols = self.data.select_dtypes(include = np.number).columns
        rolling_mean_columns = [f"Rolling Mean of {col}" for col in num_cols]
        rolling_std_columns = [f"Rolling std of {col}" for col in num_cols]
        self.data[rolling_mean_columns] = self.data[num_cols].rolling(window=24).mean()
        self.data[rolling_std_columns] = self.data[num_cols].rolling(window=24).std()
        return self.data
    
