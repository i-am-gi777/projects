# CSV to Excel (XLSX) Conversion using Apache Spark

# Project Overview

This project demonstrates how to convert a CSV file into an Excel
(`.xlsx`) file using **Apache Spark (PySpark)**.

The workflow includes:

-   Creating a project structure
-   Loading CSV data using Spark
-   Converting Spark DataFrame → Pandas DataFrame
-   Exporting output as an Excel file

------------------------------------------------------------------------

# Project Structure

    csv_to_excel_spark/
    │
    ├── google.csv
    ├── csv_to_excel_spark.py
    ├── README.md
    └── output/
          └── google.xlsx

------------------------------------------------------------------------

# Step 1: Create Project Folder

``` bash
mkdir csv_to_excel_spark
cd csv_to_excel_spark
```

------------------------------------------------------------------------

# Step 2: Create CSV File

Create:

``` bash
nano google.csv
```

Add sample data:

    App,Category,Rating,Reviews,Installs,Type,Price,Current_Version
    WhatsApp Messenger,COMMUNICATION,4.3,5634321,1000000000,Free,0,2.23.11
    Candy Crush Saga,GAME,4.4,3501234,500000000,Free,0,1.200.0
    Duolingo,EDUCATION,4.7,1200000,100000000,Free,0,7.96.1
    Dropbox,PRODUCTIVITY,4.2,650432,50000000,Free,0,2024.2
    Calm,HEALTH,4.6,540123,10000000,Free,0,6.2.0
    Minecraft,GAME,4.5,480123,10000000,Paid,6.99,1.19.60
    Monument Valley,GAME,4.8,150234,500000,Paid,3.99,2.6
    Evernote,PRODUCTIVITY,4.1,210345,10000000,Free,0,10.2.4
    Poweramp,MUSIC,4.6,50234,5000000,Paid,3.99,3.0.12
    Facetune,PHOTOGRAPHY,4.0,120432,1000000,Paid,4.99,4.7.2

Save and exit.

------------------------------------------------------------------------

# Step 3: Create PySpark Script

Create:

``` bash
nano csv_to_excel_spark.py
```

# Script

``` python
from pyspark.sql import SparkSession

spark = SparkSession.builder     .appName("CSV to Excel Converter")     .getOrCreate()

input_csv = "google.csv"
output_excel = "output/google.xlsx"

df = spark.read     .option("header", True)     .option("inferSchema", True)     .csv(input_csv)

final_df = df

pandas_df = final_df.toPandas()
pandas_df.to_excel(output_excel, index=False)

spark.stop()

print("Excel file created successfully!")
```

------------------------------------------------------------------------

# Requirements

Install:

-   Python 3
-   Java (JDK 8 or 11)
-   Apache Spark
-   PySpark
-   Pandas
-   OpenPyXL

------------------------------------------------------------------------

# Install Python

``` bash
brew install python
python3 --version
```

------------------------------------------------------------------------

# Install Java

``` bash
brew install openjdk@11
```

Set environment:

``` bash
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 11)' >> ~/.zshrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
```

------------------------------------------------------------------------

# Install Apache Spark

``` bash
brew install apache-spark
spark-submit --version
```

Add Spark variables:

``` bash
export SPARK_HOME=/opt/homebrew/opt/apache-spark/libexec
export PATH=$SPARK_HOME/bin:$PATH
export SPARK_LOCAL_IP=127.0.0.1
```

Reload:

``` bash
source ~/.zshrc
```

------------------------------------------------------------------------

# Create Virtual Environment

``` bash
python3 -m venv spark_env
source spark_env/bin/activate
```

Install dependencies:

``` bash
pip install pyspark pandas openpyxl
```

Verify:

``` bash
python -c "import pyspark, pandas; print('Setup Working')"
```

------------------------------------------------------------------------

# Run Spark Application

``` bash
spark-submit csv_to_excel_spark.py
```

Output:

    output/
     └── google.xlsx

Console:

    Excel file created successfully!

------------------------------------------------------------------------

# Important Concepts

# SparkSession

Entry point to Spark:

``` python
SparkSession.builder.appName().getOrCreate()
```

# Reading CSV

``` python
spark.read.csv()
```

Options:

-   `header=True` → first row as columns
-   `inferSchema=True` → auto datatype detection

# Why Convert to Pandas?

Spark cannot directly write Excel files.

    Spark DataFrame
          ↓
    toPandas()
          ↓
    Pandas DataFrame
          ↓
    Excel (.xlsx)


------------------------------------------------------------------------

# Learning Outcomes

After completing this project you will understand:

-   SparkSession creation
-   Reading CSV with PySpark
-   Spark DataFrame concepts
-   Spark → Pandas conversion
-   Writing Excel files
-   Running Spark jobs using spark-submit

