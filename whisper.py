import mlx_whisper
from pydub import AudioSegment
import numpy as np

def preprocess_audio(sound):
    """音声を16kHz・モノラル・16bitに変換"""
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound

def transcribe_audio(audio_file="recorded.wav"):
    """
    mlx_whisperを使って文字起こしを行う
    """
    print("文字起こしを開始します...")
    result = mlx_whisper.transcribe(audio_file, path_or_hf_repo="whisper-base-mlx")
    text = result["text"]
    print("文字起こしが完了しました。")
    print("------ 文字起こし結果 ------")
    print(text)
    return text