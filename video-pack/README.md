# Video pack — Jeżyce ↔ Sołacz

Krótkie wideo pod social (Reels / TikTok / Stories / Shorts / feed). Tekst renderowany przez **headless Chrome** (prawdziwe fonty marki: Bricolage Grotesque + IBM Plex Sans), ruch i montaż przez **ffmpeg** (zoompan + xfade). Faktografia 1:1 ze stroną — bez kosztów, bez dat realizacji, bez „miasto zbuduje". Każdy klip z renderami ma znak „wizualizacja AI".

## Gotowe klipy (`out/`)

| Plik | Format | Dł. | Cel |
|------|--------|-----|-----|
| `01-haslo-kenburns_1080x1920.mp4` | pion 9:16 | 12,5 s | Hook + CTA. Ken Burns po renderach + hasło → „Wciąż go nie ma" → poprzyj. |
| `04-galeria-1x1_1080x1080.mp4` | kwadrat | 8 s | Feed IG/FB. Slideshow wizualizacji + pasek z domeną. |

Master 9:16 H.264/AAC, faststart — działa na Reels, TikTok, Shorts, Stories bez re-eksportu (różnią się tylko opis/hasztagi).

## Jak zbudować

```bash
cd video-pack
python3 src/generuj-overlay.py     # warstwy tekstowe HTML (fonty marki)
bash build/build-A.sh              # -> out/01-haslo-kenburns_1080x1920.mp4
bash build/build-D.sh              # -> out/04-galeria-1x1_1080x1080.mp4
```

Wymagane: Google Chrome + ffmpeg (`brew install ffmpeg`). Ścieżki można nadpisać `FF=` i `CHROME=`.

## Muzyka (opcjonalna — dodaj ręcznie)

Klipy działają bez dźwięku (social gra cicho, tekst = napis). By dodać podkład:
1. Pobierz utwór **royalty-free / CC0**: [Pixabay Music](https://pixabay.com/music/) (licencja Pixabay, bez atrybucji), [Free Music Archive](https://freemusicarchive.org/) (filtr CC0 / CC BY), lub YouTube Audio Library (przy publikacji na YT). Profil: cinematic / hopeful, 90–110 BPM.
2. Zapisz jako `audio/bed-hopeful.mp3` i **wpisz atrybucję do `audio/LICENCJE.txt`**.
3. Dołóż ścieżkę (przykład dla klipu A):
```bash
ffmpeg -y -i out/01-haslo-kenburns_1080x1920.mp4 -i audio/bed-hopeful.mp3 \
  -filter_complex "[1:a]atrim=0:12.5,afade=t=out:st=11:d=1.5,loudnorm=I=-16:TP=-1.5[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest out/01-haslo-kenburns_audio.mp4
```

## Do dorobienia (storyboard gotowy)

- **Klip B — `02-problem-rozwiazanie` (18 s, pion):** zdjęcie wąskiego tunelu (`problem-koscielna-full.webp`, zoom-in) → cięcie → render („A mogłoby tak"). Tekst on-screen: „Dziś jedyne przejście: tunel przy Kościelnej" / „Tak wąski, że dwa wózki się nie miną" / „W planie od 2024" / CTA. Pipeline jak A: overlay Chrome + zoompan na zdjęciu + xfade.
- **Klip C — `03-cytaty` (~22 s, pion):** 4–5 prawdziwych, anonimowych cytatów (podpis = dzielnica) na przyciemnionych renderach; intro „Z 311 odpowiedzi mieszkańców:". Karty jak `share-pack/cytaty/` lub overlaye fade.

## Co automatyczne, co ręczne

- **Automatyczne (Chrome+ffmpeg):** klipy A, B, C, D — tła z renderów/zdjęć, tekst Chrome, montaż ffmpeg, eksport master.
- **Ręczne:** wybór/pobranie muzyki (licencja!), ewentualne nagrania w terenie (zamaż twarze — RODO), publikacja na kontach social.

## Struktura

```
video-pack/
  src/        overlaye HTML (tekst, fonty marki) + generuj-overlay.py
  build/      build-A.sh, build-D.sh
  audio/      bed-hopeful.mp3 (ręcznie) + LICENCJE.txt
  out/        gotowe mp4
  tmp/        klatki/segmenty pośrednie (nie wersjonowane)
```
