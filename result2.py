# Seasonal Yield Comparison using Boxplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')
plt.figure(figsize=(12, 6))
sns.boxplot(x='Season', y='Yield_Tonnes_Ha', data=df, palette='Set2')
plt.title('Crop Yield Distribution Across Different Seasons', fontsize=16)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Yield (Tonnes/Ha)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()