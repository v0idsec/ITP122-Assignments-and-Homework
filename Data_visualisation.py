import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'e:/Downloads/Python stuff/hospital_readmissions.csv'
df = pd.read_csv(file_path)

# Basic info
print(df.info())
print(df.describe())

# Visualize the distribution of time spent in the hospital
plt.figure(figsize=(10, 6))
sns.histplot(df['time_in_hospital'], bins=14, kde=True, color='skyblue')
plt.title('Distribution of Time Spent in Hospital')
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.show()

# Visualize the distribution of the number of medications prescribed
plt.figure(figsize=(10, 6))
sns.histplot(df['n_medications'], bins=20, kde=True, color='salmon')
plt.title('Distribution of Number of Medications Prescribed')
plt.xlabel('Number of Medications')
plt.ylabel('Frequency')
plt.show()

# Countplot for readmitted
plt.figure(figsize=(8, 5))
sns.countplot(x='readmitted', data=df, palette='Set2')
plt.title('Readmission within 30 Days')
plt.xlabel('Readmitted')
plt.ylabel('Count')
plt.show()

# Correlation heatmap for numerical features
plt.figure(figsize=(12, 8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Features')
plt.show()

