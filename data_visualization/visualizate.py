import matplotlib.pyplot as plt


def plot_score_distribution(df):
    """
    Vẽ biểu đồ histogram phân bố điểm các môn
    """
    plt.figure()
    plt.hist(df['math_score'], bins=10, alpha=0.7, label='Math')
    plt.hist(df['reading_score'], bins=10, alpha=0.7, label='Reading')
    plt.hist(df['writing_score'], bins=10, alpha=0.7, label='Writing')

    plt.title("Phân bố điểm các môn học")
    plt.xlabel("Điểm số")
    plt.ylabel("Số lượng sinh viên")
    plt.legend()
    plt.show()


def plot_gender_distribution(df):
    """
    Vẽ biểu đồ cột thể hiện số lượng sinh viên theo giới tính
    """
    gender_counts = df['gender'].value_counts()

    plt.figure()
    plt.bar(gender_counts.index, gender_counts.values)
    plt.title("Phân bố sinh viên theo giới tính")
    plt.xlabel("Giới tính")
    plt.ylabel("Số lượng")
    plt.show()


def plot_parent_education(df):
    """
    Vẽ biểu đồ cột thể hiện trình độ học vấn của phụ huynh
    """
    edu_counts = df['parental_level_of_education'].value_counts()

    plt.figure()
    plt.barh(edu_counts.index, edu_counts.values)
    plt.title("Trình độ học vấn của phụ huynh")
    plt.xlabel("Số lượng sinh viên")
    plt.ylabel("Trình độ học vấn")
    plt.show()


def plot_math_vs_reading(df):
    """
    Vẽ biểu đồ scatter thể hiện mối quan hệ giữa điểm Toán và Đọc
    """
    plt.figure()
    plt.scatter(df['math_score'], df['reading_score'])
    plt.title("Mối quan hệ giữa điểm Toán và Đọc")
    plt.xlabel("Điểm Toán")
    plt.ylabel("Điểm Đọc")
    plt.show()
