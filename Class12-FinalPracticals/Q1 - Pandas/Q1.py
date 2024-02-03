import pandas as pd

# 1. Create the DataFrame
data = {'M2': [[45, 2], [-3, 10], [5, -2], [8, 15], [-6, -5], [9, 3]]}  # Create a dictionary with a list of lists as values
df = pd.DataFrame(data)  # Create the DataFrame from the dictionary

# 2. Replace negative values with 0
df = df.where(df >= 0, 0)  # Use where() to replace negative values with 0 in-place

# 3. Display the modified DataFrame
print("DataFrame with negative values replaced by 0:\n", df)

# 4. Display the shape of the DataFrame
print("\nShape of the DataFrame:", df.shape)  # Use shape attribute to get dimensions
