# share-pack — grafiki do repostowania

Zestaw gotowych grafik dla mieszkańców do udostępniania na Instagramie i Facebooku.
Kampania: bezpieczne przejście pieszo-rowerowe pod torami linii 351 przy ul. św. Wawrzyńca,
łączące Jeżyce z Sołaczem. Strona: **jezyce-solacz.pl**. Poparcie: https://forms.gle/ArwnA9HsqTZWteWM6

## Co jest w paczce

### Kwadrat 1080×1080 (feed Instagram / Facebook)
- `ig-kwadrat-01.jpg` — hasło „Połączmy Jeżyce z Sołaczem" na wizualizacji + jezyce-solacz.pl.
- `ig-kwadrat-02.jpg` — karta-fakt „W planie od 2024. Wciąż go nie ma." (tło papierowe, bez zdjęcia).
- `ig-kwadrat-03.jpg` — CTA „Poprzyj przejście" + duży adres jezyce-solacz.pl na wizualizacji.

### Story 1080×1920 (Instagram / Facebook Stories)
- `ig-story-01.jpg` — hasło „Połączmy Jeżyce z Sołaczem"; u góry zostawione miejsce na naklejkę „Link".
- `ig-story-02.jpg` — CTA „Poprzyj inicjatywę"; u dołu miejsce na naklejkę „Link" / swipe-up.

## Jak użyć
1. Pobierz wybrany plik `.jpg`.
2. **Feed:** dodaj jako post (kwadrat). W opisie wklej link: jezyce-solacz.pl
3. **Story:** dodaj jako tło relacji, następnie nałóż natywną **naklejkę „Link"** w zaznaczonym
   miejscu (góra w story-01, dół w story-02) i wskaż adres **jezyce-solacz.pl**.
4. Zachęcamy do dopisania własnego komentarza — dlaczego to przejście jest dla Ciebie ważne.

Uwaga: grafiki z renderem mają dyskretny dopisek „wizualizacja AI" (uczciwość — to wizualizacja,
nie zdjęcie istniejącego obiektu). Nie usuwaj go przy ponownym renderowaniu.

## Jak zregenerować
Szablony HTML są w `templates/`. Tła pochodzą z `../hero/hero-XX.webp` (ścieżka względna).
Render headless Chrome → PNG, potem konwersja do JPG.

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(pwd)"   # uruchom z katalogu share-pack/

# kwadraty 1080×1080
for n in 01 02 03; do
  "$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
    --window-size=1080,1080 --virtual-time-budget=6000 \
    --screenshot="$DIR/ig-kwadrat-$n.png" "file://$DIR/templates/ig-kwadrat-$n.html"
done

# story 1080×1920
for n in 01 02; do
  "$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
    --window-size=1080,1920 --virtual-time-budget=6000 \
    --screenshot="$DIR/ig-story-$n.png" "file://$DIR/templates/ig-story-$n.html"
done

# PNG → JPG (zdjęcia q84; płaska karta-fakt q92)
for f in ig-kwadrat-01 ig-kwadrat-03 ig-story-01 ig-story-02; do
  sips -s format jpeg -s formatOptions 84 "$DIR/$f.png" --out "$DIR/$f.jpg"
done
sips -s format jpeg -s formatOptions 92 "$DIR/ig-kwadrat-02.png" --out "$DIR/ig-kwadrat-02.jpg"
rm -f "$DIR"/*.png
```

## Brand
- Font display: Bricolage Grotesque 800; body: IBM Plex Sans (Google Fonts CDN).
- Kolory: sygnałowy `#d8362a` (ciemniejszy `#a82318` pod małym tekstem dla kontrastu),
  grafit `#15171b`, papier `#f3efe6`.
- Tła wizualizacji: `hero/hero-01..12.webp` + ciemny gradient dla czytelności tekstu.

Aby zmienić tło danej grafiki, podmień nazwę pliku w regule `.bg{...url("../../hero/hero-XX.webp")...}`
w odpowiednim szablonie i zregeneruj.
