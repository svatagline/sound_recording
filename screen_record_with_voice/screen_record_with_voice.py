import subprocess
import signal
import sys
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

video_file = f"screen_{timestamp}.mp4"
audio_file = f"audio_{timestamp}.wav"

VIDEO_DEVICE = "0"   # Screen
AUDIO_DEVICE = "1"   # BlackHole
FPS = 30
# ---------- VIDEO (SCREEN ONLY) ----------
video_cmd = [
    "ffmpeg",
    "-y",
    "-f", "avfoundation",
    "-framerate", str(FPS),
    "-i", f"{VIDEO_DEVICE}:{AUDIO_DEVICE}",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-crf", "23",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "128k",
    "-movflags", "+faststart",
    video_file
]

# ---------- AUDIO (SYSTEM AUDIO → WAV) ----------
audio_cmd = [
    "ffmpeg",
    "-f", "avfoundation",
    "-i", "none:1",          # System audio (BlackHole)
    "-ac", "2",
    "-ar", "44100",
    "-c:a", "pcm_s16le",     # WAV (16-bit PCM)
    audio_file
]

print("🎥 Recording VIDEO and AUDIO separately")
print("🛑 Press CTRL + C to stop")
print(f"📁 Video: {video_file}")
print(f"📁 Audio: {audio_file}")

video_proc = subprocess.Popen(
    video_cmd,
    preexec_fn=os.setsid
)
audio_proc = subprocess.Popen(audio_cmd)

def stop_recording(sig, frame):
    print("\n🛑 Stopping recording...")
    os.killpg(os.getpgid(video_proc.pid), signal.SIGINT)
    video_proc.wait() 
    audio_proc.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, stop_recording)

video_proc.wait()
audio_proc.wait()
