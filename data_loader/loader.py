import pandas as pd
import os


def load_data(file_path):
    """
    Đọc dữ liệu từ file CSV bằng Pandas

    :param file_path: đường dẫn tới file student.csv
    :return: DataFrame Pandas
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Không tìm thấy file dữ liệu: {file_path}")

    df = pd.read_csv(file_path)
    return df


def preview_data(df, rows=5):
    """
    Hiển thị một số dòng đầu của dữ liệu

    :param df: DataFrame
    :param rows: số dòng muốn hiển thị
    """
    print(f"\nHiển thị {rows} dòng đầu tiên của dữ liệu:")
    print(df.head(rows))


def show_basic_info(df):
    """
    Hiển thị thông tin cơ bản của tập dữ liệu:
    - Số dòng, số cột
    - Kiểu dữ liệu
    - Thống kê mô tả
    """
    print("\nKích thước dữ liệu (rows, columns):")
    print(df.shape)

    print("\nThông tin chi tiết các cột:")
    df.info()

    print("\nThống kê mô tả các thuộc tính số:")
    print(df.describe())
