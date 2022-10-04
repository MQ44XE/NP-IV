import pandas as pd

df_tlt = pd.read_csv("TLT.csv")
df_voo = pd.read_csv("VOO.csv")

df_test = pd.read_excel("teszt.xlsx", sheet_name="Sheet1")
# excel file-ból csinál csv-t
df_test.to_csv("df_test_output.csv")

df = pd.DataFrame(data={"A": [3, 4, "a"],
                        "B": ["dafd", 3, 5]})

# print(df_tlt, df_voo)
# # debug, "view as dataframe"
# print(df_test)

# print(df)

# adattábla első n sora (head), és utolsó n sora (tail)

# print(df_voo.head(3))
# print(df_voo.tail(3))
# print(df_voo.columns)
# print(df_voo.index)
# print(df_voo.dtypes)

# print(df["B"])
# df["C"] = ""
# print(df)
# del df["C"]
# print(df)

# debugger, evaluate expression parancsok
# df[["A", "B"]]
# df_voo.loc[0:5, "Adj Close"]
# df_voo.iloc[-5:-1]["Adj Close"]

# df_voo_copy = df_voo.copy()
# df_voo_copy.index = df_voo_copy["Date"]
# print(df_voo_copy)
# del df_voo_copy["Date"]
# print(df_voo_copy)

df_voo["Volume in thousands"] = df_voo["Volume"] / 1000
df_voo["Open Close Difference"] = df_voo["Open"] - df_voo["Close"]
print(df_voo)