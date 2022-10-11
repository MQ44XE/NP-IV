import pandas as pd
import numpy as np

df_tlt = pd.read_csv("TLT.csv")
df_voo = pd.read_csv("VOO.csv")
# print(df_tlt)

# voo (left) és tlt (right) mergelése
# Left Join / Left Merge ; Right -; Inner-; Outer-
# Ebben az esetben Left és Inner ugyanaz, 2010-től kezdődik
# Right és Outer is ugyanaz, 2002-től kezdődik

# df_merged = df_voo.merge(df_tlt, how="inner", on="Date", suffixes = ["_voo", "_tlt"])
# print(df_merged)
# df_merged_filtered = df_merged[["Date", "Adj Close_voo", "Adj Close_tlt"]]
# print(df_merged_filtered)

df_prop = pd.read_csv("property data.csv")
# print(df_prop)

# evaluate parancsok
# df_prop["ST_NAME"] == "BERKELEY"
# df_prop.loc[df_prop["ST_NAME"] == "BERKELEY"]

# msk1 = df_prop[["ST_NAME"] == "BERKELEY"]
# print(df_prop.loc[msk1])
# msk2 = df_prop[['ST_NAME'] == 'BERKELEY', 'ST_NAME']
# print(df_prop.loc[msk2])
# msk3 = df_prop['ST_NAME'].isin(['BERKELEY', 'LEXINGTON'])
# print(df_prop.loc[msk3])
# msk4 = (df_prop['ST_NUM'] < 200) & (df_prop['ST_NAME'] == "LEXINGTON")
# print(df_prop.loc[msk4])
# msk5 = df_prop["ST_NUM"].notnull()
# print(df_prop.loc[msk5])

# df_prop = df_prop.fillna("UNKNOWN")
# print(df_prop)
# df_prop = df_prop.replace("na", "UNKNOWN")
# print(df_prop)
# df_prop = df_prop.fillna("UNKNOWN")
# print(df_prop)

# df_voo["effective_return"] = df_voo["Adj Close"] / df_voo["Adj Close"].shift(1) - 1
# print(df_voo)
# df_voo["log_return"] = np.log(df_voo["Adj Close"] / df_voo["Adj Close"].shift(1))
# print(df_voo)
# df_voo["cumsum_log_return"] = df_voo["log_return"].cumsum()
# print(df_voo)
# # Adj Close utolsó értékének meg kell egyezni az alábbi képlet eredményével
# print(df_voo.loc[0, "Adj Close"] * np.exp(df_voo.iloc[-1]["cumsum_log_return"]))