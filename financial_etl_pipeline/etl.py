from pyspark.sql import SparkSession
from pyspark.sql.functions import *


# Initialize Spark with AWS Glue configuration
spark = (
    SparkSession.builder
    .appName("CheckOutput")
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:4566")
    .config("spark.hadoop.fs.s3a.access.key", "test")
    .config("spark.hadoop.fs.s3a.secret.key", "test")
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
    .getOrCreate()
)
# S3 Paths for LocalStack
S3_BUCKET = "financial-pipeline-bucket"
SALES_PATH = "s3a://financial-pipeline-bucket/data/sales.csv"
TAX_PATH = "s3a://financial-pipeline-bucket/data/tax.csv"
OUTPUT_PATH = "s3a://financial-pipeline-bucket/financial-data/"

print("Loading Sales Data...")
sales_df = spark.read.option("header", "true").csv(SALES_PATH)
sales_df = sales_df.withColumn("sale_amount", col("sale_amount").cast("double"))
sales_df = sales_df.withColumn("sale_date", to_date(col("sale_date"), "yyyy-MM-dd"))

print("Loading Tax Data...")
tax_df = spark.read.option("header", "true").csv(TAX_PATH)
tax_df = tax_df.withColumn("tax_amount", col("tax_amount").cast("double"))
tax_df = tax_df.withColumn("tax_rate", col("tax_rate").cast("double"))

print("Raw Data Preview:")
sales_df.show(5, truncate=False)
tax_df.show(5, truncate=False)

# Core Business Logic: Join & Enrich
print("Joining Sales + Tax Data...")
consolidated_df = sales_df.join(tax_df, "transaction_id", "left") \
    .withColumn("total_amount", 
                round(coalesce(col("sale_amount"), lit(0)) + coalesce(col("tax_amount"), lit(0)), 2)) \
    .withColumn("net_profit_margin", 
                round((col("sale_amount") - coalesce(col("tax_amount"), lit(0))) / col("sale_amount") * 100, 2)) \
    .withColumn("ledger_date", current_date()) \
    .select(
        "transaction_id", "store_id", "customer_id", "sale_amount", 
        "tax_amount", "total_amount", "net_profit_margin", 
        "state", "sale_date", "ledger_date"
    ).orderBy(desc("sale_date"))

print("Consolidated Executive Dataset:")
consolidated_df.show(truncate=False)
print(f"Total Records: {consolidated_df.count()}")

# Write Executive-Ready Output (Parquet for Redshift)
print("Writing to S3 (Redshift-ready format)...")
consolidated_df.coalesce(1).write \
    .mode("overwrite") \
    .parquet(OUTPUT_PATH)

print("ETL Pipeline Complete!")
print(f"Output location:s3://financial-pipeline-bucket/financial-data/")
spark.stop()
