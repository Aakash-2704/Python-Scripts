from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read CSV").getOrCreate()

df = spark.read.csv("/workspaces/python-scripts/PySpark/Data/mtcars.csv", header=True, inferSchema=True)

df.show()


