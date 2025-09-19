import os
import logging
import sqlite3
import openai
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
log_dir = 'log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(log_dir, "app.log")),
                        logging.StreamHandler()
                    ])

# 環境変数と定数
CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DB_PATH = 'occupations.db'

# APIクライアントの設定
configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
openai.api_key = OPENAI_API_KEY
handler = WebhookHandler(CHANNEL_SECRET)

def search_occupations(query):
    """データベースから職業名を検索する"""
    results = []
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            search_query = f"%{query}%"
            cursor.execute("SELECT occupation_name FROM occupations WHERE occupation_name LIKE ?", (search_query,))
            results = [row[0] for row in cursor.fetchall()]
            logging.info(f"Found {len(results)} occupations for query: '{query}'" )
    except Exception as e:
        logging.error(f"Database search error: {e}")
    return results

def generate_ai_response(user_query, search_results):
    """OpenAI APIを使用して、検索結果を元に応答を生成する"""
    logging.info("Generating AI response...")
    try:
        system_prompt = """
あなたは政府公式職業データベースのデータに精通した、経験豊富な生成AIコンサルタントです。
ユーザーから企業の事業内容に関する質問を受けたら、関連する職種リストを提示し、どのような業務でAIを活用できるか提案してください。

【重要な原則】
- データベースから取得した職種リストに完全に基づいて回答してください。
- 専門用語を避け、誰にでも分かりやすい平易な言葉で説明してください。
- 親しみやすく、丁寧な口調で回答してください。
"""

        prompt = f"""
【事業内容】
{user_query}

【関連職種リスト】
{', '.join(search_results)}

上記の事業内容と関連職種リストを基に、どのような職種が存在し、それぞれの職種で生成AIをどのように活用できる可能性があるか、具体的な業務を挙げて解説してください。
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        ai_message = response.choices[0].message['content'].strip()
        logging.info("Successfully generated AI response.")
        return ai_message

    except Exception as e:
        logging.error(f"Error generating AI response: {e}")
        return "申し訳ありません、AIの応答生成中にエラーが発生しました。"

@app.route("/callback", methods=['POST'])
def callback():
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
    user_text = event.message.text
    logging.info(f"Received message: {user_text} from user: {event.source.user_id}")

    search_results = search_occupations(user_text)

    if search_results:
        # AI 응답 생성
        reply_text = generate_ai_response(user_text, search_results)
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