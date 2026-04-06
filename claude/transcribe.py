#!/usr/bin/env python3
"""Fast GPU transcription using faster-whisper. Outputs plain text to stdout."""
import sys
from faster_whisper import WhisperModel

model = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")

audio_file = sys.argv[1]
segments, _ = model.transcribe(audio_file, language="en", beam_size=5)
text = " ".join(seg.text.strip() for seg in segments)
print(text)
