# Real Estate Data Analysis and Visualization

This repository contains a Python script for analyzing and visualizing a real estate dataset using pandas and matplotlib.

## Overview

The script performs the following tasks:

1. **Read the Dataset:**
   - Replace the file path in the script with the correct location of your real estate dataset.

   ```python
   data = pd.read_csv(r'c:\Users\User\Downloads\archive (1)\realtor-data.zip.csv')

```Remove Null Values:
Remove null values from the dataset.```

data.dropna(inplace=True)
data.info()

## Display Information:

Display information about the dataset, including unique counts for each attribute.

plt.title('Unique Counts for Each Attribute')
plt.xlabel('Attribute')
plt.ylabel('Count')

Print and Visualize Unique Values:

Specify the column name for which you want to print unique values and visualize their occurrence.

column_name = 'city'

unique_values = data[column_name].unique()
value_counts = data[column_name].value_counts()
value_counts = value_counts.sort_values(ascending=False)

plt.bar(value_counts.index, value_counts.values, color='skyblue')
plt.title(f'Occurrence of Unique Values in {column_name}')
plt.xlabel(column_name)
plt.ylabel('Count')
plt.show()

Generate Histograms for Numeric Columns:

Generate histograms for each numeric column.

Remove Duplicates and Save Cleaned Data:

Remove duplicate rows from the dataset and save the cleaned data to a CSV file.

Contributors
Woodrow W. Wilson
Feel free to contribute, report issues, or suggest improvements!