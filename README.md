# sound_recording

https://chatgpt.com/share/6952914e-edb8-800d-9781-15bd7924e1eb

1. install
   brew uninstall blackhole-2ch
   brew install blackhole-2ch

2. remove headphone and select system speaker from top right corner wifi,bluetooth

3. restart pc

4. python - <<EOF
   import sounddevice as sd
   print(sd.query_devices())
   EOF
   <!-- Below device should need to see in terminal -->

   2 BlackHole 2ch, Core Audio (2 in, 2 out)

5. run script
