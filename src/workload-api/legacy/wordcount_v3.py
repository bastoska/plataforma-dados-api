from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# initializing the Spark session
spark = SparkSession.builder \
    .appName('BigQueryReadExample') \
    .getOrCreate()

# BQ public dataset
project_id = 'bigquery-public-data'
dataset_id = 'samples'
table_id = 'shakespeare'
col_to_count = 'word'

# BQ table path
table_path = f'{project_id}.{dataset_id}.{table_id}'

# read data from table
input_df = spark.read \
    .format('bigquery') \
    .option('table', table_path) \
    .load()

# select text col to count
lines_df = input_df.select(col_to_count)

# count
words_df = lines_df.withColumn('word', explode(split(col(col_to_count), ' '))) \
                   .groupBy('word') \
                   .count()

# output path with current data
current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
output_path = f"gs://kb-wc/output/output-bq-{current_time}/"

# save to gcs
words_df.write.csv(output_path)

# stop spakr session
spark.stop()
