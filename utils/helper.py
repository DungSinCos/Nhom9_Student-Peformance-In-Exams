import os


def print_separator(title=None):
    """
    In đường phân cách để chương trình dễ nhìn hơn
    """
    print("\n" + "=" * 50)
    if title:
        print(title)
        print("-" * 50)


def print_basic_statistics(df):
    """
    In thống kê cơ bản của dữ liệu
    """
    print("Thống kê cơ bản các thuộc tính số:")
    print(df.describe())


def missing_values_report(df):
    """
    Báo cáo số lượng giá trị thiếu của từng cột
    """
    print("Báo cáo giá trị thiếu:")
    missing = df.isnull().sum()
    print(missing)
    return missing


def save_dataframe_to_csv(df, output_path):
    """
    Lưu DataFrame ra file CSV
    """
    directory = os.path.dirname(output_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    df.to_csv(output_path, index=False)
    print(f"Dữ liệu đã được lưu tại: {output_path}")


def normalize_text_column(df, column_name):
    """
    Chuẩn hóa chuỗi: loại bỏ khoảng trắng, chuyển về chữ thường
    """
    if column_name in df.columns:
        df[column_name] = df[column_name].astype(str).str.strip().str.lower()
        print(f"Đã chuẩn hóa chuỗi cho cột: {column_name}")
    return df
