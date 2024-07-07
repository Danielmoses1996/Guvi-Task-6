import matplotlib.pyplot as plt

# Example plot: Comparison of cost in INR vs other currencies
plt.figure(figsize=(10, 6))
plt.bar(zomato_df['Currency'], zomato_df['Cost_INR'])
plt.xlabel('Currency')
plt.ylabel('Cost in INR')
plt.title('Cost Comparison in INR vs Other Currencies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
