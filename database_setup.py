
import pandas as pd
import sqlite3
import logging

# ログ設定
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("database_setup.log"),
                        logging.StreamHandler()
                    ])

DB_PATH = 'occupations.db'
OCCUPATIONS_CSV_PATH = 'occupation_data.csv'

def create_tables(conn):
    """データベースにテーブルを作成する"""
    cursor = conn.cursor()
    # occupations テーブル
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS occupations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_row_id INTEGER NOT NULL UNIQUE, -- 元CSVの行番号
        occupation_name TEXT NOT NULL,
        occupation_code TEXT -- 職業コードは後で特定・更新する
    );
    ''')
    # 他のテーブル（skills, knowledge, tasks）も同様に作成（今回は省略）
    logging.info("'occupations' table created successfully.")
    conn.commit()

def insert_occupations(conn, df):
    """occupationsテーブルにデータを挿入する"""
    cursor = conn.cursor()
    logging.info(f"Inserting data into 'occupations' table...")
    
    # ヘッダーが複雑なため、データ部分のみを処理対象とする
    # 最初の列を data_row_id, 2番目の列を occupation_name として挿入
    # データの開始行を正しく特定する必要がある
    # df.iloc[1:] はデータが2行目から始まると仮定
    for index, row in df.iterrows():
        try:
            # 1列目(職業番号)と2列目(職業名)を想定
            data_row_id = int(row.iloc[0])
            occupation_name = row.iloc[1]
            
            # データが存在する場合のみ挿入
            if pd.notna(data_row_id) and pd.notna(occupation_name):
                cursor.execute("INSERT INTO occupations (data_row_id, occupation_name) VALUES (?, ?)",
                               (data_row_id, str(occupation_name)))
        except (ValueError, IndexError) as e:
            logging.warning(f"Skipping row {index} due to data conversion error: {e} - Row content: {row}")
            continue

    conn.commit()
    logging.info(f"{cursor.rowcount} records inserted into 'occupations' table.")

def main():
    """メイン処理"""
    try:
        df = pd.read_csv(OCCUPATIONS_CSV_PATH, encoding='utf-8-sig', header=None, skiprows=1) # ヘッダーをスキップ
        with sqlite3.connect(DB_PATH) as conn:
            create_tables(conn)
            insert_occupations(conn, df)
    except FileNotFoundError:
        logging.error(f"CSV file not found at {OCCUPATIONS_CSV_PATH}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
