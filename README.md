# 企業情報取得アプリ

このプロジェクトは、企業名を入力すると、その企業の情報を取得して表示するデスクトップアプリケーションです。CustomTkinterを使用してGUIを構築し、OpenAIのAPIを利用して企業情報を取得します。

## 主な機能
- 企業名を入力して情報を取得
- 取得した情報をマークダウン形式で表示
- 非同期処理によるスムーズな操作

## 必要条件
- Python 3.10以上
- OpenAI APIキー

## セットアップ
1. 必要なライブラリをインストールします。

   ```bash
   pip install customtkinter openai python-dotenv
   ```

2. `.env`ファイルを作成し、OpenAI APIキーを設定します。

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. アプリケーションを実行します。

   ```bash
   python main.py
   ```

## ファイル構成
- `main.py`: アプリケーションのエントリーポイント。
- `gpt_client.py`: OpenAI APIを使用して企業情報を取得するモジュール。
- `README.md`: プロジェクトの概要とセットアップ手順。
- `youken.md`: 要件や仕様に関するドキュメント。

## 使用方法
1. アプリケーションを起動します。
2. 企業名を入力し、「情報を取得」ボタンをクリックします。
3. 取得した情報が画面に表示されます。

## 注意事項
- OpenAI APIキーが必要です。
- 取得する情報は正確性を保証するものではありません。

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。