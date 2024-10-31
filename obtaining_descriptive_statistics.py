# Import the necessary libraries
import pandas as pd
import random
import numpy as np

# Load the data and apply unit conversions
df = pd.read_csv("weight_height_gender.csv")
df.Height = df.Height * 2.54  # Convert from inches to cm
df.Weight = df.Weight / 2.2  # Convert from pounds to kg

# Basic dataset information
print("Basic information of the dataset:")
print(df.info())
print()

# Statistical summary and variable ranges
print("Statistical summary:")
print(df.describe())
print()

# Trimmed Mean
sorted_df = df["Height"].sort_values()
sorted_df = sorted_df.reset_index(drop=True)
p = 5
trimmed_mean = sorted_df[p:-p].mean()
print(f"Trimmed mean of height: {trimmed_mean}")

# Weighted Mean
weights = [random.random() for i in range(len(df))]
weighted_mean = np.average(df["Height"], weights=weights)
print(f"Weighted mean of height: {weighted_mean}")

# Mode
mode = df["Height"].mode()[0]
print(f"Mode of height: {mode}")

# Median
median = df["Height"].median()
print(f"Median of height: {median}")

# Variance
variance = df["Height"].var()
print(f"Variance of height: {variance}")

# Standard Deviation
std_dev = df["Height"].std()
print(f"Standard deviation of height: {std_dev}")

# Quartiles
quartiles = df["Height"].quantile([0.25, 0.5, 0.75])
print(f"Quartiles of height: {quartiles}")
