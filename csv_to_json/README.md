# CSV to JSON Conversion using Apache Spark

# Project Overview

This project demonstrates how to convert a CSV file into JSON format
using Apache Spark (PySpark).

# We will:

-   Create project structure
-   Load CSV data
-   Process data using Spark
-   Export output as JSON

------------------------------------------------------------------------

# Project Structure

    csv_to_json/
    │
    ├── netflix_subscriptions.csv
    ├── netflix_subscriptions.py
    ├── README.md
    └── output/
        └── netflix_subscriptions_json/

------------------------------------------------------------------------

# Step 1: Create Project Folder

``` bash
mkdir csv_to_json
```

------------------------------------------------------------------------

# Step 2: Create CSV File

Create:

``` bash
nano netflix_subscriptions.csv
```

# CSV Content

    user_id,name,plan,start_date,end_date,is_active,monthly_cost
    U001,Alice,Premium,2023-01-10,2024-01-10,TRUE,17.99
    U002,Bob,Standard,2023-05-01,,TRUE,13.99
    U003,Charlie,Basic,2022-11-15,2023-11-15,FALSE,9.99
    U004,David,Premium,2024-02-01,,TRUE,17.99

------------------------------------------------------------------------

# Step 3: Create PySpark Script

Create:

``` bash
nano netflix_subscriptions.py
```

# Script Code

``` python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
    "Netflix Subscription CSV to JSON"
).getOrCreate()

df = spark.read.csv(
    "netflix_subscriptions.csv",
    header=True,
    inferSchema=True
)

df.show()
df.printSchema()

df.write.json(
    "output/netflix_subscriptions_json",
    mode="overwrite"
)

spark.stop()
```

------------------------------------------------------------------------

# Step 4: Requirements (Tools)

-   Python 3.x
-   Java (JDK 11 recommended)
-   Apache Spark
-   PySpark

# Install Python

``` bash
brew install python
python3 --version
```

# Install Java

``` bash
brew install openjdk@11
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 11)' >> ~/.zshrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
java -version
```

# Install Apache Spark

``` bash
brew install apache-spark
spark-submit --version
```

# Configure Spark Environment

``` bash
nano ~/.zshrc
```

Add:

``` bash
export SPARK_HOME=/opt/homebrew/opt/apache-spark/libexec
export PATH=$SPARK_HOME/bin:$PATH
export SPARK_LOCAL_IP=127.0.0.1
```

Reload:

``` bash
source ~/.zshrc
which spark-submit
```

# Create Virtual Environment

``` bash
cd csv_to_json
python3 -m venv spark_env
source spark_env/bin/activate
```

# Install PySpark

``` bash
pip install pyspark
python -c "import pyspark; print('PySpark Working')"
```

------------------------------------------------------------------------

# Final Architecture

    macOS
     │
     ├── Homebrew
     │     ├── Python
     │     ├── Java
     │     └── Apache Spark
     │
     └── Virtual Environment
            └── PySpark (Python API)

------------------------------------------------------------------------

# Step 5: Run the Spark Application

``` bash
cd csv_to_json
spark-submit netflix_subscriptions.py
```

------------------------------------------------------------------------

# Successful Execution Output

    output/
     └── netflix_subscriptions_json/
          ├── part-00000-xxxx.json
          └── _SUCCESS

Spark creates: - JSON partition files (`part-*.json`) - `_SUCCESS` file
indicating successful execution

------------------------------------------------------------------------

# Example JSON Output

``` json
{"user_id":"U001","name":"Alice","plan":"Premium","start_date":"2023-01-10","end_date":"2024-01-10","is_active":true,"monthly_cost":17.99}
{"user_id":"U002","name":"Bob","plan":"Standard","start_date":"2023-05-01","end_date":null,"is_active":true,"monthly_cost":13.99}
```

------------------------------------------------------------------------

# Important Concepts

# SparkSession

Entry point to work with Spark DataFrames.

``` python
SparkSession.builder.appName().getOrCreate()
```

# Reading CSV

``` python
spark.read.csv()
```

Options: - `header=True` → first row as column names -
`inferSchema=True` → automatic datatype detection

# DataFrame

Structured dataset similar to a table.

Useful commands:

    df.show()
    df.printSchema()

# Writing JSON

``` python
df.write.json()
```

Option: - `mode="overwrite"` replaces existing output

------------------------------------------------------------------------

# Notes

-   Spark outputs multiple JSON files (distributed processing)
-   Empty CSV values become `null` in JSON
-   Always use `spark-submit` instead of `python file.py`

------------------------------------------------------------------------

# Learning Outcome

After completing this project, you will understand:

✅ SparkSession creation\
✅ Reading CSV using PySpark\
✅ Working with DataFrames\
✅ Writing JSON output\
✅ Running Spark jobs
