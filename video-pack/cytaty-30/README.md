# Cytaty 30 — pętla pod nagranie (b-roll TV / social)

Samodzielna strona `index.html` (HTML+CSS+JS w jednym pliku, zero zależności, działa offline przez `file://`). 30 anonimowych cytatów mieszkańców, autoodtwarzanie w pętli, scena stała 1920×1080.

**Layout „Ściana głosów":** wszystkie 30 cytatów widoczne naraz jako przygaszona mozaika w tle (dowód społeczny — wrażenie setek głosów), a jeden cyklicznie wychodzi na pierwszy plan jako duży, czytelny panel. Kafelek wyróżnionego cytatu gaśnie w ścianie („wyjęty do przodu"). Centralny scrim przyciemnia środek → panel jest ostry i czytelny nawet po kompresji TV.

## Jak nagrać

1. Otwórz `index.html` w **Google Chrome** (dwuklik / przeciągnij do okna).
2. **F11** lub klawisz **F** — tryb pełnoekranowy. Okno większe niż 1920×1080 → scena zostaje wyśrodkowana na czarnym tle (nagranie czyste); dla 1:1 ustaw przeglądarkę na monitorze 1920×1080.
3. Nagraj ekran **1920×1080** (QuickTime „Nagraj ekran" → zaznacz obszar; OBS → źródło „Display Capture", canvas 1920×1080).
4. Info o sterowaniu znika po ~3 s — zacznij nagrywanie i odczekaj te 3 s, albo dograj od drugiej pętli.
5. Bez dźwięku (b-roll). Podkład muzyczny dodaj w montażu.

## Czas pętli

Jedna pełna pętla: **~255 s (4 min 15 s)**. Taktowanie deterministyczne (powtarzalne między nagraniami — bez losowości). Każdy cytat: wjazd 0,9 s → przytrzymanie 4,5–8,5 s (skalowane do długości) → wypad 0,7 s.

## Sterowanie klawiaturą

| Klawisz | Działanie |
|---|---|
| `Spacja` | pauza / wznów |
| `←` / `→` (lub `↑` / `↓`) | poprzedni / następny cytat |
| `F` | pełny ekran |

## Uwagi

- Autostart bez interakcji (od załadowania).
- `prefers-reduced-motion` → bez ruchu (twarde przejścia), ale pętla nadal gra.
- Zero danych osobowych — tylko cytat + dzielnica.
