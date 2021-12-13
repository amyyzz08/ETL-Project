import pandas as pd

# function
def rename_columns(input_df):
#     create copy
    df=input_df.copy(deep=True)
    column_mapping={}
    for column in df.columns:
        column_mapping[column]=column.lower().replace(" ","_")
    df=df.rename(columns=column_mapping)
    return df




