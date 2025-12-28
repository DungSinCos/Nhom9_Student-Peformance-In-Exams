import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def remove_duplicates(df):
    """
    Loại bỏ các dòng dữ liệu trùng lặp
    """
    original_rows = df.shape[0]
    df = df.drop_duplicates()
    removed_rows = original_rows - df.shape[0]
    print(f"Đã loại bỏ {removed_rows} dòng dữ liệu trùng lặp")
    return df


def handle_missing_values(df):
    """
    Xử lý dữ liệu thiếu:
    - Với cột số: thay thế bằng giá trị trung bình
    - Với cột dạng chuỗi: thay thế bằng giá trị xuất hiện nhiều nhất
    """
    for column in df.columns:
        if df[column].isnull().sum() > 0:
            if pd.api.types.is_numeric_dtype(df[column]):
                mean_value = df[column].mean()
                df[column] = df[column].fillna(mean_value)
            else:
                mode_value = df[column].mode()[0]
                df[column] = df[column].fillna(mode_value)

    print("Đã xử lý xong các giá trị thiếu")
    return df


def normalize_numeric_columns(df, columns):
    """
    Chuẩn hóa các cột dữ liệu số về khoảng [0,1]
    """
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    print(f"Đã chuẩn hóa các cột: {columns}")
    return df


def clean_data(df):
    """
    Hàm tổng hợp thực hiện toàn bộ quá trình làm sạch dữ liệu
    """
    print("Bắt đầu quá trình làm sạch dữ liệu...")
    df = remove_duplicates(df)
    df = handle_missing_values(df)
    print("Hoàn tất quá trình làm sạch dữ liệu!")
    return df
def standardize_column_names(df):
    """
    Chuẩn hóa tên cột: lowercase + thay khoảng trắng bằng _
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )
    return df
