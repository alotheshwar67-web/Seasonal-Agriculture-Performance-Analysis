# Scatter plot: Yield vs Rainfall by Season
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')
plt.figure(figsize=(12, 7))
sns.scatterplot(x='Rainfall_mm', y='Yield_Tonnes_Ha', hue='Season', 
                data=df, alpha=0.6, s=60)
plt.title('Yield vs Rainfall by Season', fontsize=16)
plt.xlabel('Rainfall (mm)', fontsize=14)
plt.ylabel('Yield (Tonnes/Ha)', fontsize=14)
plt.legend(title='Season')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()