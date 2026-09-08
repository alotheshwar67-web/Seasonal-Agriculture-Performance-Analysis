import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')
# Average Profit Across Seasons
plt.figure(figsize=(10, 6))
sns.barplot(x='Season', y='Profit_INR', data=df, estimator=np.mean,
             palette='viridis')
plt.title('Average Profit Across Seasons', fontsize=16)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Average Profit (INR)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()