
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower

# Initialize Spark session
spark = SparkSession.builder.appName("CustomerDataETL").getOrCreate()

# Read CSV data from local (simulate S3)
df = spark.read.option("header", True).csv("data/sample_customers.csv")

# Data Cleaning: Drop nulls and lowercase emails
df_clean = df.dropna(subset=["customer_id", "email"]).withColumn("email", lower(col("email")))

# Show sample transformed data
df_clean.show()

# Write to Parquet (simulate S3 or RDS load)
df_clean.write.mode("overwrite").parquet("output/cleaned_customers")

# Stop Spark session
spark.stop()
