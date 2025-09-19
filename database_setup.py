
import pandas as pd
import sqlite3
import logging
import os

# ログ設定
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("database_setup.log"),
                        logging.StreamHandler()
                    ])

# --- 定数定義 ---
DB_PATH = 'occupations.db'
DATA_DIR = 'data'
NUMERIC_CSV = os.path.join(DATA_DIR, 'numeric_data.csv')
DESCRIPTION_CSV = os.path.join(DATA_DIR, 'description_data.csv')
DEFINITIONS_CSV = os.path.join(DATA_DIR, 'column_definitions.csv')

NUMERIC_SOURCE_FILE = 'IPD_DL_numeric_6_01.xlsx'
DESCRIPTION_SOURCE_FILE = 'IPD_DL_description_6_00_06.xlsx'


def create_tables(conn):
    """データベースにテーブルを作成する"""
    cursor = conn.cursor()
    logging.info("Creating database tables...")

    # occupations テーブル
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS occupations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        occupation_code TEXT NOT NULL UNIQUE, -- 職業コード
        occupation_name TEXT NOT NULL,
        source_file TEXT
    );
    ''')

    # skills テーブル
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        occupation_id INTEGER NOT NULL,
        skill_name TEXT NOT NULL,
        skill_score REAL NOT NULL,
        source_file TEXT,
        FOREIGN KEY (occupation_id) REFERENCES occupations(id)
    );
    ''')

    # knowledge テーブル
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS knowledge (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        occupation_id INTEGER NOT NULL,
        knowledge_name TEXT NOT NULL,
        knowledge_score REAL NOT NULL,
        source_file TEXT,
        FOREIGN KEY (occupation_id) REFERENCES occupations(id)
    );
    ''')

    # tasks テーブル
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        occupation_id INTEGER NOT NULL,
        task_description TEXT NOT NULL,
        source_file TEXT,
        FOREIGN KEY (occupation_id) REFERENCES occupations(id)
    );
    ''')

    conn.commit()
    logging.info("Tables created successfully.")

def get_column_definitions():
    """インプットデータ細目から列定義を読み込む"""
    try:
        df_def = pd.read_csv(DEFINITIONS_CSV, header=3, encoding='utf-8-sig')
        df_def.columns = ['_1', 'large_area', 'medium_area', 'small_area', 'version_mgmt', 'ipd_id', 'item_name', 'data_format', 'length_range', 'description', 'notes']
        
        # 正確な領域名でフィルタリング
        skill_cols = df_def[df_def['large_area'] == '０４　数値プロフィール領域'][df_def['medium_area'] == 'スキル']['ipd_id'].tolist()
        knowledge_cols = df_def[df_def['large_area'] == '０４　数値プロフィール領域'][df_def['medium_area'] == '知識']['ipd_id'].tolist()
        task_cols = df_def[df_def['large_area'] == '０５　タスク領域']['ipd_id'].tolist()
        
        code_to_name = pd.Series(df_def.item_name.values, index=df_def.ipd_id).to_dict()

        logging.info(f"Loaded {len(skill_cols)} skill columns, {len(knowledge_cols)} knowledge columns, {len(task_cols)} task columns.")
        return skill_cols, knowledge_cols, task_cols, code_to_name
    except Exception as e:
        logging.error(f"Failed to read or parse column definitions: {e}", exc_info=True)
        return None, None, None, None

def main():
    """メイン処理"""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        logging.info(f"Removed existing database file: {DB_PATH}")

    skill_cols, knowledge_cols, task_cols, code_to_name = get_column_definitions()
    if not all([code_to_name]) or not (skill_cols or knowledge_cols or task_cols):
        logging.error("Could not proceed without column definitions.")
        return

    try:
        with sqlite3.connect(DB_PATH) as conn:
            create_tables(conn)
            cursor = conn.cursor()

            # 数値データの処理
            logging.info(f"Processing {NUMERIC_CSV}...")
            df_numeric = pd.read_csv(NUMERIC_CSV, header=17, encoding='utf-8-sig')
            
            # 職業コードと職業名が格納されている列を特定
            occ_code_col = df_numeric.columns[0]
            occ_name_col = df_numeric.columns[1]

            for _, row in df_numeric.iterrows():
                occ_code = row[occ_code_col]
                occ_name = row[occ_name_col]
                if pd.isna(occ_code) or pd.isna(occ_name):
                    continue

                # occupations テーブルへの挿入
                cursor.execute("INSERT OR IGNORE INTO occupations (occupation_code, occupation_name, source_file) VALUES (?, ?, ?)", 
                               (str(occ_code), str(occ_name), NUMERIC_SOURCE_FILE))
                cursor.execute("SELECT id FROM occupations WHERE occupation_code = ?", (str(occ_code),))
                occupation_id = cursor.fetchone()[0]

                # skills テーブルへの挿入
                for col in skill_cols:
                    if col in row and pd.notna(row[col]):
                        cursor.execute("INSERT INTO skills (occupation_id, skill_name, skill_score, source_file) VALUES (?, ?, ?, ?)",
                                       (occupation_id, code_to_name.get(col, col), row[col], NUMERIC_SOURCE_FILE))
                
                # knowledge テーブルへの挿入
                for col in knowledge_cols:
                    if col in row and pd.notna(row[col]):
                        cursor.execute("INSERT INTO knowledge (occupation_id, knowledge_name, knowledge_score, source_file) VALUES (?, ?, ?, ?)",
                                       (occupation_id, code_to_name.get(col, col), row[col], NUMERIC_SOURCE_FILE))
            conn.commit()
            logging.info("Finished processing numeric data.")

            # 解説系データの処理
            logging.info(f"Processing {DESCRIPTION_CSV}...")
            df_desc = pd.read_csv(DESCRIPTION_CSV, header=17, encoding='utf-8-sig')
            occ_code_col_desc = df_desc.columns[0]

            for _, row in df_desc.iterrows():
                occ_code = row[occ_code_col_desc]
                if pd.isna(occ_code):
                    continue
                
                cursor.execute("SELECT id FROM occupations WHERE occupation_code = ?", (str(occ_code),))
                result = cursor.fetchone()
                if not result:
                    continue
                occupation_id = result[0]

                # tasks テーブルへの挿入
                for col in task_cols:
                    if col in row and pd.notna(row[col]):
                        cursor.execute("INSERT INTO tasks (occupation_id, task_description, source_file) VALUES (?, ?, ?)",
                                       (occupation_id, row[col], DESCRIPTION_SOURCE_FILE))
            conn.commit()
            logging.info("Finished processing description data.")

    except Exception as e:
        logging.error(f"An error occurred during database setup: {e}", exc_info=True)

if __name__ == "__main__":
    main()
