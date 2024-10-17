import os
from pyspark.sql import SparkSession

def create_spark_session(app_name="SparkApp", local_ip="10.0.1.54", log_level="ERROR"):
    os.environ["SPARK_LOCAL_IP"] = local_ip
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.warehouse.dir", "/path/to/your/warehouse") \
        .getOrCreate()
    spark.sparkContext.setLogLevel(log_level)
    return spark
