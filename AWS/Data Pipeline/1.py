import os

os.environ['PYSPARK_SUBMIT_ARGS'] = 'pyspark-shell'

# from pyspark.sql import SparkSession

# from pyspark.sql import SparkSession

# Initialize a Spark session
# spark = SparkSession.builder \
#     .appName("Word Count Example") \
#     .getOrCreate()