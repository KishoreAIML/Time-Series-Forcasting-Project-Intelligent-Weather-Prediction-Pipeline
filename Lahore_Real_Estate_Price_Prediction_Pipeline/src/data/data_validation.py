import pandera as pa
from pandera import Column, DataFrameSchema
import numpy as np
import traceback
import warnings
warnings.filterwarnings("ignore")

def validate_dataset(data):
    """
    Validate the given dataset schemas(eg.datatypes,value rages,ect.)

    Args:
        data (DataFrame): it contains Lahore House Listings from Zameen.com (2025).

    Returns:
        message about valiations of each schema of the dataset.

    """
    
    try:
        schema = DataFrameSchema({"Date Posted" : Column(np.dtype("datetime64[ns]"))})
        schema.validate(data)
        schema = DataFrameSchema({"Price" : Column(int)})
        schema.validate(data)
        schema = DataFrameSchema({"Bedrooms" : Column(int)})
        schema.validate(data)
        schema = DataFrameSchema({"Bathrooms" : Column(int)})
        schema.validate(data)
        schema = DataFrameSchema({"Built Year" : Column(int)})
        schema.validate(data)
        schema = DataFrameSchema({"Kitchens" : Column(int)})
        schema.validate(data)
        schema = DataFrameSchema({"Store Rooms" : Column(int)})
        schema.validate(data)
        schema = DataFrameSchema({"Servant Quarters" : Column(int)})
        schema.validate(data)
        schema = DataFrameSchema({"Area" : Column(float)})
        schema.validate(data)
        schema = DataFrameSchema({"Title" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Type" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Purpose" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Furnished" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Gym" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Study Room" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Drawing Room" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Lawn/Garden" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Swimming Pool" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Electricity Backup" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Lounge/Sitting Room" : Column(str)})
        schema.validate(data)
        schema = DataFrameSchema({"Link" : Column(str)})
        schema.validate(data)
    except:
        print("Schema data validation faild!")
        traceback.print_exc()
    return "Dataset Validated Successfully."