import pandas as pd
import numpy as np


def handling_outliers(data):
    before = len(data)
    data = data[(data["Price_PKR"] >= 1_000_000) & (data["Price_PKR"] <= 500_000_000)] 
    after = len(data)

    print(f"Removed {before - after} outlier rows.")
    print(f"Remaining rows: {after}")
    return data

def  location_granularity(location):

    location_lookup = {

        #DHA 
        "DHA Defence": "DHA",
        "Defence": "DHA",

        "DHA Phase 1": "DHA Phase 1",
        "DHA Phase 2": "DHA Phase 2",
        "DHA Phase 3": "DHA Phase 3",
        "DHA Phase 4": "DHA Phase 4",
        "DHA Phase 5": "DHA Phase 5",
        "DHA Phase 6": "DHA Phase 6",
        "DHA Phase 7": "DHA Phase 7",
        "DHA Phase 8": "DHA Phase 8",
        "DHA Phase 9": "DHA Phase 9",
        "DHA Phase 9 Prism": "DHA Phase 9 Prism",

        #Bahria Town
        "Bahria Town": "Bahria Town",
        "Bahria Town Sector A": "Bahria Town",
        "Bahria Town Sector B": "Bahria Town",
        "Bahria Town Sector C": "Bahria Town",
        "Bahria Town Sector D": "Bahria Town",
        "Bahria Town Sector E": "Bahria Town",
        "Bahria Town Sector F": "Bahria Town",

        #Park View City
        "Park View City": "Park View City",
        "Park View City - Rose Block": "Park View City",
        "Park View City - Tulip Block": "Park View City",
        "Park View City - Jasmine Block": "Park View City",
        "Park View City - Crystal Block": "Park View City",

        #Lake City
        "Lake City": "Lake City",
        "Lake City - Sector M": "Lake City",
        "Lake City - Sector N": "Lake City",

        #Johar Town 
        "Johar Town Phase 1": "Johar Town",
        "Johar Town Phase 2": "Johar Town",

        #Wapda Town
        "Wapda Town Phase 1": "Wapda Town",
        "Wapda Town Phase 2": "Wapda Town",

        #Valencia
        "Valencia Housing Society": "Valencia Housing Society",

        #LDA Avenue
        "LDA Avenue": "LDA Avenue",
        "LDA Avenue Block A": "LDA Avenue",
        "LDA Avenue Block B": "LDA Avenue",

        #Others
        "Model Town": "Model Town",
        "Garden Town": "Garden Town",
        "Gulberg": "Gulberg",
        "Askari": "Askari",
        "Paragon City": "Paragon City",
        "Central Park Housing Scheme": "Central Park Housing Scheme",
        "State Life Housing Society": "State Life Housing Society",
        "Al Rehman Garden": "Al Rehman Garden",
        "Fazaia Housing Scheme": "Fazaia Housing Scheme",
        "Eden": "Eden",
        "Izmir Town": "Izmir Town",
        "Bahria Orchard": "Bahria Orchard",
        "Canal Garden": "Canal Garden",
        "Punjab Coop Housing Society": "Punjab Coop Housing Society",
        "Green City": "Green City",
        "Tajpura": "Tajpura",
        "Government Employees Cooperative Housing Society (GECHS)": "GECHS",
        "Bismillah Housing Scheme": "Bismillah Housing Scheme",
    }

    parts = [x.strip() for x in str(location).split(",")]
    if len(parts) >= 2:
        key = parts[1]
        return location_lookup.get(key, key)



