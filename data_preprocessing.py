
import pandas as pd
import logging

# ログ設定
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("data_preprocessing.log"),
                        logging.StreamHandler()
                    ])

# ファイルパス
input_csv_path = 'IPD_DL_numeric_6_01.csv'
output_csv_path = 'occupation_data.csv'

def preprocess_data():
    """
    Shift-JISでエンコードされたCSVファイルを読み込み、
    UTF-8で保存し直す。
    """
    try:
        logging.info(f"Reading CSV file: {input_csv_path} with encoding 'shift-jis'...")
        # Shift-JISでCSVを読み込む。ヘッダーは18行目（0-indexedで17）にあり、データは20行目から。
        df = pd.read_csv(input_csv_path, encoding='shift-jis', header=17)

        logging.info("Successfully loaded the data. Displaying first 5 rows:")
        print(df.head())

        # UTF-8で新しいCSVファイルに保存
        df.to_csv(output_csv_path, index=False, encoding='utf-8-sig')
        logging.info(f"Successfully converted and saved the data to {output_csv_path} in UTF-8 format.")

    except FileNotFoundError:
        logging.error(f"Error: The file {input_csv_path} was not found.")
    except UnicodeDecodeError:
        logging.error(f"Error: The file {input_csv_path} could not be decoded with 'shift-jis'. Please check the file encoding.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    preprocess_data()
