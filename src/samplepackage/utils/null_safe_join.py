from typing import Tuple, List
from pyspark.sql import DataFrame
from pyspark.sql.functions import expr


def null_safe_join(
    left_df: DataFrame,
    right_df: DataFrame,
    join_conditions: List[Tuple]
) -> DataFrame:
    def construct_join_condition_string(condition: Tuple):
        return f"l.`{condition[0]}` <=> r.`{condition[1]}`"

    left_df = left_df.alias("l")
    right_df = right_df.alias("r")

    right_select_cols = [
        c for c in right_df.columns
        if c not in (jc[1] for jc in join_conditions)
    ]

    join_conditions = [
        construct_join_condition_string(c)
        for c in join_conditions
    ]

    join_conditions_string = " and ".join(join_conditions)

    joined_df = left_df.join(right_df, expr(join_conditions_string), "left") \
        .select("l.*", *right_select_cols)

    return joined_df
