# Customer Data Migration ETL Pipeline

This project showcases a sample data migration ETL pipeline using **AWS Glue**, **PySpark**, and **S3**. It simulates a customer dataset being extracted, transformed, and loaded into a cloud database or a parquet file.

## Problem Statement
Companies often need to migrate legacy customer data into modern, cloud-based systems. Ensuring data consistency, transformation accuracy, and scalability is critical.

## Tech Stack
- **AWS Glue**
- **PySpark**
- **AWS S3**
- **Python**
- **AWS RDS / Parquet Output**

## Workflow
1. Read raw customer data from S3
2. Clean and transform using PySpark (handle nulls, normalize fields)
3. Output results to a target (RDS or S3 Parquet)
4. Validate record counts and log metrics

## Folder Structure

├── scripts/ │ └── etl_script.py ├── data/ │ └── sample_customers.csv ├── README.md

## Sample Script Preview (PySpark) ```python df = spark.read.option("header", True).csv("s3://bucket-name/sample_customers.csv") df_clean = df.dropna().withColumn("email", lower(col("email"))) df_clean.write.parquet("s3://bucket-name/processed/customers/")

Future Improvements 

Add logging and error handling

Automate job trigger using AWS Lambda

Add unit tests

Author 

Naveen Charan


