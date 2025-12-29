import sounddevice as sd
import soundfile as sf
import numpy as np

# ---- CONFIG ----
SAMPLE_RATE = 44100
CHANNELS = 2
DURATION = 10          # seconds
OUTPUT_FILE = "system_audio.wav"

# List devices to find BlackHole
print("Available audio devices:")
print(sd.query_devices())

# Change this index to BlackHole device index
BLACKHOLE_DEVICE_INDEX = 2  # <-- update after checking list

print("Recording system audio...")

recording = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    device=BLACKHOLE_DEVICE_INDEX,
    dtype='float32'
)

sd.wait()

sf.write(OUTPUT_FILE, recording, SAMPLE_RATE)

print(f"Recording saved as {OUTPUT_FILE}")
