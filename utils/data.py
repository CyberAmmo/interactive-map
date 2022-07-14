import pandas as pd

class PandasData:
    data = pd.read_csv('Ukrainian_cities.csv')

    LAT = list(data['LAT'])
    LNG = list(data['LNG'])
    POPULATION = list(data['POPULATION'])