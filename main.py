# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("data.csv")

# Basic information and descriptive statistics
print("Basic information of the dataset:")
print(df.info())
print()
print("Statistical summary:")
print(df.describe())
print()

# Trimmed mean for the 'Value' column
sorted_df = df['Value'].sort_values()
sorted_df = sorted_df.reset_index(drop=True)
p = 5
trimmed_mean = sorted_df[p:-p].mean()
print(f"Trimmed mean of server density: {trimmed_mean}")

# Server density change in Mexico over time
mexico_data = df[df['Country Name'] == 'Mexico']
plt.figure()
sns.lineplot(x='Year', y='Value', data=mexico_data, label='Mexico')
sns.lineplot(x='Year', y='Value', data=df, label='Global Average')
plt.title('Change in Server Density in Mexico vs Global Average')
plt.xlabel('Year')
plt.ylabel('Server Density')
plt.legend()
plt.show()

# Server density in the last recorded year for various countries (Top 10)
latest_year = df['Year'].max()
latest_data = df[df['Year'] == latest_year]
top_countries_latest = latest_data.groupby('Country Name')['Value'].mean().sort_values(ascending=False).head(10)
plt.figure()
sns.barplot(y=top_countries_latest.index, x=top_countries_latest.values, orient='h')
plt.title(f'Top 10 Countries by Server Density in {latest_year}')
plt.xlabel('Server Density')
plt.ylabel('Country')
plt.show()

# Pie chart to compare British Virgin Islands, Liechtenstein, and Gibraltar in the last year
latest_year = df['Year'].max()
selected_countries = df[(df['Country Name'].isin(['British Virgin Islands', 'Liechtenstein', 'Gibraltar'])) & (df['Year'] == latest_year)]
plt.figure()
plt.pie(selected_countries['Value'], labels=selected_countries['Country Name'], autopct='%1.1f%%')
plt.title(f'Server Density Distribution in {latest_year} among British Virgin Islands, Liechtenstein, and Gibraltar')
plt.show()

# Vertical heatmap of server density in the European Union over the years
eu_data = df[df['Country Name'] == 'European Union']
plt.figure(figsize=(10, 8))
heatmap_data = eu_data.pivot_table(values='Value', index='Year', columns='Country Name')
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Server Density Heatmap in the European Union')
plt.xlabel('European Union')
plt.ylabel('Year')
plt.gca().invert_yaxis()
plt.show()

from scipy.stats import linregress

# Filter data to include only the regions of interest
regions_of_interest = ['Latin America & Caribbean', 'Europe & Central Asia']
filtered_data = df[df['Country Name'].isin(regions_of_interest)]

# Pivot the data so each row represents a year and each column represents a region
pivoted_data = filtered_data.pivot(index='Year', columns='Country Name', values='Value')

# Remove rows with NaN values to ensure fair comparison
pivoted_data.dropna(inplace=True)

# Calculate linear regression and R^2 coefficient
slope, intercept, r_value, p_value, std_err = linregress(pivoted_data['Latin America & Caribbean'], pivoted_data['Europe & Central Asia'])
r_squared = r_value ** 2

# Create scatter plot
plt.figure(figsize=(10, 8))
sns.scatterplot(x=pivoted_data['Latin America & Caribbean'], y=pivoted_data['Europe & Central Asia'], label='Scatterplot')
sns.regplot(x=pivoted_data['Latin America & Caribbean'], y=pivoted_data['Europe & Central Asia'], scatter=False, color='red', label=f'Linear Regression (R^2 = {r_squared:.2f})')
plt.title('Server Density Comparison between Latin America & Caribbean and Europe & Central Asia')
plt.xlabel('Server Density in Latin America & Caribbean')
plt.ylabel('Server Density in Europe & Central Asia')
plt.legend()

plt.show()
