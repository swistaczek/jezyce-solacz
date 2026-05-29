# Karty cytatów — PNG z przezroczystym tłem

Karty z autentycznymi, anonimowymi cytatami mieszkańców (podpis = dzielnica). Płyta karty jest **nieprzezroczysta** (papier #f3efe6), margines wokół **przezroczysty** + miękki cień — dzięki temu karta jest czytelna **na jasnym i na ciemnym tle** hosta (media osadzają w swoich materiałach). Format pliku: **PNG RGBA** (nie konwertować na JPG).

## Pliki

- `cytat-kwadrat-01..06.png` — 1080×1080 (IG/FB feed)
- `cytat-story-01,03,05.png` — 1080×1920 (Stories / Reels cover)
- `cytat-poziom-01,02,06.png` — 1200×630 (artykuły, OG, Twitter/X)

## Regeneracja

```bash
cd share-pack/cytaty
python3 generuj.py        # pisze build/*.html
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
while IFS=$'\t' read -r h dims png; do
  "$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
    --default-background-color=00000000 --window-size=$dims --virtual-time-budget=4000 \
    --screenshot="$png" "file://$h"
done < build/jobs.tsv
```

## Zasady

- Tylko cytaty autentyczne (z formularza poparcia / sekcji „Głosy" na stronie). Bez zmyślania.
- Podpis = wyłącznie dzielnica (Jeżyce / Sołacz / Poznań / Spoza Poznania). Nigdy imię, adres, e-mail — RODO.
- System wizualny zgodny ze stroną: Bricolage Grotesque + IBM Plex Sans, czerwień #d8362a, papier #f3efe6.
- Auto-skalowanie cytatu przez klasę długości na `.card`: `len-s` / `len-m` / `len-l` / `len-xl`.
