import pandera as pa
from pandera import Column, DataFrameSchema
import numpy as np
import traceback
import warnings
warnings.filterwarnings("ignore")

def validate_dataset(data):
    
    try:
        schema = DataFrameSchema({"Date" : Column(np.dtype("datetime64[ns]"))})
        schema.validate(data)
        schema = DataFrameSchema({"Temperature" : Column(float)})
        schema.validate(data)
        schema = DataFrameSchema({"is_day" : Column(int)})
        schema.validate(data)
        schema = DataFrameSchema({"Relative_humidity" : Column(int, checks=pa.Check.in_range(0,100))})
        schema.validate(data)
        schema = DataFrameSchema({"Rain" : Column(float, checks = pa.Check.ge(0))})
        schema.validate(data)
        schema = DataFrameSchema({"Soil_temperature" : Column(float)})
        schema.validate(data)
        schema = DataFrameSchema({"Wind_speed" : Column(float, checks = pa.Check.ge(0))})
        schema.validate(data)
        schema = DataFrameSchema({"Surface_pressure" : Column(float)})
        schema.validate(data)
        schema = DataFrameSchema({"Pressure_msl" : Column(float)})
        schema.validate(data)
    except:
        print("Schema data validation faild!")
        traceback.print_exc()
    return "Dataset Validated Successfully.There is no any inconsisties in data!"

