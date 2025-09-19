
import pandas as pd
import os
import logging

# ログ設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DATA_DIR = 'data'
files_to_inspect = ['numeric_data.csv', 'description_data.csv', 'column_definitions.csv']

def inspect_csv_files():
    """指定されたCSVファイルの先頭5行を読み込んで表示する"""
    if not os.path.exists(DATA_DIR):
        logging.error(f"Directory not found: {DATA_DIR}")
        return

    for filename in files_to_inspect:
        path = os.path.join(DATA_DIR, filename)
        try:
            logging.info(f"--- Reading head of {path} ---")
            df = pd.read_csv(path, encoding='utf-8-sig')
            print(f"\n--- Contents of {filename} ---")
            print(df.head())
            print("\n")
        except FileNotFoundError:
            logging.error(f"File not found: {path}")
        except Exception as e:
            logging.error(f"An error occurred while reading {path}: {e}")

if __name__ == "__main__":
    inspect_csv_files()
