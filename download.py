import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def download_data():
    df = pd.read_csv("https://raw.githubusercontent.com/Veniashvilly/dtset/refs/heads/main/Car_sales.csv")
    return df

def clear_data():
    df = download_data()

    # Оставим только нужные колонки и удалим строки с пропущенными значениями
    df = df[[
        'Manufacturer', 'Model', 'Vehicle_type',
        'Sales_in_thousands', 'Engine_size', 'Horsepower',
        'Curb_weight', 'Fuel_efficiency', 'Price_in_thousands'
    ]].dropna().reset_index(drop=True)

    # Закодируем категориальные признаки
    cat_columns = ['Manufacturer', 'Model', 'Vehicle_type']
    encoder = OrdinalEncoder()
    df[cat_columns] = encoder.fit_transform(df[cat_columns])


    df.to_csv("df_clear.csv", index=False)

if __name__ == "__main__":
    clear_data()
