# Dependencies
import pandas as pd
from transformation_functions import rename_columns

def test_rename_columns():
    # Assemble
    input_df=pd.DataFrame({
       "Column A":[1,2],
       "Column B":[3,4]
    })
    expected_df=pd.DataFrame({
        "column_a":[1,2],
        "column_b":[3,4]
    })

    # Act
    output_df=rename_columns(input_df)

    # Assert
    pd.testing.assert_frame_equal(left=output_df,right=expected_df)

