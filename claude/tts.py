#!/usr/bin/env python3
"""Generate TTS audio with word-level timing using edge-tts.
Outputs JSON: {"audio": "<base64 mp3>", "words": [...], "wtimes": [...], "wdurations": [...]}
"""
import sys
import json
import asyncio
import base64
import io
import edge_tts

VOICE = sys.argv[2] if len(sys.argv) > 2 else "en-US-AvaMultilingualNeural"

async def main():
    text = sys.argv[1]
    communicate = edge_tts.Communicate(text, VOICE, boundary="WordBoundary")

    audio_chunks = []
    words = []
    wtimes = []
    wdurations = []

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_chunks.append(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            words.append(chunk["text"])
            # edge-tts times are in 100-nanosecond units, convert to milliseconds
            offset_ms = chunk["offset"] / 10000
            duration_ms = chunk["duration"] / 10000
            wtimes.append(offset_ms)
            wdurations.append(duration_ms)

    audio_bytes = b"".join(audio_chunks)
    audio_b64 = base64.b64encode(audio_bytes).decode("ascii")

    result = {
        "audio": audio_b64,
        "words": words,
        "wtimes": wtimes,
        "wdurations": wdurations
    }
    print(json.dumps(result))

asyncio.run(main())
