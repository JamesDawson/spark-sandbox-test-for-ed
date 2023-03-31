from typing import List, Tuple
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import DataFrame, SparkSession

schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("age", IntegerType(), True),
])

defaultData = [
    (1, "Ed", 25),
    (2, "Eli", 23),
    (3, "Mike", 32),
]


class People():
    spark: SparkSession
    data: List[Tuple] = defaultData

    def __init__(self, spark):
        self.spark = spark

    def get_df(self) -> DataFrame:
        return self.spark.createDataFrame(self.data, schema)
