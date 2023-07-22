import time
import pandas as pd
import polars as pl

def execution_speed(func):
    """実行速度計測用のデコレータ
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"関数名:{func.__name__} 実行時間:{run_time}秒")
    return wrapper


def main():
    """CSVの読み込み速度を比較
    """
    file_path = r"docs\user_list_10000.csv"
    pandas_read_csv(file_path)
    polars_read_csv(file_path)


@execution_speed
def pandas_read_csv(path: str):
    user_list = pd.read_csv(path)
    print(user_list.tail(3))


@execution_speed
def polars_read_csv(path: str):
    user_list = pl.read_csv(path)
    print(user_list.tail(3))
