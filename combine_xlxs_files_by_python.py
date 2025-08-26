import pandas as pd
import glob
import os

folder_path = r"C:\Users\Admin\OneDrive\Documents\goldie_data"

file_list = glob.glob(os.path.join(folder_path, "*.xlsx"))

df_list = []

for file in file_list:
    print(f"Đang xử lý: {file}")
    df = pd.read_excel(file)
    df_list.append(df)

merged_df = pd.concat(df_list, ignore_index=True)

output_path = os.path.join(folder_path, "combined_shopee_data_04_2023_04_2025.xlsx")
merged_df.to_excel(output_path, index=False)

print("Done")
