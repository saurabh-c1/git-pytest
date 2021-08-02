import pandas as pd

pd.read_excel
data = pd.read_csv("data.csv")
print(data.dtypes)
print(data.agg({"Unit Price": ["min", "max"],
                "Total Cost": ["min", "max"]}))
