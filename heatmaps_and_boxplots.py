import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the dataset
df = pd.read_csv("clients_shopping_center.csv")

# General data description
print(df.head())
print(df.describe())

# Boxplot for each numerical column
numeric_columns = df.select_dtypes(include=[np.number]).columns
for column in numeric_columns:
    plt.figure()
    sns.boxplot(data=df, y=column)
    plt.title(f"Boxplot for {column}")
    plt.show()

# Histograms for each numerical column
for column in numeric_columns:
    plt.figure()
    sns.histplot(data=df, x=column, bins=20, kde=True)
    plt.title(f"Histogram for {column}")
    plt.show()

# Heatmap for the correlation matrix
corr = df[numeric_columns].corr()
plt.figure()
sns.heatmap(data=corr, vmin=-1, vmax=1, cmap="coolwarm", annot=True)
plt.title("Heatmap for the Correlation Matrix")
plt.show()
