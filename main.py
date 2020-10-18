import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('car_crashes')

print(df.head().to_string())
df.plot(x='alcohol', y='speeding', kind='scatter')
plt.show()


print(df[['alcohol', 'speeding']].corr())