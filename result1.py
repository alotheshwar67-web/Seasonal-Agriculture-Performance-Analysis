# 1. Load and Inspect Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('seasonal_agriculture_performance_dataset.csv')

# 2. Check for Missing Values
print("Missing Values per Column:\n", df.isnull().sum())

# 3. Get Summary Statistics Grouped by Season
print("\nSummary Statistics for Key Metrics Grouped by Season:")
seasonal_stats = df.groupby('Season')[['Yield_Tonnes_Ha', 'Profit_INR', 'Water_Used_m3', 'Fertilizer_kg_ha']].describe()
print(seasonal_stats)