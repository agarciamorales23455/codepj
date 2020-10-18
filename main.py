import seaborn as sns
import matplotlib.pyplot as plt
import sys

# making some changes to play around
df = sns.load_dataset('car_crashes')

# some more changes
print(df.head().to_string())
df.plot(x='alcohol', y='speeding', kind='scatter')
plt.show()

# and a little more
print(df[['alcohol', 'speeding']].corr())
sys.exit(0)

print("\nCompleted successfully")