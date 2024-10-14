from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("simple dataframe").getOrCreate()

data = [("john",25),("ame",24),("rock",30)]

column =["Name","Age"]

df = spark.createDataFrame(data,column)

df.show()
