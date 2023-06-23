import pandas as pd
# Đọc và lưu trong dataFrame
df = pd.read_csv("day9/addresses.csv")

full_name = df[['firstName','lastName']]
print(full_name)