def save_text(text, filename="recordingsample.txt"):
    """
    文字起こし結果をテキストファイルに保存
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"文字起こし結果を '{filename}' に保存しました。")