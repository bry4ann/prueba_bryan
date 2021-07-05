import pandas as pd 
import matplotlib.pyplot as plt

worbook1="comunas2.xlsx"

df = pd.read_excel(worbook1)

print(df.head())