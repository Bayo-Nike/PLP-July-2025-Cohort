# Step 1.1: Load the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first few rows
df.head()

# Step 1.2: Inspect Data Structure
# Check data types and missing values
df.info()

# Check for missing values
df.isnull().sum()

# Step 1.3: Clean the Data
# Drop missing values (if any)
df.dropna(inplace=True)


# Step 2.1: Compute Basic Statistics
# Summary statistics
df.describe()

# Step 2.2: Group by Species and Compute Mean of Numerical Columns
# Group by species and compute mean
grouped_means = df.groupby('species').mean(numeric_only=True)
grouped_means


# Task 3: Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set(style="whitegrid")

try:
    # Line Chart
    # Simulated line chart (e.g., petal length trends over sample index per species)
    plt.figure(figsize=(10, 5))
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.plot(subset.index, subset['petal_length'], label=species)
    plt.title('Petal Length Trends Across Samples')
    plt.xlabel('Sample Index')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    plt.show()

    # Bar Chart
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='species', y='petal_length', ci=None)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.show()

    # Histogram
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x='sepal_width', bins=20, kde=True)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species')
    plt.title('Sepal Length vs. Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.show()

except Exception as e:
    print("❌ Error creating visualizations:", str(e))

