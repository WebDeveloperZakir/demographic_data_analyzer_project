import pandas as pd

# Define headers
headers = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
]

# Load raw adult.data
df = pd.read_csv('adult.data', header=None, names=headers)

# Strip leading/trailing spaces from string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Save cleaned CSV with headers
df.to_csv('adult_cleaned.csv', index=False)

print("adult_cleaned.csv created successfully!")
