#!/usr/bin/env bash
# Klip A — "haslo + Ken Burns", 1080x1920 pion, ~12.5 s. Bez muzyki (social gra cicho).
# Tekst: Chrome (fonty marki). Ruch: ffmpeg zoompan. Montaz: xfade.
set -euo pipefail
FF="${FF:-/opt/homebrew/bin/ffmpeg}"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
ROOT="/Volumes/Projects/jezyce-solacz/video-pack"
HERO="/Volumes/Projects/jezyce-solacz/hero"
T="$ROOT/tmp"; mkdir -p "$T" "$ROOT/out"

RENDS=(hero-04 hero-09 hero-02 hero-11)         # tla scen s1..s4
TXT=(overlay-A-s1 overlay-A-s2 overlay-A-s3 overlay-A-s4)

for i in 0 1 2 3; do
  n=$((i+1))
  "$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --default-background-color=00000000 --window-size=1080,1920 --virtual-time-budget=4000 \
    --screenshot="$T/txt_s$n.png" "file://$ROOT/src/${TXT[$i]}.html" 2>/dev/null
  # Render jest poziomy (3:2). NIE skalujemy go do 9:16 (to scisnelo obraz) ani nie tniemy
  # (straci szerokosc sceny). Pasmo 3:2 z pelnym renderem + rozmyte/przyciemnione tlo
  # wypelniajace kadr 9:16 (styl Reels). Ken Burns (zoom-in) na ostrej warstwie, s=3:2 -> brak zniekszt.
  # UWAGA: -t 3.5 MUSI byc opcja WYJSCIA (po -map) — zoompan d=105 na -loop 1 inaczej
  # eksploduje do setek sekund. Kapujemy output na 3.5 s.
  "$FF" -y -loop 1 -i "$HERO/${RENDS[$i]}.webp" -filter_complex "\
[0]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=28:2,eq=brightness=-0.22:saturation=0.85[bg];\
[0]scale=1620:-1,zoompan=z='min(zoom+0.0008,1.10)':d=105:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x720:fps=30,setsar=1[fg];\
[bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p[v]" \
    -map "[v]" -t 3.5 -r 30 -c:v libx264 -pix_fmt yuv420p -crf 21 "$T/A_s$n.mp4" 2>/dev/null
  "$FF" -y -i "$T/A_s$n.mp4" -i "$T/txt_s$n.png" \
    -filter_complex "[0:v][1:v]overlay=0:0,format=yuv420p" -c:v libx264 -crf 18 "$T/A_s${n}_t.mp4" 2>/dev/null
done

"$FF" -y -i "$T/A_s1_t.mp4" -i "$T/A_s2_t.mp4" -i "$T/A_s3_t.mp4" -i "$T/A_s4_t.mp4" \
  -filter_complex "[0][1]xfade=transition=fade:duration=0.5:offset=3.0[a];[a][2]xfade=transition=fade:duration=0.5:offset=6.0[b];[b][3]xfade=transition=fade:duration=0.5:offset=9.0,format=yuv420p[v]" \
  -map "[v]" -c:v libx264 -crf 22 -preset medium -maxrate 5M -bufsize 10M -pix_fmt yuv420p -r 30 -movflags +faststart \
  "$ROOT/out/01-haslo-kenburns_1080x1920.mp4" 2>/dev/null
echo "GOTOWE: out/01-haslo-kenburns_1080x1920.mp4"
