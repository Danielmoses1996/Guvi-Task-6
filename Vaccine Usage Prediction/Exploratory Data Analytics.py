import matplotlib.pyplot as plt
import seaborn as sns

# Example EDA - Countplot for H1N1 vaccine uptake
plt.figure(figsize=(8, 6))
sns.countplot(x='h1n1_vaccine', data=df)
plt.title('H1N1 Vaccine Uptake')
plt.xlabel('Received Vaccine')
plt.ylabel('Count')
plt.show()

# Example EDA - Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()
