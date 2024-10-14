from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CheckSparkVersion").getOrCreate()
print("The version of Spark is:", spark.version)
