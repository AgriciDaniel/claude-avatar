#!/usr/bin/env python3
"""Persistent faster-whisper server. Model stays loaded in VRAM.
Reads WAV file paths from stdin, outputs transcripts to stdout.
"""
import sys
from faster_whisper import WhisperModel

print("LOADING_MODEL", flush=True)
model = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")
print("MODEL_READY", flush=True)

for line in sys.stdin:
    wav_path = line.strip()
    if not wav_path:
        continue
    try:
        segments, _ = model.transcribe(wav_path, language="en", beam_size=5)
        text = " ".join(seg.text.strip() for seg in segments)
        print(f"TRANSCRIPT:{text}", flush=True)
    except Exception as e:
        print(f"ERROR:{e}", flush=True)
