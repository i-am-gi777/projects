from pyspark.sql import SparkSession

# ---------------------------
# Create Spark Session
# ---------------------------
spark = SparkSession.builder \
    .appName("CSV to Excel Converter") \
    .getOrCreate()

# ---------------------------
# EXTRACT
# Read CSV File
# ---------------------------
input_csv = "google.csv"
output_excel = "output/google.xlsx"

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(input_csv)

# ---------------------------
# TRANSFORM
# (No transformation)
# ---------------------------
final_df = df

# ---------------------------
# LOAD
# Convert to Pandas → Excel
# ---------------------------
pandas_df = final_df.toPandas()

pandas_df.to_excel(output_excel, index=False)

# Stop Spark
spark.stop()

print("Excel file created successfully!")
