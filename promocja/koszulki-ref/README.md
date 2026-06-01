# Referencje fotograficzne do generacji koszulek Jeżyce

Prawdziwe zdjęcia realnych obiektów — podawaj je generatorowi jako **image-to-image / style-reference** (Nano Banana 2: multi-image edit; GPT Image 2: „apply the style to Image 1, keep the real shape of the building/tram/tunnel"). Cel: AI ma odwzorować PRAWDZIWY kształt, nie halucynować.

## Pliki i co przedstawiają

| Plik | Obiekt (realny) | Do której koszulki | Źródło / licencja |
|------|------------------|--------------------|-------------------|
| `real-tunel-koscielna.webp` | Faktyczny wąski tunel pod historycznym wiaduktem, ul. Kościelna (obiekt kampanii; twarze zasłonięte) | TEE2 (etching), TEE3 (zine) | własne (kampania) |
| `render-tunel-2.jpg` | Wizualizacja docelowego tunelu Jeżyce↔Sołacz (AI, poglądowa) | TEE2 | render kampanii |
| `render-lot-ptaka.jpeg` | Wał linii 351 z lotu ptaka + lokalizacja przejścia | TEE3 (nasyp jako bariera) | render kampanii |
| `kamienice-roosevelta.jpg` | Eklektyczno-secesyjna kamienica narożna z wieżyczką (ul. Roosevelta) | TEE1 (doodle kamienica) | Wikimedia Commons — sprawdź autora/licencję |
| `kamienica-kordeckiego12.jpg` | Secesyjna kamienica narożna z wykuszem i szczytem (ul. Kordeckiego 12) | TEE1 (alternatywa kamienicy) | Wikimedia Commons |
| `rynek-jezycki.jpg` | Rynek Jeżycki — stragany + pierzeja kamienic | TEE1 (tło/klimat), ew. osobny motyw | Wikimedia Commons |
| `tramwaj-poznan-102n.jpg` | **Zielony** poznański tramwaj (Konstal) — pod wiaduktem | TEE1 (tramwaj-buźka), TEE3 | Wikimedia Commons |

## Kluczowe „prawdy" do zachowania (żeby nie było generyka)

- **Poznańska bimba jest ZIELONA** (nie żółta/czerwona). Wymuś kolor + sylwetkę Konstal z `tramwaj-poznan-102n.jpg`.
- **Wiadukt Kościelna = ceglany, łukowy, ~150 lat** — kształt z `real-tunel-koscielna.webp` / `render-tunel-2.jpg`.
- **Kamienice Jeżyc** — secesja/eklektyzm: wykusze, wieżyczki, zdobione szczyty (Roosevelta/Kordeckiego), nie blokowisko.
- **Nasyp linii 351** — trawiasty wał + sieć trakcyjna + słupy (z `render-lot-ptaka.jpeg`).

## Użycie (image-to-image)

1. Wgraj zdjęcie referencyjne jako Image 1.
2. Prompt stylu (etching / doodle / zine — z głównego briefu) + instrukcja: *„redraw the building/tram/tunnel from Image 1 in {style}, keep its real silhouette and proportions, flat print artwork, isolated background"*.
3. Dla serii: trzymaj jeden styl, zmieniaj tylko obiekt (kamienica → tramwaj → tunel) — spójna kolekcja.

## Licencje (WAŻNE przed publikacją sprzedażową)

Zdjęcia z **Wikimedia Commons** mają licencje CC (BY / BY-SA / CC0) — różne per plik. Jako **referencja do generacji** output jest nową grafiką, ale jeśli finalny wzór będzie wyglądał jak kalka konkretnego zdjęcia, **podaj atrybucję autora** (sprawdź na stronie pliku na Commons). Pliki kampanii (`real-tunel`, rendery) — własne; render to AI-wizualizacja, oznaczaj „wizualizacja".
