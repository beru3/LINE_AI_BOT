
import os
import logging
import sqlite3
from flask import Flask, request, abort
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ログ設定
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                                                logging.FileHandler("log/app.log"),
                        logging.StreamHandler()
                    ])

# 環境変数と定数
CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
DB_PATH = 'occupations.db'

# LINE Bot APIの設定
configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

def search_occupations(query):
    """データベースから職業名を検索する"""
    results = []
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            # occupation_nameから部分一致で検索
            search_query = f"%{query}%"
            cursor.execute("SELECT occupation_name FROM occupations WHERE occupation_name LIKE ?", (search_query,))
            results = [row[0] for row in cursor.fetchall()]
            logging.info(f"Found {len(results)} occupations for query: '{query}'" )
    except Exception as e:
        logging.error(f"Database search error: {e}")
    return results

@app.route("/callback", methods=['POST'])
def callback():
    """Webhookからのリクエストを処理する"""
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    logging.info(f"Request body: {body}")
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        logging.error("Invalid signature. Please check your channel secret.")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    """テキストメッセージを受信したときの処理"""
    user_text = event.message.text
    logging.info(f"Received message: {user_text} from user: {event.source.user_id}")

    # 職業を検索
    search_results = search_occupations(user_text)

    # 返信メッセージを作成
    if search_results:
        reply_text = "関連する職業が見つかりました：\n" + "\n".join(search_results[:5]) # 最大5件表示
        if len(search_results) > 5:
            reply_text += f"\n...他{len(search_results) - 5}件"
    else:
        reply_text = f"「{user_text}」に一致する職業は見つかりませんでした。"

    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        try:
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=reply_text)]
                )
            )
            logging.info(f"Replied to user: {event.source.user_id}")
        except Exception as e:
            logging.error(f"Error replying to message: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
