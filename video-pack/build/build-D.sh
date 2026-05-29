#!/usr/bin/env bash
# Klip D — galeria wizualizacji 1080x1080, ~8 s, staly pasek dolny. Najprostszy, na feed.
set -euo pipefail
FF="${FF:-/opt/homebrew/bin/ffmpeg}"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
ROOT="/Volumes/Projects/jezyce-solacz/video-pack"
HERO="/Volumes/Projects/jezyce-solacz/hero"
T="$ROOT/tmp"; mkdir -p "$T" "$ROOT/out"

"$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --default-background-color=00000000 --window-size=1080,1080 --virtual-time-budget=4000 \
  --screenshot="$T/D_pasek.png" "file://$ROOT/src/overlay-D-pasek.html" 2>/dev/null

# slideshow 5 renderow x 2 s + xfade 0.5 s, lekki crop do 1:1
"$FF" -y \
 -loop 1 -t 2 -i "$HERO/hero-01.webp" -loop 1 -t 2 -i "$HERO/hero-04.webp" \
 -loop 1 -t 2 -i "$HERO/hero-06.webp" -loop 1 -t 2 -i "$HERO/hero-09.webp" -loop 1 -t 2 -i "$HERO/hero-11.webp" \
 -i "$T/D_pasek.png" \
 -filter_complex "\
[0]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v0];\
[1]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v1];\
[2]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v2];\
[3]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v3];\
[4]scale=1080:1080:force_original_aspect_ratio=increase,crop=1080:1080,setsar=1[v4];\
[v0][v1]xfade=transition=fade:duration=0.5:offset=1.5[a];\
[a][v2]xfade=transition=fade:duration=0.5:offset=3.0[b];\
[b][v3]xfade=transition=fade:duration=0.5:offset=4.5[c];\
[c][v4]xfade=transition=fade:duration=0.5:offset=6.0[bg];\
[bg][5]overlay=0:0,format=yuv420p[v]" \
 -map "[v]" -c:v libx264 -crf 20 -r 30 -movflags +faststart \
 "$ROOT/out/04-galeria-1x1_1080x1080.mp4" 2>/dev/null
echo "GOTOWE: out/04-galeria-1x1_1080x1080.mp4"
