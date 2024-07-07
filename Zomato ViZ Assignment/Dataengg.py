import pandas as pd

# Load Zomato dataset
zomato_url = "https://raw.githubusercontent.com/nethajinirmal13/Training-datasets/main/zomato/zomato.csv"
zomato_df = pd.read_csv(zomato_url)

# Load country ISO codes
country_code_url = "https://github.com/nethajinirmal13/Training-datasets/raw/main/zomato/Country-Code.xlsx"
country_code_df = pd.read_excel(country_code_url)

# Merge Zomato data with country codes
zomato_df = zomato_df.merge(country_code_df, on='Country Code', how='left')

# Convert currency to Indian Rupees (INR)
exchange_rates = {
    'AED': 20.36,  
    'USD': 75.12,
    
}

# Function to convert to INR
def convert_to_inr(row):
    if row['Currency'] == 'INR':
        return row['Cost']
    else:
        return row['Cost'] * exchange_rates.get(row['Currency'], 1.0)

# Apply conversion to create new column
zomato_df['Cost_INR'] = zomato_df.apply(convert_to_inr, axis=1)

# Display first few rows of modified dataframe
print(zomato_df.head())
