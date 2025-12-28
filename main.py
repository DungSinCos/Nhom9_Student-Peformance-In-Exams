from data_loader.load_data import load_data, preview_data, show_basic_info
from data_cleaning.clean_data import (
    clean_data,
    normalize_numeric_columns,
    standardize_column_names
)
from visualization.visualize import (
    plot_score_distribution,
    plot_gender_distribution,
    plot_parent_education,
    plot_math_vs_reading
)
from utils.helpers import (
    print_separator,
    missing_values_report,
    save_dataframe_to_csv
)

def visualization_menu(df):
    while True:
        print("\n---- MENU TRỰC QUAN HÓA DỮ LIỆU ----")
        print("1. Phân phối điểm các môn")
        print("2. Phân bố giới tính")
        print("3. Trình độ học vấn của phụ huynh")
        print("4. Tương quan điểm Toán và Đọc")
        print("0. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            plot_score_distribution(df)
        elif choice == "2":
            plot_gender_distribution(df)
        elif choice == "3":
            plot_parent_education(df)
        elif choice == "4":
            plot_math_vs_reading(df)
        elif choice == "0":
            print("Thoát menu trực quan hóa.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

def main():
    # BƯỚC 1: ĐỌC DỮ LIỆU
    print_separator("BƯỚC 1: ĐỌC DỮ LIỆU")
    data_path = "data/student.csv"
    df = load_data(data_path)

    # BƯỚC 2: CHUẨN HÓA TÊN CỘT
    df = standardize_column_names(df)

    # BƯỚC 3: XEM TRƯỚC & THÔNG TIN DỮ LIỆU
    print_separator("BƯỚC 2: THÔNG TIN DỮ LIỆU")
    preview_data(df)
    show_basic_info(df)

    # BƯỚC 4: KIỂM TRA GIÁ TRỊ THIẾU
    print_separator("BƯỚC 3: KIỂM TRA GIÁ TRỊ THIẾU")
    missing_values_report(df)

    # BƯỚC 5: LÀM SẠCH DỮ LIỆU
    print_separator("BƯỚC 4: LÀM SẠCH DỮ LIỆU")
    df = clean_data(df)

    # BƯỚC 6: CHUẨN HÓA DỮ LIỆU SỐ
    print_separator("BƯỚC 5: CHUẨN HÓA DỮ LIỆU")
    score_columns = ['math_score', 'reading_score', 'writing_score']
    df = normalize_numeric_columns(df, score_columns)

    # BƯỚC 7: LƯU DỮ LIỆU SAU XỬ LÝ
    print_separator("BƯỚC 6: LƯU DỮ LIỆU")
    save_dataframe_to_csv(df, "output/cleaned_student.csv")

    # BƯỚC 8: TRỰC QUAN HÓA DỮ LIỆU
    print_separator("BƯỚC 7: TRỰC QUAN HÓA DỮ LIỆU")
    visualization_menu(df)

    print_separator("HOÀN THÀNH CHƯƠNG TRÌNH")


if __name__ == "__main__":
    main()
