import os
from pyspark.sql import SparkSession # noqa E402
from delta import configure_spark_with_delta_pip

from samplepackage.tables import People, Scores # noqa E402
from samplepackage.utils import null_safe_join, drop_managed_table # noqa E402

if __name__ == '__main__':
    builder = SparkSession.builder.appName("MyApp")

    # Check if we're running in Synapse or locally.
    if os.environ.get("MMLSPARK_PLATFORM_INFO") == "synapse":
        spark = builder.getOrCreate()
    else:
        builder \
            .config(
                "spark.sql.extensions",
                "io.delta.sql.DeltaSparkSessionExtension") \
            .config(
                "spark.sql.catalog.spark_catalog",
                "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
            .config(
                "spark.sql.warehouse.dir",
                "/workspaces/spark-sandbox/sample_entrypoints/spark-warehouse")

        spark = configure_spark_with_delta_pip(builder).getOrCreate()

        spark.sparkContext.setLogLevel("ERROR")

    scores_df = Scores(spark).get_df()
    people_df = People(spark).get_df()

    join_conditions = [("person_id", "id"), ]

    full_df = null_safe_join(scores_df, people_df, join_conditions)

    table_name = "full_scores"

    full_df.write.format("delta").mode("overwrite").saveAsTable(table_name)

    # Clean-up
    drop_managed_table(spark, table_name)
