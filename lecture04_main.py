from recording import record_audio
from whisper import transcribe_audio
from save import save_text

def main():
    print("=== 音声録音 → 文字起こし → 保存 システム ===")
    audio_file = record_audio(duration=10)  # 10秒録音
    text = transcribe_audio(audio_file)
    save_text(text)
    print("=== 一連の処理が完了しました！ ===")

if __name__ == "__main__":
    main()