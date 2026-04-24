# Enterprise Financial Data Pipeline (Local AWS Simulation)

# Project Overview

This project demonstrates an Enterprise Financial Data Pipeline
built using local tools that simulate AWS services.

# Problem

Manual ledger consolidation was slow, error‑prone, and unable to handle
increasing financial transaction volumes.

# Solution

Designed and implemented an ETL data pipeline using: - LocalStack
(AWS Simulation) - Apache Spark (PySpark ETL) - Docker Containers - S3
Data Lake (Simulated) - Redshift (PostgreSQL Simulation)

The pipeline automatically processes raw financial datasets and prepares
executive‑ready analytics data.

------------------------------------------------------------------------

# Architecture

    Local Machine
    │
    ├── Docker
    │     ├── LocalStack → S3 Data Lake
    │     ├── Spark Container → ETL Processing
    │     └── PostgreSQL → Redshift Simulation
    │
    ├── PySpark ETL
    │       Join Sales + Tax Data
    │       Calculate Financial Metrics
    │
    └── Executive Reporting Dataset

------------------------------------------------------------------------

# Tech Stack

-   Docker
-   LocalStack
-   AWS S3 (Simulated)
-   Apache Spark / PySpark
-   PostgreSQL (Redshift Simulation)
-   Python
-   Pandas

------------------------------------------------------------------------

# Project Structure

    financial-pipeline/
    │
    ├── data/
    │   ├── sales.csv
    │   └── tax.csv
    │
    ├── docker-compose.yml
    ├── setup-localstack.sh
    ├── etl.py
    └── spark_env/

------------------------------------------------------------------------

# What I Implemented (Step‑by‑Step)

# Local Environment Setup

-   Installed Docker, LocalStack, Python, Java, Apache Spark
-   Configured Spark environment variables
-   Created Python virtual environment
-   Installed PySpark dependencies

Result: Fully local AWS‑like development environment.

------------------------------------------------------------------------

# Created Financial Dataset

Built two datasets: - **sales.csv** → sales transactions - **tax.csv** →
tax information

These simulate raw enterprise financial data sources.

------------------------------------------------------------------------

# Containerized Infrastructure (Docker)

Created `docker-compose.yml` to run: - LocalStack → AWS services
simulation - PostgreSQL → Redshift warehouse - Spark notebook → ETL
processing

Result: Reproducible data engineering infrastructure.

------------------------------------------------------------------------

# Built Local Data Lake (S3)

Using LocalStack: - Created S3 bucket - Created folders: - raw data -
processed data - Uploaded CSV datasets

    financial-pipeline-bucket/
     ├── data/
     └── financial-data/

Result: Local enterprise data lake.

------------------------------------------------------------------------

#Developed PySpark ETL Pipeline

Created `etl.py`.

ETL Logic: - Read sales data from S3 - Read tax data from S3 - Join
datasets using transaction_id - Calculate: - total_amount -
net_profit_margin - ledger_date - Write output as Parquet (Redshift
optimized)

Result: Executive‑ready analytical dataset.

------------------------------------------------------------------------

# Spark Execution

Executed pipeline using:

    spark-submit etl.py

Spark generated: - Parquet files - `_SUCCESS` marker

ETL successfully completed.

------------------------------------------------------------------------

#Data Warehouse Simulation (Redshift)

Used PostgreSQL container to simulate Amazon Redshift.

Steps: - Created warehouse table - Converted Parquet → CSV using
Pandas - Loaded data using COPY command

    SELECT * FROM financial_ledger;

Data successfully stored for reporting.

------------------------------------------------------------------------

# Final Output

Executive financial ledger containing: - transaction_id - store_id -
customer_id - sale_amount - tax_amount - total_amount -
net_profit_margin - state - sale_date - ledger_date

------------------------------------------------------------------------

# Key Data Engineering Concepts Demonstrated

-   ETL Pipeline Design
-   Data Lake Architecture
-   Distributed Processing with Spark
-   AWS Service Simulation
-   Containerized Infrastructure
-   Data Warehouse Loading
-   Analytical Dataset Creation

------------------------------------------------------------------------

# Resume Description

**Enterprise Financial Data Pipeline (AWS Simulation)**\
Designed a containerized ETL pipeline using PySpark and LocalStack to
process financial transactions from an S3 data lake into a
Redshift‑style warehouse. Implemented distributed joins, financial
metric calculations, and automated data preparation for executive
reporting.

------------------------------------------------------------------------

# Skills Demonstrated

-   Data Engineering
-   PySpark
-   AWS Architecture
-   Docker
-   SQL
-   Data Warehousing
-   ETL Automation

------------------------------------------------------------------------

# How to Run the Project

# Start Infrastructure

    docker compose up -d

# Create Bucket & Upload Data

    bash setup-localstack.sh

# Run ETL

    spark-submit etl.py

# Load to Warehouse

    psql -h localhost -p 5439 -U admin -d financialdb

------------------------------------------------------------------------
------------------------------------------------------------------------

# step_by step notes:

**Project 1: Enterprise Financial Data Pipeline 
—The Problem**: Manual ledger consolidation was slow and prone to errors as transaction
volumes grew beyond standard processing limits.
**—The Solution**: Designed an ETL pipeline using Local Spark ETL  to move financial ledger data from S3 into Redshift.
—**Implementation**: Developed PySpark scripts to join sales and tax datasets. Used Local PySpark ETL for data processing and to prepare it for executive level reporting.

# Project Folder Setup

**Project Structure:**

```
financial-pipeline/
│
├── data/
│   ├── sales.csv
│   └── tax.csv
│
├── docker-compose.yml
├── setup-localstack.sh
├── etl.py
├── financial-data
└──spark_env/
```

**project set up in local** 

**using terminal:**

create financial-pipeline folder:

```bash
mkdir financial-pipeline 

financial-pipeline
```

create folder data :

```bash
cd financial-pipeline

mkdir data 

```

inside data
create sales.csv

```bash
cd data 
nano sales.csv
```

sales.csv 

```
**create sales.csv:**
transaction_id,store_id,sale_amount,customer_id,sale_date
TXN001,STORE01,1250.50,CUST123,2026-04-01
TXN002,STORE02,890.75,CUST456,2026-04-02
TXN003,STORE01,2100.00,CUST789,2026-04-03
TXN004,STORE03,450.25,CUST123,2026-04-04
```

**Save:**
CTRL + O 
ENTER 
CTRL + X

inside data
create tax.csv

```bash
cd data 
nano tax.csv
```

tax.csv

```
**create tax.csv:**
transaction_id,tax_rate,tax_amount,state
TXN001,0.085,106.29,TX
TXN002,0.0625,55.67,CA
TXN003,0.085,178.50,TX
TXN004,0.08,36.02,NY
```

**Save:**
CTRL + O 
ENTER 
CTRL + X

create -compose.yml

```bash
cd financial-pipeline

nano docker-compose.yml

services:

  localstack:
    image: localstack/localstack:3.5
    container_name: localstack-main
    ports:
      - "4566:4566"
    environment:
      SERVICES: s3,glue,redshift,iam,sts
      DEBUG: 1
      DEFAULT_REGION: us-east-1
      AWS_ACCESS_KEY_ID: test
      AWS_SECRET_ACCESS_KEY: test
      LS_LOG: trace
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "./localstack-data:/var/lib/localstack"

  postgres:
    image: postgres:14
    container_name: postgres-db
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: financials
    ports:
      - "5432:5432"

  spark:
    image: jupyter/pyspark-notebook:python-3.11
    container_name: spark-etl
    depends_on:
      - localstack
      - postgres
    volumes:
      - .:/home/jovyan/work
    ports:
      - "8888:8888"
```

**Save:**
CTRL + O 
ENTER 
CTRL + X

create localstack.sh:

```bash
cd financial-pipeline 

nano setup-localstack.sh 

create setup-localstack.sh:

#!/bin/bash
echo "🚀 Setting up LocalStack AWS environment..."

# Wait for services
sleep 20

# Create S3 bucket
aws --endpoint-url=http://localhost:4566 s3 mb s3://financial-ledger-bucket --region us-east-1

# Upload raw data
aws --endpoint-url=http://localhost:4566 s3 cp data/sales.csv s3://financial-ledger-bucket/raw/sales/
aws --endpoint-url=http://localhost:4566 s3 cp data/tax.csv s3://financial-ledger-bucket/raw/tax/

# Create bucket structure
aws --endpoint-url=http://localhost:4566 s3api put-object --bucket financial-ledger-bucket --key processed/consolidated/

echo "✅ S3 bucket 'financial-ledger-bucket' ready with sample data!"
echo "📁 Raw data uploaded to: s3://financial-ledger-bucket/raw/"

```

**Save:**
CTRL + O 
ENTER 
CTRL + X

etl.py

```bash
cd financial-pipeline 

nano etl.py 
```

```python

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

```

**Save:**
CTRL + O 
ENTER 
CTRL + X

**Requirements(TOOLS)**

Make sure the following are installed:

```
docker 29.4.0
LocalStack CLI 4.6.0
Python (3.14.4)
Java (JDK 8 or 11)
Apache Spark
PySpark
```

**install docker desktop**

```bash
brew install --cask docker
```

Launch Docker

```bash
open /Applications/Docker.app
```

Verify:

```bash
docker --version
```

example:

```bash
Docker version 29.4.0, build 9d7ad9ff18
```

**install localstack**

```bash
brew install localstack/tap/localstack-cli
```

Verify:

```bash
localstack --version
```

example:

```bash
LocalStack CLI 4.6.0
```

**Install Python**

Install Python:

```bash
brew install python
```

Check version:

```bash
python3 --version
```

Example:

```bash
Python 3.14.4
```

**Install Java (Required for Spark)**

Spark works best with Java 11.

Install java:

```bash
brew install openjdk@11
```

Set JAVA_HOME:

```bash
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 11)' >> ~/.zshrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
```

Check version:

```bash
java -version
```

Example:

```bash
openjdk 17.0.18 2026-01-20
OpenJDK Runtime Environment Homebrew (build 17.0.18+0)
OpenJDK 64-Bit Server VM Homebrew (build 17.0.18+0, mixed mode, sharing)
```

**Install Apache Spark**

Install Apache Spark:

```bash
brew install apache-spark
```

Check installation:

```bash
spark-submit --version
```

Example:

```bash
WARNING: Using incubator modules: jdk.incubator.vector
Using Spark's default log4j profile: org/apache/spark/log4j2-defaults.properties
26/04/16 19:54:02 WARN Utils: Your hostname, Prasannahs-MacBook-Air.local, resolves to a loopback address: 127.0.0.1; using 192.168.0.3 instead (on interface en0)
26/04/16 19:54:02 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Welcome to
    *__*__              __
   / **__/__**  *___* _____/ /__
*_. \ \/ _ \/ _ `/ __*/  '_/
 /**___/ .__**/\_,*_/_*/ /_/\_\   version 4.1.1
    /_/
Using Scala version 2.13.17, OpenJDK 64-Bit Server VM, 17.0.18
Branch HEAD
Compiled by user runner on 2026-01-02T11:55:02Z
Revision c0690c763bafabd08e7079d1137fa0a769a05bae
Url https://github.com/apache/spark
Type --help for more information.
```

**Configure Spark Environment**

Open configuration:

```bash
nano ~/.zshrc
```

Add:

**Apache Spark Setup**

```bash
export SPARK_HOME=/opt/homebrew/opt/apache-spark/libexec
export PATH=$SPARK_HOME/bin:$PATH
export SPARK_LOCAL_IP=127.0.0.1
```

Reload:

```bash
source ~/.zshrc
```

Verify:

```bash
which spark-submit
```

Example:

```python
/Users/Name/spark_env/bin/spark-submit
```

**Create Virtual Environment**

Move to project:

```bash
cd financial-pipeline
```

Create venv:

```bash
python3 -m venv spark_env
```

Activate:

```bash
source spark_env/bin/activate
```

**Install PySpark**

Inside venv

Install pyspark :

```bash
pip install pyspark
```

Verify:

```bash
python -c "import pyspark; print('PySpark Working')"
```

Example:

```bash
PySpark Working
```

**Final Architecture (Very Important)**

```
macOS
│
├── Homebrew
│     ├── Docker
│     ├── localstack
│     ├── Python
│     ├── Java
│     └── Apache Spark
│└── Virtual Environment
        └── PySpark (Python API)
```

EXECUTION PROCESS:
start docker desktop:

```bash
open -a Docker
docker ps -a
docker start localstack-mai
docker ps 
```

**start localstack:**

```bash
docker pull localstack/localstack:3.5

docker run -d \
--name localstack-main \
-p 4566:4566 \
-e SERVICES=s3,glue,redshift,iam \
-e DEBUG=1 \
localstack/localstack:3.5
docker ps
docker logs localstack-main
localstack status services
```

# Created Data Lake (LocalStack S3)

**open new terminal create s3 buckets, folders & files:**

```bash
awslocal s3 ls

awslocal s3 mb s3://financial-pipeline-bucket
make_bucket: financial-pipeline-bucket

awslocal s3 ls
2026-04-15 00:02:49 financial-pipeline-bucket

awslocal s3api put-object \
--bucket financial-pipeline-bucket\
--key financial-data/
Last login: Wed Apr 15 00:32:11 on ttys001

awslocal s3api put-object \
--bucket financial-pipeline-bucket\
--key data/

awslocal s3 ls s3://financial-pipeline-bucket/
PRE data/PRE financial-data/

awslocal s3 cp data/sales.csv s3://financial-pipeline-bucket/data/sales.csv
upload: sales.csv to s3://financial-pipeline-bucket/data/sales.csv

awslocal s3 cp data/tax.csv s3://financial-pipeline-bucket/data/tax.csv
upload: tax.csv to s3://financial-pipeline-bucket/data/tax.csv

awslocal s3 ls s3://financial-pipeline-bucket/data/
2026-04-15 00:44:07        224 sales.csv
2026-04-15 00:44:08        131 tax.csv

awslocal s3 cp s3://financial-pipeline-bucket/data/sales.csv -
transaction_id,store_id,sale_amount,customer_id,sale_date
TXN001,STORE01,1250.50,CUST123,2026-04-01
TXN002,STORE02,890.75,CUST456,2026-04-02
TXN003,STORE01,2100.00,CUST789,2026-04-03
TXN004,STORE03,450.25,CUST123,2026-04-04

awslocal s3 ls s3://financial-pipeline-bucket/financial-data/
2026-04-15 00:51:43          0
```

**Run the Spark Application**

Navigate to the project directory:

```bash
source spark_env/bin/activate

cd financial-pipeline
```

Run the script using Spark:

```python
spark-submit \  
--packages org.apache.hadoop:hadoop-aws:3.3.1 \
etl.py
```

**Successful Execution Output**

After execution:

parquet file generated:

```bash

awslocal s3 ls s3://financial-pipeline-bucket/financial-data/
2026-04-15 12:32:37          0 _SUCCESS
2026-04-15 12:32:37       3139 part-00000-18ff1f6b-deee-42cc-84a4-d18b0d826998-c000.snappy.parquet
```

```
financial-data/
├── part-00000-18ff1f6b-deee-42cc-84a4-d18b0d826998-c000.snappy.parquet
└── _SUCCESS
```

Spark creates: - parquet files (part-*.jparquet) - _SUCCESS file

indicating successful execution

**run local redshift:**

```bash
docker run -d \
  --name local-redshift \
  -p 5439:5432 \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=Password123 \
  -e POSTGRES_DB=financialdb \
  postgres:15

docker pull postgres:15

docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS                  PORTS                                         NAMES
f37e4530e75a   postgres:15                 "docker-entrypoint.s…"   32 seconds ago   Up 31 seconds           0.0.0.0:5439->5432/tcp, [::]:5439->5432/tcp   local-redshift
0d53e8b59b80   localstack/localstack:3.5   "docker-entrypoint.sh"   16 hours ago     Up 16 hours (healthy)   0.0.0.0:4566->4566/tcp, [::]:4566->4566/tcp   localstack-main

psql -h localhost -p 5439 -U admin -d financialdb
Password for user admin: Password123 

financialdb=# CREATE TABLE financial_transactions (
    transaction_id VARCHAR(50),
    account_id VARCHAR(50),
    amount FLOAT,
    transaction_type VARCHAR(20),
    transaction_date TIMESTAMP
);
CREATE TABLE

\d financial_transactions
 Table "public.financial_transactions"
      Column      |            Type             | Collation | Nullable | Default 
------------------+-----------------------------+-----------+----------+---------
 transaction_id   | character varying(50)       |           |          | 
 account_id       | character varying(50)       |           |          | 
 amount           | double precision            |           |          | 
 transaction_type | character varying(20)       |           |          | 
 transaction_date | timestamp without time zone |           |          | 

create financial-data folder locally
awslocal s3 cp s3://financial-pipeline-bucket/financial-data/ ./data --recursive
download: s3://financial-pipeline-bucket/financial-data/_SUCCESS to data/_SUCCESS
download: s3://financial-pipeline-bucket/financial-data/part-00000-18ff1f6b-deee-42cc-84a4-d18b0d826998-c000.snappy.parquet to data/part-00000-18ff1f6b-deee-42cc-84a4-d18b0d826998-c000.snappy.parquet
```

```bash
(spark_env) Name-MacBook-Air financial-pipeline % pip list | grep pandas
pandas          3.0.2

(spark_env) Name-MacBook-Air financial-pipeline % python3
Python 3.14.4 (main, Apr  7 2026, 13:13:20) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import pandas as pd
... 
... df = pd.read_parquet(
...     "financial-data/part-00000-18ff1f6b-deee-42cc-84a4-d18b0d826998-c000.sn\
appy.parquet"
... )
... 
... df.to_csv("financial_data.csv", index=False)
... 
... print(df.head())
... 

  transaction_id store_id customer_id  ...  state   sale_date  ledger_date
0         TXN004  STORE03     CUST123  ...     NY  2026-04-04   2026-04-15
1         TXN003  STORE01     CUST789  ...     TX  2026-04-03   2026-04-15
2         TXN002  STORE02     CUST456  ...     CA  2026-04-02   2026-04-15
3         TXN001  STORE01     CUST123  ...     TX  2026-04-01   2026-04-15

[4 rows x 10 columns]
>>> 
>>> 
>>> exit()

(spark_env) Name-MacBook-Air financial-pipeline % ls
data			financial-data		setup-localstack.sh
docker-compose.yml	etl.

(spark_env) Name-MacBook-Air financial-pipeline % psql -h localhost -p 5439 -U admin -d financialdb
Password for user admin: 
psql (14.20 (Homebrew), server 15.17 (Debian 15.17-1.pgdg13+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
Type "help" for help.

financialdb=# CREATE TABLE financial_ledger (
    transaction_id VARCHAR(50),
    store_id VARCHAR(50),
    customer_id VARCHAR(50),
    sale_amount FLOAT,
    tax_amount FLOAT,
    total_amount FLOAT,
    net_profit_margin FLOAT,
    state VARCHAR(50),
    sale_date DATE,
    ledger_date DATE
);
CREATE TABLE
financialdb=# /q
financialdb-# \q
(myvenv) Name-MacBook-Air financial-pipeline % psql -h localhost -p 5439 -U admin -d financialdb \
-c "\COPY financial_ledger FROM 'financial_data.csv' CSV HEADER;"
Password for user admin: 
COPY 4
(myvenv) Name-MacBook-Air financial-pipeline % psql -h localhost -p 5439 -U admin -d financialdb
Password for user admin: 
psql (14.20 (Homebrew), server 15.17 (Debian 15.17-1.pgdg13+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
Type "help" for help.

financialdb=# SELECT * FROM financial_ledger LIMIT 10;
 transaction_id | store_id | customer_id | sale_amount | tax_amount | total_amount | net_profit_margin | state | sale_date  | ledger_date 
----------------+----------+-------------+-------------+------------+--------------+-------------------+-------+------------+-------------
 TXN004         | STORE03  | CUST123     |      450.25 |      36.02 |       486.27 |                92 | NY    | 2026-04-04 | 2026-04-15
 TXN003         | STORE01  | CUST789     |        2100 |      178.5 |       2278.5 |              91.5 | TX    | 2026-04-03 | 2026-04-15
 TXN002         | STORE02  | CUST456     |      890.75 |      55.67 |       946.42 |             93.75 | CA    | 2026-04-02 | 2026-04-15
 TXN001         | STORE01  | CUST123     |      1250.5 |     106.29 |      1356.79 |              91.5 | TX    | 2026-04-01 | 2026-04-15
(4 rows)

financialdb=# 

```

```bash
Name-MacBook-Air ~ % awslocal s3 ls
2026-04-15 00:02:49 financial-pipeline-bucket

Name-MacBook-Air ~ % awslocal s3 ls s3://financial-pipeline-bucket/
                           PRE data/
                           PRE financial-data/

Name-MacBook-Air ~ % docker start local-redshift
local-redshift

Name-MacBook-Air ~ % psql -h localhost -p 5439 -U admin -d financialdb
Password for user admin: 
psql: error: connection to server at "localhost" (::1), port 5439 failed: FATAL:  password authentication failed for user "admin"

Name-MacBook-Air ~ % psql -h localhost -p 5439 -U admin -d financialdb
Password for user admin: 
psql (14.20 (Homebrew), server 15.17 (Debian 15.17-1.pgdg13+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
Type "help" for help.

financialdb=# SELECT * FROM financial_ledger LIMIT 5;
 transaction_id | store_id | customer_id | sale_amount | tax_amount | total_amount | net_profit_margin | state | sale_date  | ledger_date 
----------------+----------+-------------+-------------+------------+--------------+-------------------+-------+------------+-------------
 TXN004         | STORE03  | CUST123     |      450.25 |      36.02 |       486.27 |                92 | NY    | 2026-04-04 | 2026-04-15
 TXN003         | STORE01  | CUST789     |        2100 |      178.5 |       2278.5 |              91.5 | TX    | 2026-04-03 | 2026-04-15
 TXN002         | STORE02  | CUST456     |      890.75 |      55.67 |       946.42 |             93.75 | CA    | 2026-04-02 | 2026-04-15
 TXN001         | STORE01  | CUST123     |      1250.5 |     106.29 |      1356.79 |              91.5 | TX    | 2026-04-01 | 2026-04-15
(4 rows)

financialdb=# \q
```

```bash
localstack stop:
docker stop localstack-main
```

---

