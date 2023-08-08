import os
import pandas as pd
from pyspark.sql import SparkSession
 
file_path = f"C:/Users/manishak/Downloads/11Jul2023.xlsx"
df_content = pd.read_excel(file_path)
data_frame1 = df_content

# Create PySpark SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("Japan_table") \
    .getOrCreate()
#Create PySpark DataFrame from Pandas
sparkDF=spark.createDataFrame(df_content) 
sparkDF.printSchema()
sparkDF.show()



def merge_the_tools(string, k):
    # your code goes here
    list_of_strings = [list(set(string[i:i+k])) for i in range(0,len(string),k)]
    
    print(list_of_strings)   
    # AABCAAADA

# if _name_ == '__main__':
    string, k = 'AABCAAADA', int(3)
    merge_the_tools(string, k)
# =




