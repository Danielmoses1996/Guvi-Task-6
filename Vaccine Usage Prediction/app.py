import pandas as pd

# Load the dataset from URL
url = "https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/Vaccine.csv"
df = pd.read_csv(url)

# Display basic information about the dataset
print(df.info())

# Display first few rows of the dataset
print(df.head())
