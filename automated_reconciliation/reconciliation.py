#Load Data
import pandas as pd

# Load ERP data
erp = pd.read_csv("data/erp_transactions.csv")

# Load Bank data
bank = pd.read_csv("data/bank_statement.csv")

print("ERP DATA")
print(erp)

print("\nBANK DATA")
print(bank)

# Reconcile transactions
reconciliation = pd.merge(
    erp,
    bank,
    how="outer",
    on=["date", "amount"],
    indicator=True
)

print("\nRECONCILIATION RESULT")
print(reconciliation)

reconciliation["status"] = reconciliation["_merge"].map({
    "both": "Matched",
    "left_only": "Missing in Bank",
    "right_only": "Missing in ERP"
})

print("\nFINAL RESULT")
print(reconciliation)

reconciliation.to_excel("reconciliation_report.xlsx", index=False)

print("\nReport Generated Successfully!")

summary = reconciliation["status"].value_counts()

print("\nSUMMARY")
print(summary)
