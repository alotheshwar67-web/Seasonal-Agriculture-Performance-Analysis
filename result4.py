# Correlation Heatmap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')
plt.figure(figsize=(12, 10))
numeric_cols = ['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 
                'Sunlight_Hours_Day','Soil_Moisture_pct',
                'Fertilizer_kg_ha', 'Yield_Tonnes_Ha', 'Profit_INR']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix of Key Agricultural Metrics', fontsize=16)
plt.show()