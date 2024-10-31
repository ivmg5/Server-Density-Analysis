# **Server Density Analysis**
> *Analyzing server density trends across regions with visualizations and statistical summaries.*

## **Introduction**
The Server Density Analysis project aims to provide insights into server density trends across various countries and regions over time. Through statistical analysis and data visualization, this project facilitates the understanding of global and regional server distribution trends, enabling more informed infrastructure planning and decision-making.

## **Project Description**
- **Main functionality:** Analyzes server density data across multiple countries, visualizing trends and relationships through descriptive statistics, boxplots, histograms, and correlation heatmaps.
- **Technologies used:** Python, Pandas, NumPy, Matplotlib, Seaborn.
- **Challenges faced:** Dealing with missing values and maintaining consistency in unit conversion across datasets.
- **Future improvements:** Expanding regional comparison capabilities and adding automated data cleaning processes.

## **Table of Contents**
1. [Introduction](#introduction)
2. [Project Description](#project-description)
3. [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)

## **Installation**
1. **Prerequisites**:
   - **Python** - [Download Python](https://www.python.org/downloads/)
   - **Pandas** - `pip install pandas`
   - **NumPy** - `pip install numpy`
   - **Matplotlib** - `pip install matplotlib`
   - **Seaborn** - `pip install seaborn`

2. **Clone the repository:**
   ```bash
   git clone https://github.com/ivmg5/Server-Density-Analysis.git
   cd Server-Density-Analysis
   ```

3. **Run specific Python scripts based on your analysis needs:**
   - **Basic statistical analysis:** `obtaining_descriptive_statistics.py`
   - **Boxplots and heatmaps:** `heatmaps_and_boxplots.py`
   - **General project analysis:** `main.py`

### **Configuration Options**
- Ensure dataset files (e.g., `clients_shopping_center.csv`, `data.csv`) are in the same directory as the script you intend to run.
- Set environment variables for debug mode if necessary by exporting `DEBUG=true` before running the script.

## **Usage**
Run scripts to perform specific analyses:

1. **Run `obtaining_descriptive_statistics.py`** to analyze height and weight statistics from `weight_height_gender.csv`. The output will include:
   - Basic dataset information
   - Summary statistics (mean, median, standard deviation)
   - Calculations such as trimmed mean, weighted mean, mode, variance, and quantiles for height.

   ```bash
   python obtaining_descriptive_statistics.py
   ```

2. **Run `heatmaps_and_boxplots.py`** for generating boxplots, histograms, and a correlation heatmap from the `clients_shopping_center.csv` dataset. This script will output:
   - Descriptive statistics and distribution graphs for each numeric variable.
   - A heatmap showing correlation between variables.

   ```bash
   python heatmaps_and_boxplots.py
   ```

3. **Run `main.py`** for server density analysis across countries, producing:
   - A line graph comparing Mexico's server density to the global average over time.
   - Top 10 countries by server density, pie chart comparisons, and a heatmap for the EU.

   ```bash
   python main.py
   ```

## **License**
This project is licensed under the MIT License.

[![Build Status](https://img.shields.io/badge/status-active-brightgreen)](#)
[![Code Coverage](https://img.shields.io/badge/coverage-85%25-yellowgreen)](#)
