
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DEFINITIONS_CSV = 'data/column_definitions.csv'

def inspect_definitions():
    try:
        df_def = pd.read_csv(DEFINITIONS_CSV, header=3, encoding='utf-8-sig')
        # 列名を一時的に設定
        df_def.columns = [f'col_{i}' for i in range(len(df_def.columns))]
        
        # 「大領域」に相当する列（2列目、インデックス1）のユニークな値を表示
        logging.info("Unique values in 'large_area' column:")
        print(df_def['col_1'].unique())

    except Exception as e:
        logging.error(f"Failed to inspect column definitions: {e}")

if __name__ == "__main__":
    inspect_definitions()
