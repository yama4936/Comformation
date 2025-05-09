import os
import json
import openai
import re
from dotenv import load_dotenv

load_dotenv()

# APIキーの取得
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEYが設定されていません。環境変数を確認してください。")

openai.api_key = api_key

def fetch_company_info(company_name: str) -> str:
    prompt = f"""
あなたは企業情報を収集して構造化JSONとして出力する専門AIです。
以下のフォーマットに従って、企業「{company_name}」の情報を可能な限り埋めてください。

たとえ正確でない可能性があっても、**予想される情報を埋めてください**。
不明な箇所には「情報が見つかりませんでした」と記載してください。

必ず、**以下と同じ構造のJSONを```jsonで囲んだコードブロック内にのみ**出力してください。
前置きや説明、謝罪文は一切不要です。

# 出力形式の例（※出力時もこの構造をそのまま使用）:
```json
{{
  "基本情報": {{
    "正式名称": "株式会社サンプル",
    "設立年": "1985年",
    "所在地": "東京都港区芝公園",
    "代表者": "山田 太郎",
    "資本金": "1億円",
    "従業員数": "500名",
    "売上高": "100億円"
  }},
  "事業内容": [
    "精密機器の製造販売",
    "金属加工部品の輸出"
  ],
  "初任給": {{
    "大学院修了": "25万円",
    "大学卒": "23万円",
    "高専・短大・専門卒": "20万円"
  }},
  "働き方と福利厚生": {{
    "フレックスタイム制": "あり",
    "年間休日": "120日",
    "休暇制度": "年末年始、夏季休暇、有給休暇",
    "福利厚生": "社会保険完備、家賃補助、資格取得支援",
    "育児・介護支援": "育児休暇制度あり、介護休業制度あり"
  }},
  "企業の簡単な説明": [
    "再生可能エネルギーの利用促進",
    "女性管理職比率の向上"
  ]
}}
"""

    try:
        response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=1000
    )
        print("[DEBUG] APIレスポンス:", response)  # デバッグ用にレスポンスを出力
        content = response['choices'][0]['message']['content'].strip()
        print("[DEBUG] content:", content)  # デバッグ用にcontentを出力

        # JSON部分を抽出
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_match:
            json_content = json_match.group()
            return json.loads(json_content)
        else:
            print("[ERROR] JSON部分が見つかりませんでした。")
            return {"error": "公開されていない情報が含まれています。"}

    except json.JSONDecodeError as json_error:
        print(f"[ERROR] JSON解析失敗: {json_error}")
        return {"error": "JSON解析に失敗しました。"}
    except openai.OpenAIError as e:
        print(f"[ERROR] API呼び出し失敗: {e}")
        return {"error": "API呼び出しに失敗しました。"}
