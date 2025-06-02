import pandas as pd

file_path = 'KaggleV2-May-2016.csv'
df = pd.read_csv(file_path)

print("\n ==== Dataset Loaded Successfully! ====\n")
print(" Basic Dataset Information:")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")
print("\n Column Names:")
print(list(df.columns))
print("\n Sample Data Preview (first 5 rows):")
print(df.head())
print("\n Checking for Missing Values:")

missing = df.isnull().sum()
print(missing[missing > 0] if any(missing > 0) else " No missing values found!")

num_duplicates = df.duplicated().sum()
print(f"\n Number of Duplicate Rows: {num_duplicates}")

df_cleaned = df.drop_duplicates()
print(f" Shape after Removing Duplicates: {df_cleaned.shape}")

df_cleaned['ScheduledDay'] = pd.to_datetime(df_cleaned['ScheduledDay'])
df_cleaned['AppointmentDay'] = pd.to_datetime(df_cleaned['AppointmentDay'])
print("\n Date columns converted to datetime!")

df_cleaned['No-show'] = df_cleaned['No-show'].str.strip().str.lower()
print("\n 'No-show' column cleaned (lowercase)")

binary_cols = ['Scholarship', 'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received']
print("\n Unique Values in Binary Columns:")
for col in binary_cols:
    print(f" - {col}: {df_cleaned[col].unique()}")

output_file_all = 'Final Output appointments_cleaned.csv'
df_cleaned.to_csv(output_file_all, index=False)
print(f"\n All cleaned data saved as **'{output_file_all}'** with headers!")


no_show_df = df_cleaned[df_cleaned['No-show'] == 'yes']
output_file_no_show = 'Final Output no_show_only.csv'
no_show_df.to_csv(output_file_no_show, index=False)
print(f"\n Only No-show records saved as **'{output_file_no_show}'** with headers!")

print("\n ==== Data Cleaning and No-show Extraction Completed Successfully! ====\n")
