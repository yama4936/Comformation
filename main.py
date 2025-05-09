import customtkinter as ctk
from gpt_client import fetch_company_info
import threading
import json

def main():
    def get_company_info():
        company_name = entry.get().strip()
        if not company_name:
            result_label.configure(text="企業名を入力してください。", text_color="red")
            return

        # 待機画面の表示
        result_label.configure(text=f"{company_name} の情報を取得中...\n5秒程お待ちください。", text_color="white")

        def fetch_info():
            info = fetch_company_info(company_name)
            result_box.configure(state="normal")
            result_box.delete("1.0", "end")

            if "error" in info:
                result_box.insert("end", info["error"])
            else:
                # マークダウン形式で整形して表示
                formatted = "\n".join([
                    f"- **{key}**:\n  " + "\n  ".join([f"- {sub_key}: {sub_value}" for sub_key, sub_value in value.items()]) if isinstance(value, dict) else \
                    f"- **{key}**:\n  " + "\n  ".join([f"- {item}" for item in value]) if isinstance(value, list) else \
                    f"- **{key}**: {value}"
                    for key, value in info.items()
                ])
                result_box.insert("end", formatted)

            result_box.configure(state="disabled")

            # 情報取得後に表示を更新
            result_label.configure(text=f"{company_name} の情報を取得しました。", text_color="green")

        # 別スレッドで情報を取得
        threading.Thread(target=fetch_info).start()

    # GUIのセットアップ
    ctk.set_appearance_mode("System")  # 外観モードをシステムに合わせる
    ctk.set_default_color_theme("blue")  # カラーテーマを設定

    root = ctk.CTk()
    root.title("企業情報取得アプリ")

    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    label = ctk.CTkLabel(frame, text="企業名を入力してください:", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    entry = ctk.CTkEntry(frame, width=300, font=("Arial", 12))
    entry.pack(pady=10)

    button = ctk.CTkButton(frame, text="情報を取得", command=get_company_info, font=("Arial", 12))
    button.pack(pady=10)

    result_label = ctk.CTkLabel(frame, text="", wraplength=400, justify="left", text_color="white", font=("Arial", 12))
    result_label.pack(pady=10)

    # 結果表示用のテキストボックスを追加
    result_box = ctk.CTkTextbox(frame, width=400, height=200, font=("Arial", 12))
    result_box.pack(pady=10)
    result_box.configure(state="disabled")

    root.mainloop()

if __name__ == "__main__":
    main()