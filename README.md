# Claude Avatar

A 3D talking avatar connected to **Claude Code CLI** for real-time voice conversation — no API keys required.

Built on top of [TalkingHead](https://github.com/met4citizen/TalkingHead) by Mika Suominen (MIT License).

---

## How it works

```
Mic → faster-whisper (GPU) → Claude Code CLI → edge-tts → Avatar lip-sync
```

- **Voice input** — MediaRecorder → ffmpeg WAV → faster-whisper `large-v3-turbo` on CUDA
- **Claude** — Persistent `claude` CLI session via `stream-json` protocol (~5s response, no startup overhead)
- **Voice output** — edge-tts `en-US-AvaMultilingualNeural` with word-level timing → TalkingHead lip-sync
- **UI** — Split layout: 3D avatar + chat (top) / CLI activity log (bottom)

---

## Requirements

- [Claude Code CLI](https://claude.ai/code) installed and authenticated
- Python 3.10+
- Node.js 18+
- ffmpeg
- NVIDIA GPU (for faster-whisper CUDA)

```bash
pip install faster-whisper edge-tts
npm install
```

---

## Run

```bash
node claude/server.cjs
```

Then open `claude/index.html` in your browser (or serve it via a local HTTP server).

---

## File structure

```
claude/
  server.cjs           # WebSocket bridge — Claude CLI + Whisper + TTS
  index.html           # Frontend — avatar, chat, CLI log
  tts.py               # edge-tts neural voice with word boundaries
  transcribe_server.py # Persistent Whisper server (model stays in VRAM)
  transcribe.py        # One-shot Whisper fallback
```

---

## Credits

- [TalkingHead](https://github.com/met4citizen/TalkingHead) — Mika Suominen (MIT License)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) — GPU-accelerated transcription
- [edge-tts](https://github.com/rany2/edge-tts) — Microsoft neural voices
- [Three.js](https://threejs.org/) — 3D rendering

---

## License

MIT — see [LICENSE](LICENSE). Original TalkingHead library © 2023-2024 Mika Suominen.
