import pandas as pd
import logging
import os

# ログ設定
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("data_preprocessing.log"),
                        logging.StreamHandler()
                    ])

# 入力と出力のパス設定
INPUT_DIR = 'input'
OUTPUT_DIR = 'data'

FILES_SHEETS_MAP = {
    'IPD_DL_numeric_6_01.xlsx': {
        'IPD形式': 'numeric_data.csv',
        'インプットデータ細目': 'column_definitions.csv'
    },
    'IPD_DL_description_6_00_06.xlsx': {
        '解説系': 'description_data.csv'
    }
}

def preprocess_excel_to_csv():
    """
    Excelファイルの指定されたシートを読み込み、
    それぞれをUTF-8エンコーディングのCSVファイルとして保存する。
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        logging.info(f"Created output directory: {OUTPUT_DIR}")

    for excel_file, sheets in FILES_SHEETS_MAP.items():
        input_path = os.path.join(INPUT_DIR, excel_file)
        try:
            xls = pd.ExcelFile(input_path)
            logging.info(f"Successfully opened {input_path}")

            for sheet_name, output_csv in sheets.items():
                output_path = os.path.join(OUTPUT_DIR, output_csv)
                try:
                    logging.info(f"Reading sheet '{sheet_name}'...")
                    # シートを読み込む。ヘッダーは18行目（0-indexedで17）にあると仮定。
                    # ファイルによってヘッダーの位置が違う可能性も考慮し、まずはヘッダーなしで読み込む
                    df = pd.read_excel(xls, sheet_name=sheet_name, header=None)
                    
                    # 実際のデータ構造に合わせてヘッダーと開始行を調整する必要があるが、
                    # まずはそのままCSVに変換してみる
                    df.to_csv(output_path, index=False, encoding='utf-8-sig')
                    logging.info(f"Successfully saved sheet '{sheet_name}' to {output_path}")

                except Exception as e:
                    logging.error(f"Could not process sheet '{sheet_name}' in {excel_file}. Error: {e}")

        except FileNotFoundError:
            logging.error(f"File not found: {input_path}")
        except Exception as e:
            logging.error(f"An error occurred while processing {excel_file}: {e}")

if __name__ == "__main__":
    preprocess_excel_to_csv()