from pyspark.sql import SparkSession

# Step 1: Start Spark session
spark = SparkSession.builder \
    .appName("Netflix Subscription CSV to JSON") \
    .getOrCreate()

# Step 2: Read CSV
df = spark.read.csv("netflix_subscriptions.csv", header=True, 
inferSchema=True)

# Optional: Show DataFrame
df.show()
df.printSchema()

# Step 3: Write to JSON
df.write.json("output/netflix_subscriptions_json", mode="overwrite")

# Step 4: Stop Spark
spark.stop()

