# Koszulki Jeżyce — kierunek + prompty do generacji

Noszalne koszulki o dzielnicy Jeżyce (Poznań). **Bez treści kampanijnych/agitacyjnych** — lokalna duma, gwara, ikony dzielnicy. Realne obiekty z `koszulki-ref/` jako referencje image-to-image (anty-halucynacja). Wynik panelu 3 ekspertów (koncept+copy, prompt-engineering i2i, krytyk-noszalności).

## Zasady (panel-approved)

**Wygrywa:** detal zamiast pocztówki · monochrom lub 2 kolory · jeden pomysł · zero apelu · insiderski kod (detal architektoniczny bez podpisu, jedno słowo gwary poważnym fontem, faux-instytucja, kod pocztowy/rok).

**Cringe — NIE robić:** doodle-cluster wszystkiego naraz · pełna pocztówkowa scena · psychodelia bez konceptu · maskotka-cukierek / słodki jeżyk z oczkami · „I ❤️ Jeżyce" · szablon „EST.+wieniec" · hashtagi · uśmiechnięta bimba · gwara całymi zdaniami · Comic Sans / WordArt · herb miasta.

**Trend 2026:** „neighborhood / city-pride streetwear" jest na fali (Bronx Native, The 7 Line, Awake NY) — ale wygrywa subtelny kod, nie stos symboli.

## Reguły techniczne (z wcześniejszego researchu)

- Modele: **GPT Image 2** (najlepszy tekst), **Nano Banana 2** (transparencja, 2K/4K, i2i). Prompty po EN.
- **Anty-mockup** (do każdego promptu): `flat 2D artwork only, NOT a mockup, no t-shirt, no garment, no person, isolated background`.
- **Print-ready:** `flat solid fills, clean edges, limited palette, no gradients` (spot/etching). Paletę i tak redukuj po generacji (Photoshop Indexed/Posterize).
- **i2i wierność:** nazwij `Image 1`, dodaj `preserve exact silhouette/proportions/details, do not add or invent, restyle only the technique`. Geometrię opisz też słownie (redundancja ratuje przy dryfie). 4-6 wariantów, odrzucaj zhalucynowane.
- **Polskie znaki (ż/ę/ó/ł) modele psują** → **lettering wektorem osobno** (Affinity/Illustrator/Inkscape), realny font. „bimba"/„tej" bez ogonków bezpieczne w prompcie.
- **Druk:** flat-art → wektor → sitodruk 1-kolor, jasny garment (cienka kreska etchingu nie znosi białej bazy na ciemnym). Halftone/psychodelia → raster 300 DPI w docelowym cm. Sprany look = efekt druku (water-based/discharge), nie grafiki.
- Garment vintage: Stanley/Stella (Natural Raw — EU/Printful), Comfort Colors 1717 (Ivory/Pepper), AS Colour Faded. Unikać Gildan.

---

## TEE 1 — „WIADUKT" (etching mono, flagowiec)

Ceglany łuk wiaduktu Kościelna jako rycina — industrialny, czyta się jak cool print bez podpisu.
Ref: `koszulki-ref/real-tunel-koscielna.webp` · Garment: vintage white / ecru · Tusz: 1 kolor (#1b2a3a granat lub sepia) · Układ: duży plecy LUB średni pierś, mikro-podpis albo zero.

```
Image 1 is a real photo of a red-brick arched railway viaduct/tunnel in Poznań,
with a black steel railing along the footpath and a dark arched tunnel mouth.
Redraw the EXACT arch and brick structure from Image 1 as a vintage etching / copperplate engraving.
HARD CONSTRAINTS: preserve the exact shape and proportions of the brick arch, the railing line
and the tunnel opening from Image 1. Do NOT add or invent structures. Remove all people, strollers,
cars, stickers and emoji. Restyle ONLY the technique into engraved line work.
STYLE: monochrome etching, fine cross-hatching and parallel-line shading, bold inked keyline,
antique print plate feel, subtle worn-ink distress.
PALETTE: single ink color #1b2a3a on off-white #f3ead7, 1-color separation, no gradients.
flat 2D artwork ONLY, NOT a mockup, no t-shirt, no garment, no person, isolated on off-white background,
centered, high contrast, clean edges for screen printing.
EXCLUDE: color, photo texture, mockup, modern objects, gradients, soft shadow, 3D.
```

Alt motyw (ta sama technika → spójna seria): `koszulki-ref/kamienice-roosevelta.jpg` — wytnij samą wieżyczkę z hełmem (detal, nie całą fasadę).
Mikro-podpis (wektor, opcja): „JEŻYCE" małe pod łukiem albo `52.41°N 16.91°E`.

---

## TEE 2 — „BIMBA" (typograficzna, jedno słowo)

Gwarowy żart bez tłumaczenia. Wielkie BIMBA poważnym grotem/serifem, monochrom + cichy kod. Kontrast „poważny font × zabawne słowo".
Garment: sprany butelkowy zielony lub ecru · 1 kolor · Układ: duże słowo centralnie + drobne `PL-60 · JEŻYCE` pod spodem.

**Głównie wektor** (pewne ogonki, ostre do druku). Krój: solidny grotesk (Anton / Archivo Black) lub retro serif. Bez „śmiesznego" fontu. „bimba" bez ogonków = bezpieczne.

Opcjonalny mikro-emblem (i2i, ikonka techniczna zamiast ilustracji):
```
Image 1 is a real photo of a green-and-cream articulated Konstal tram (two segments + accordion joint).
Make a tiny minimal single-line technical side-silhouette icon of THIS exact tram —
keep the two articulated segments and accordion joint from Image 1.
STYLE: clean mono-weight line icon, 1 color, no fill, transit-blueprint look.
flat 2D artwork only, no mockup, no shirt, isolated on transparent/white, 1-color #2b2b2b.
EXCLUDE: face, eyes, cuteness, color, 3D, gradient, mockup, extra cars.
```

Alt-słowa (ten sam layout): „TEJ", „PYRY", „SZNEKA Z GLANCEM" (mikro).

---

## TEE 3 — „JEŻYCKIE ZAKŁADY" (faux-instytucja, stary szyld)

Udawany międzywojenny/PRL szyld nieistniejącego zakładu — chwyt hyperlocal marek. Liternictwo emaliowanego szyldu, 1 kolor na naturze. Subtelny linearny jerzyk lub rok.
Garment: natural raw / ecru · 1 kolor (terakota lub granat) · Układ: plecy — szyld w ramce; przód — mała pieczątka.

**Wektor-led** (typografia szyldu). Jerzyk rysuj liniowo w wektorze (nie maskotka). Nazwy faux-org (bez naruszeń znaków):
- „JEŻYCKIE ZAKŁADY ROWEROWE" · „SPÓŁDZIELNIA JEŻYCKA" · „TOWARZYSTWO PRZYJACIÓŁ KAMIENIC" · „KLUB JEŻYCE — POZNAŃ".
Detal: drobne `od 1900` (rok włączenia Jeżyc do Poznania — fakt) zamiast pustego „EST.".

Opcjonalny emblem szyldu (i2i z kamienicy):
```
Image 1 is a real photo of a corner Art-Nouveau tenement in Poznań with a rounded corner oriel
(bay window) and two tall ornamental gables.
Redraw ONLY the corner turret/gable detail from Image 1 as a small 1-color enamel-sign emblem.
HARD CONSTRAINTS: keep the real shape of the gable/oriel from Image 1, do not invent.
STYLE: vintage enamel shop-sign / linocut, single flat color, bold simple shapes.
flat 2D artwork only, no mockup, no shirt, isolated on flat background, 1-color, no gradient.
EXCLUDE: full facade, cars, signage text, color, 3D, mockup.
```

---

## Uniwersalne hasła (gwara + duma, bez kampanii)

Na mały hit / rękaw / metkę: „TEJ, Z JEŻYC" · „JEŻYCE — POZNAŃ" · „WUCHTA WIARY" · „BLUBRAĆ PO JEŻYCKU" · „POZNAŃ / JEŻYCE / od 1900" · „SZNEKA Z GLANCEM".

## Referencje fotograficzne

Wszystkie w `koszulki-ref/` (+ README z mapowaniem i licencjami): real-tunel-koscielna, render-tunel-2, render-lot-ptaka, kamienice-roosevelta, kamienica-kordeckiego12, rynek-jezycki, tramwaj-poznan-102n (zielony Konstal).

## Fakty do pilnowania (anty-błąd)

- Poznańska bimba jest **zielona**. Wiadukt Kościelna: ceglany, łukowy, ~150 lat.
- Jeż/jerzyk = symbole z muralu Jeżycka 36 (2021, wybrane przez mieszkańców) — legit, ale rysuj liniowo, nie jako maskotkę.
- **Goplana = żywy znak towarowy** → tylko inspiracja dziedzictwem, bez logo/nazwy na wzorze.
- Patron kościoła Jeżyc = **św. Florian** (NIE Wawrzyniec — to nazwa ulicy).
- Prawa komercyjne AI-artu do sprzedaży na produktach: sprawdź TOS modelu [do weryfikacji].
