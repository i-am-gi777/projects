import pandas as pd

# Load the CSV file
csv_file = "invoices.csv"
df = pd.read_csv(csv_file)

# Save to XLSX
xlsx_file = "invoices.xlsx"
df.to_excel(xlsx_file, index=False)

print(f"Converted '{csv_file}' to '{xlsx_file}'")


