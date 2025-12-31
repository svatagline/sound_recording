import subprocess
import datetime
import sys

VIDEO_DEVICE = "0"   # screen
AUDIO_DEVICE = "1"   # BlackHole
FPS = 30

OUTPUT = f"screen_record_{datetime.datetime.now():%Y%m%d_%H%M%S}.mp4"

cmd = [
    "ffmpeg",
    "-f", "avfoundation",
    "-framerate", str(FPS),
    "-i", f"{VIDEO_DEVICE}:{AUDIO_DEVICE}",
    "-vf", "format=yuv420p",
    "-c:v", "libx264",
    "-profile:v", "high",
    "-level", "4.2",
    "-preset", "veryfast",
    "-crf", "23",
    "-c:a", "aac",
    "-b:a", "128k",
    "-movflags", "+faststart",
    OUTPUT
]

print("🎥 Recording FULL SCREEN + SYSTEM AUDIO")
print("🛑 Press ENTER to stop recording")

process = subprocess.Popen(
    cmd,
    stdin=subprocess.PIPE,
    text=True
)

try:
    input()
finally:
    print("🛑 Stopping recording...")
    process.stdin.write("q\n")
    process.stdin.flush()
    process.wait()

print("✅ Recording saved successfully:", OUTPUT)
