# CSV to Excel (XLSX) Conversion using Pandas

# Project Overview

This project demonstrates how to convert a CSV file into an Excel (.xlsx) format file using Python and Pandas.

We will:
- Create a simple project structure
- Load CSV data using Pandas
- Convert data into a DataFrame
- Export output as an Excel file

---

# Project Structure

```
csv_to_xlsx_pandas/
│
├── invoice.csv
├── csv_to_excel.py
├── README.md
└── output/
      └── invoices.xlsx
```

---

# Input File: invoice.csv

The CSV file contains invoice transaction data.

# Columns:

| Column Name     | Description                  |
|----------------|------------------------------|
| invoice_id     | Unique invoice identifier    |
| customer_name  | Name of the customer        |
| amount         | Invoice amount              |
| status         | Payment status (Paid/Unpaid)|
| invoice_date   | Date and time of invoice    |

# Sample Data:

```
INV-1001,Sai Traders,2389.5,Paid,2025-03-10 15:22:34
INV-1002,Kiran Stores,1899.0,Unpaid,2025-03-19 10:15:22
INV-1003,Gopi Enterprises,3245.75,Paid,2025-03-12 09:40:00
INV-1004,Lakshmi & Co,1520.0,Paid,2025-03-08 14:18:11
INV-1005,Kiran Stores,2750.5,Unpaid,2025-03-14 16:47:05
```

---

# Requirements

Make sure you have Python installed and install required libraries:

```bash
pip install pandas openpyxl
```

# Libraries Used:
- pandas → Data processing
- openpyxl → Excel file writing support

---

# Project Setup

# Step 1: Create Project Folder

```bash
mkdir csv_to_xlsx_pandas
cd csv_to_xlsx_pandas
```

---

# Step 2: Create CSV File

Create `invoice.csv` and paste the dataset.

---

# Step 3: Create Python Script

Create file:

```bash
csv_to_excel.py
```

---

# Step 4: Script Code

```python
import pandas as pd

# ---------------------------
# LOAD CSV FILE
# ---------------------------
csv_file = "invoice.csv"
df = pd.read_csv(csv_file)

# ---------------------------
# TRANSFORM DATA
# ---------------------------
final_df = df

# ---------------------------
# EXPORT TO EXCEL
# ---------------------------
xlsx_file = "invoices.xlsx"
final_df.to_excel(xlsx_file, index=False)

print(f"Converted '{csv_file}' to '{xlsx_file}' successfully!")
```

---

# How to Run

Run the script using:

```bash
python csv_to_excel.py
```

---

# Output

After execution:

```
invoices.xlsx
```

Console output:

```
Converted 'invoice.csv' to 'invoices.xlsx' successfully!
```

---

# Example Excel Output

| invoice_id | customer_name     | amount  | status  | invoice_date         |
|------------|------------------|---------|---------|----------------------|
| INV-1001   | Sai Traders      | 2389.5  | Paid    | 2025-03-10 15:22:34  |
| INV-1002   | Kiran Stores     | 1899.0  | Unpaid  | 2025-03-19 10:15:22  |
| INV-1003   | Gopi Enterprises | 3245.75 | Paid    | 2025-03-12 09:40:00  |

---

# Important Concepts

# Pandas DataFrame
A DataFrame is a 2D table-like structure used for data manipulation.

# Reading CSV
```python
pd.read_csv("file.csv")
```

# Writing Excel
```python
df.to_excel("file.xlsx", index=False)
```

Requires:
```bash
openpyxl
```

---

# Notes

- Suitable for small to medium datasets
- Large datasets should use databases or Parquet format
- Excel writing is slower compared to CSV

---

# Learning Outcome

After completing this project, you will understand:

- Reading CSV files using Pandas
- Working with DataFrames
- Exporting data to Excel
- Basic Python data automation wor