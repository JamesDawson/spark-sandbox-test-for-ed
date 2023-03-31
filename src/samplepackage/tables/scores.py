from datetime import date
from typing import List, Tuple
from pyspark.sql.types import StructType, StructField, IntegerType, DateType
from pyspark.sql import DataFrame, SparkSession

schema = StructType([
    StructField("date", DateType(), False),
    StructField("person_id", IntegerType(), False),
    StructField("score", IntegerType(), True),
])

defaultData = [
    (date(2022, 7, 14), 1, 42),
    (date(2022, 7, 14), 2, 73),
    (date(2022, 7, 14), 3, 53),
    (date(2022, 7, 15), 1, 92),
    (date(2022, 7, 15), 2, 13),
    (date(2022, 7, 15), 3, 86),
]


class Scores():
    spark: SparkSession
    data: List[Tuple] = defaultData

    def __init__(self, spark):
        self.spark = spark

    def get_df(self) -> DataFrame:
        return self.spark.createDataFrame(self.data, schema)
