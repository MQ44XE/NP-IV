import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.DataFrame()
df2 = pd.DataFrame(columns=["n", "Fib"])
df1["A"] = [1, 3, 5]
df1["B"] = [2, 4, 6]
df1["A^2+B^2"] = (df1["A"])**2 + (df1["B"])**2

# sor hozzáadása DF-hez
row1 = {"n": 1, "Fib": 1}
row2 = {"n": 2, "Fib": 1}
new_df = pd.DataFrame([row1, row2])
df2 = pd.concat([df2, new_df], axis=0, ignore_index=True)

df3 = pd.DataFrame(range(1,21), columns= ["n"])
df3["Fib"] = np.nan
# df3.loc[df3["n"]==1, "Fib"]=1
# df3.loc[df3["n"]==2, "Fib"]=1

# df3.loc[df3["n"] in [1, 2], "Fib"]=1

for index, row in df3.iterrows():
    if index in [0, 1]:
        df3.loc[index, "Fib"] = 1
    else:
        df3.loc[index, "Fib"] = df3.loc[index-1, "Fib"] + df3.loc[index-2, "Fib"]
    # print(index)
    # print(row)
# print(df3)

class VelSzamok():

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.value= np.random.random((self.n_rows, self.n_cols))

    def plot_column_averages(self):
        averages = self.value.mean(axis=0)
        print(averages)
        plt.plot(averages)
        plt.show()
        pass

a1 = VelSzamok(5, 2)
a2 = VelSzamok(6, 3)
print(a2.value)
a2.plot_column_averages()


