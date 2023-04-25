import pandas as pd
import polars as pl

def main():
    pd_df = pd.read_csv("../docs/user_list.csv")
    print(pd_df.last)
