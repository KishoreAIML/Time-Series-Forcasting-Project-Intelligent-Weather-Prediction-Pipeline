import pandas as pd
import numpy as np

class clean_dataset:
    """
    cleans the given dataset includes duplicates,nulls,data type conversions,ect.

    Methods:
        remove_duplicate_records,handle_null_records,rename_columns,convert_price,convert_to_sqft,remove_data_inconsistency.

    Returns:
        Dataset(DataFrame): it contains Clean Lahore House Listings from Zameen.com (2025) data.
    """
    def __init__(self,data,null_cols):
        self.data = data
        self.null_cols = null_cols
    
    def remove_duplicate_records(self):
        self.data.drop_duplicates()
        return self.data
    
    def handle_null_records(self):
        self.data.drop(columns = self.null_cols,inplace = True)
        return self.data
    
    def rename_columns(self):
        self.data.columns = self.data.columns.str.replace(" ","_").str.replace("/","_")
        return self.data
    
    def convert_price(self,price):
        if pd.isna(price):
            return None

        price = str(price).strip()
        parts = price.split(maxsplit=1)

    
        if len(parts) == 1:
            try:
                return float(parts[0])
            except ValueError:
                return None

        value = float(parts[0])
        unit = parts[1].lower()

        if "crore" in unit:
            return value * 10000000.0
        elif "lakh" in unit:
            return value * 100000.0
        elif "arab" in unit:
            return value * 1000000000.0
        else:
            return None

    def convert_to_sqft(self,area):
        value, unit = area.split(maxsplit=1)
        value = float(value)
        unit = unit.lower()

        if "kanal" in unit:
            return value * 4500.0
        elif "marla" in unit:
            return value * 225.0
        elif "sq" in unit or "sqft" in unit:
            return value
        else:
            return None
    def remove_data_inconsistency(self, cols):
        for col in cols:
            self.data[col] = (self.data[col].replace("-", np.nan).replace("", np.nan))

            self.data[col] = pd.to_numeric(self.data[col], errors="coerce")

        return self.data

    
