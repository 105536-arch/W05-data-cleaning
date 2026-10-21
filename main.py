
import pandas as pd

# 讀取原始資料
df = pd.read_csv("messy_students.csv")

# 查看資料基本資訊
print("原始資料：")
print(df.head())

print("\n資料資訊：")
df.info()

print("\n缺失值數量：")
print(df.isna().sum())

print("\n重複資料數量：")
print(df.duplicated().sum())

# 清理重複資料
df = df.drop_duplicates(subset=["name", "math", "english"])

# 清除姓名前後空白
df["name"] = df["name"].str.strip().str.strip('"').str.strip()

# 將成績轉換成數字，無法轉換的內容變成 NaN

# 將成績轉換成數字
df["math"] = pd.to_numeric(df["math"], errors="coerce")
df["english"] = pd.to_numeric(df["english"], errors="coerce")

# 將不合理的成績設為缺失值
df.loc[~df["math"].between(0, 100), "math"] = float("nan")
df.loc[~df["english"].between(0, 100), "english"] = float("nan")

# 填補缺失值：使用各科平均
df["math"] = df["math"].fillna(df["math"].mean())
df["english"] = df["english"].fillna(df["english"].mean())# 使用各科平均分數填補缺失值，避免刪除學生資料，
# 也能讓缺失的成績有合理的數值可供後續分析。
df["math"] = df["math"].fillna(df["math"].mean())
df["english"] = df["english"].fillna(df["english"].mean())

# 查看清理後的資料
print("\n清理後的資料：")
print(df)

print("\n清理後的重複資料數量：")
print(df.duplicated(subset=["name", "math", "english"]).sum())
# 匯出清理後的資料
df.to_csv("cleaned_students.csv", index=False)
# 比較清理前後的資料
print("\n清理後的資料筆數：", df.shape)
print("\n清理後的統計資料：")
print(df.describe())
print("\n清理完成！已輸出 cleaned_students.csv")