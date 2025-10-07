import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df["Pulse"].dropna()
df.plot(kind = 'hist', x = 'Duration', y = 'Calories')

plt.show()