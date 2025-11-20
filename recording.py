import ffmpeg

def record_audio(output_file="recorded.wav", duration=10):
    """
    FFmpegを使ってマイク入力を録音する（macOSの場合）
    """
    print(f"{duration}秒間、マイクからの録音を開始します...")
    try:
        (
            ffmpeg
            .input(':0', format='avfoundation', t=duration)  # macOS向け
            .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
            .run(overwrite_output=True)
        )
        print(f"録音が完了しました: {output_file}")
    except ffmpeg.Error as e:
        print(f"FFmpegエラー: {e.stderr.decode()}")
    except Exception as e:
        print(f"予期せぬエラー: {e}")

    return output_file