import spark_startup  # noqa F401
from delta import DeltaTable
from pyspark.sql import SparkSession # noqa E402
from samplepackage.tables import People, Scores # noqa E402
from samplepackage.utils import null_safe_join, drop_managed_table # noqa E402

spark = SparkSession.getActiveSession()


def test_create_delta_table():
    scores_df = Scores(spark).get_df()
    people_df = People(spark).get_df()

    join_conditions = [("person_id", "id"), ]

    full_df = null_safe_join(scores_df, people_df, join_conditions)

    table_name = "full_scores"

    full_df.write.format("delta").mode("overwrite").saveAsTable(table_name)

    output_table = DeltaTable.forName(spark, table_name)

    assert output_table
    assert output_table.toDF().count() == 6

    # Clean-up
    drop_managed_table(spark, table_name)
