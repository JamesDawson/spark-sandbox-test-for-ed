import os
import shutil


def drop_managed_table(spark, table_name: str):
    sparkWarehouseDir = spark.conf.get("spark.sql.warehouse.dir") \
        .replace("file:", "")

    deltaTableDir = os.path.join(sparkWarehouseDir, table_name)

    shutil.rmtree(deltaTableDir, True)

    spark.sql(f"DROP TABLE {table_name}")
