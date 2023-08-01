import os
import pandas as pd
from pyspark.sql import SparkSession
 
file_path = f"C:/Users/manishak/Downloads/11Jul2023.xlsx"
df_content = pd.read_excel(file_path)
df2 = df_content

# Create PySpark SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("Japan_table") \
    .getOrCreate()
#Create PySpark DataFrame from Pandas
sparkDF=spark.createDataFrame(df_content) 
sparkDF.printSchema()
sparkDF.show()





