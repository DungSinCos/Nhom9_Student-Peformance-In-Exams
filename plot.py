#đồ thị
def plot_histograms(df: pd.DataFrame, out_dir: Path) -> None:
    score_cols = [c for c in ["math_score", "reading_score", "writing_score", "average_score"] if c in df.columns]
    if not score_cols:
        return
    for c in score_cols:
        plt.figure()
        plt.hist(df[c].dropna().values, bins=20)
        plt.title(f"Histogram - {c}")
        plt.xlabel(c)
        plt.ylabel("count")
        plt.tight_layout()
        plt.savefig(out_dir / f"hist_{c}.png", dpi=200)
        plt.close()


def plot_box_by_category(df: pd.DataFrame, cat_col: str, out_dir: Path) -> None:
    score_cols = [c for c in ["math_score", "reading_score", "writing_score", "average_score"] if c in df.columns]
    if cat_col not in df.columns or not score_cols:
        return

    categories = sorted(list(df[cat_col].dropna().unique()))
    if len(categories) > 12:
        categories = categories[:12]

    for score in score_cols:
        data = [df.loc[df[cat_col] == k, score].dropna().values for k in categories]
        plt.figure(figsize=(max(6, len(categories) * 0.7), 5))
        plt.boxplot(data, labels=categories, vert=True)
        plt.title(f"Boxplot - {score} theo {cat_col}")
        plt.xlabel(cat_col)
        plt.ylabel(score)
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.savefig(out_dir / f"box_{score}_by_{cat_col}.png", dpi=200)
        plt.close()


def plot_category_counts(df: pd.DataFrame, cat_col: str, out_dir: Path) -> None:
    if cat_col not in df.columns:
        return
    vc = df[cat_col].value_counts().head(15)
    plt.figure(figsize=(8, 4))
    plt.bar(vc.index.astype(str), vc.values)
    plt.title(f"Số lượng theo {cat_col} (top 15)")
    plt.xlabel(cat_col)
    plt.ylabel("count")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / f"count_{cat_col}.png", dpi=200)
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame, out_dir: Path) -> None:
    num_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    if len(num_cols) < 2:
        return
    corr = df[num_cols].corr(numeric_only=True)

    plt.figure(figsize=(7, 6))
    plt.imshow(corr.values, aspect="auto")
    plt.title("Correlation heatmap (numeric)")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
    plt.yticks(range(len(corr.index)), corr.index)
    plt.tight_layout()
    plt.savefig(out_dir / "corr_heatmap.png", dpi=200)
    plt.close()

def visualize_all(df: pd.DataFrame, out_dir: Path) -> None:
    _safe_mkdir(out_dir)
    plot_histograms(df, out_dir)
    plot_correlation_heatmap(df, out_dir)

    for cat_col in ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"]:
        if cat_col in df.columns:
            plot_category_counts(df, cat_col, out_dir)
            plot_box_by_category(df, cat_col, out_dir)

    print(f"Đã lưu hình vào: {out_dir.resolve()}")
