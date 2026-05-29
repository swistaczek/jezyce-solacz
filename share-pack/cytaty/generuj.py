#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator kart cytatow (PNG z przezroczystym tlem) dla inicjatywy Jezyce <-> Solacz.
   Pisze HTML per karta do build/, render PNG robi render.sh (headless Chrome).
   Cytaty wylacznie autentyczne (z formularza poparcia), podpis = dzielnica (bez danych osobowych).
   Plyta karty NIEPRZEZROCZYSTA (papier) + przezroczysty margines -> czytelne na jasnym i ciemnym tle."""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(OUT, "build")
os.makedirs(BUILD, exist_ok=True)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800'
         '&family=IBM+Plex+Sans:wght@500;600;700&display=swap" rel="stylesheet">')

ROOT_CSS = """:root{--ink:#15171b;--paper:#f3efe6;--signal:#d8362a;--signal-deep:#a82318;--muted:#5d6068;--line:rgba(21,23,27,.12)}
*{margin:0;padding:0;box-sizing:border-box}
body{background:transparent;font-family:"IBM Plex Sans",system-ui,sans-serif}
.mark{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;color:var(--signal);line-height:.6;user-select:none}
.q{font-family:"Bricolage Grotesque",sans-serif;font-weight:600;letter-spacing:-.015em;color:var(--ink)}
.q b{font-weight:800;color:var(--signal-deep)}
.by{font-family:"IBM Plex Sans",sans-serif;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);display:flex;align-items:center;gap:14px}
.by::before{content:"";width:34px;height:3px;background:var(--signal);display:inline-block;border-radius:2px}
.sig{text-align:right;line-height:1.25}
.sig .init{font-weight:600;letter-spacing:.05em;color:var(--muted)}
.sig .dom{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;letter-spacing:-.01em;color:var(--ink)}
.sig .dom span{color:var(--signal)}"""

# --- format: KWADRAT 1080x1080 ---
KWADRAT_CSS = """html,body{width:1080px;height:1080px;overflow:hidden}
body{display:flex;align-items:center;justify-content:center;padding:46px}
.card{position:relative;width:100%;height:100%;background:var(--paper);border-radius:22px;border:1px solid var(--line);
 box-shadow:0 30px 70px -28px rgba(21,23,27,.55),0 4px 14px -8px rgba(21,23,27,.30);
 padding:96px 84px 78px;display:flex;flex-direction:column;isolation:isolate;overflow:hidden}
.card::after{content:"";position:absolute;left:0;top:0;width:100%;height:10px;background:var(--signal)}
.mark{font-size:200px;height:84px;margin-bottom:14px}
.q{flex:1 1 auto;display:flex;align-items:center}
.len-s .q{font-size:78px;line-height:1.04}
.len-m .q{font-size:64px;line-height:1.08}
.len-l .q{font-size:52px;line-height:1.12}
.len-xl .q{font-size:42px;line-height:1.16}
.foot{margin-top:34px;display:flex;align-items:flex-end;justify-content:space-between;gap:24px}
.by{font-size:23px}.sig .init{font-size:16px}.sig .dom{font-size:26px}"""

# --- format: STORY 1080x1920 ---
STORY_CSS = """html,body{width:1080px;height:1920px;overflow:hidden}
body{display:flex;align-items:center;justify-content:center;padding:60px 56px}
.card{position:relative;width:100%;height:100%;background:var(--paper);border-radius:28px;border:1px solid var(--line);
 box-shadow:0 40px 90px -30px rgba(21,23,27,.55),0 6px 18px -10px rgba(21,23,27,.30);
 padding:140px 92px 120px;display:flex;flex-direction:column;isolation:isolate;overflow:hidden}
.card::after{content:"";position:absolute;left:0;top:0;width:100%;height:12px;background:var(--signal)}
.mark{font-size:240px;height:108px;margin-bottom:30px}
.q{flex:1 1 auto;display:flex;align-items:center}
.len-s .q{font-size:96px;line-height:1.05}
.len-m .q{font-size:80px;line-height:1.1}
.len-l .q{font-size:64px;line-height:1.14}
.len-xl .q{font-size:52px;line-height:1.18}
.foot{margin-top:48px;display:flex;flex-direction:column;align-items:flex-start;gap:34px}
.by{font-size:28px}.sig{text-align:left}.sig .init{font-size:20px}.sig .dom{font-size:36px}"""

# --- format: POZIOM 1200x630 (cudzyslow lewa, cytat+stopka prawa) ---
POZIOM_CSS = """html,body{width:1200px;height:630px;overflow:hidden}
body{display:flex;align-items:center;justify-content:center;padding:32px}
.card{position:relative;width:100%;height:100%;background:var(--paper);border-radius:16px;border:1px solid var(--line);
 box-shadow:0 24px 60px -26px rgba(21,23,27,.55),0 4px 12px -8px rgba(21,23,27,.30);
 padding:56px 64px 52px 56px;display:grid;grid-template-columns:auto 1fr;gap:36px;isolation:isolate;overflow:hidden}
.card::after{content:"";position:absolute;left:0;top:0;width:10px;height:100%;background:var(--signal)}
.mark{font-size:150px;height:64px;line-height:.5}
.col{display:flex;flex-direction:column;height:100%}
.q{flex:1 1 auto;display:flex;align-items:center}
.len-s .q{font-size:60px;line-height:1.06}
.len-m .q{font-size:48px;line-height:1.12}
.len-l .q{font-size:40px;line-height:1.16}
.len-xl .q{font-size:33px;line-height:1.2}
.foot{margin-top:22px;display:flex;align-items:flex-end;justify-content:space-between;gap:20px}
.by{font-size:19px}.sig .init{font-size:13px}.sig .dom{font-size:22px}"""

SIG = ('<div class="sig"><div class="init">Inicjatywa obywatelska · Jeżyce ↔ Sołacz</div>'
       '<div class="dom">jezyce-solacz<span>.</span>pl</div></div>')

def card_kwadrat_story(q, by, length):
    return (f'<div class="card {length}"><div class="mark">&#8220;</div>'
            f'<blockquote class="q">{q}</blockquote>'
            f'<div class="foot"><div class="by">{by}</div>{SIG}</div></div>')

def card_poziom(q, by, length):
    return (f'<div class="card {length}"><div class="mark">&#8220;</div>'
            f'<div class="col"><blockquote class="q">{q}</blockquote>'
            f'<div class="foot"><div class="by">{by}</div>{SIG}</div></div></div>')

def page(fmt_css, inner):
    return (f'<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8">{FONTS}'
            f'<style>{ROOT_CSS}\n{fmt_css}</style></head><body>{inner}</body></html>')

# Cytaty autentyczne. (tekst, dzielnica, klasa-dlugosci-kwadrat)
CYTATY = [
    ("Wiadukt to jedyna brama z Jeżyc na Sołacz &mdash; i zarazem wąskie gardło.", "Jeżyce", "len-m"),
    ("Dwa wózki się nie miną &mdash; ludzie się blokują, przeciskają i przepychają.", "Jeżyce", "len-l"),
    ("Aktualne przejście na Kościelnej jest okropne.", "Jeżyce", "len-s"),
    ("To absurd, żeby dzieci jeździły rowerkami do parku wzdłuż Niestachowskiej.", "Jeżyce", "len-m"),
    ("Moją pracę i mieszkanie dzielą właśnie te tory.", "Sołacz", "len-s"),
    ("Każde przejście do parku z dzieckiem to stanie w kolejce pod wiaduktem.", "Jeżyce", "len-m"),
]

# Mapowanie klasy dlugosci dla formatu poziom/story (krotsze fonty -> czesto o stopien luzniej)
def shift(length, step):
    order = ["len-s","len-m","len-l","len-xl"]
    i = max(0, min(len(order)-1, order.index(length)+step))
    return order[i]

jobs = []  # (plik_html, dims, png)
# KWADRAT: wszystkie 6
for i,(q,by,ln) in enumerate(CYTATY, 1):
    f = os.path.join(BUILD, f"kwadrat-{i:02d}.html")
    open(f,"w",encoding="utf-8").write(page(KWADRAT_CSS, card_kwadrat_story(q,by,ln)))
    jobs.append((f, "1080,1080", f"cytat-kwadrat-{i:02d}.png"))

# STORY: karty krotkie (1,3,5) — najlepsze na Stories
for i in (1,3,5):
    q,by,ln = CYTATY[i-1]
    f = os.path.join(BUILD, f"story-{i:02d}.html")
    open(f,"w",encoding="utf-8").write(page(STORY_CSS, card_kwadrat_story(q,by,ln)))
    jobs.append((f, "1080,1920", f"cytat-story-{i:02d}.png"))

# POZIOM: karty 1,2,6 (uniwersalne do artykulow / OG)
for i in (1,2,6):
    q,by,ln = CYTATY[i-1]
    f = os.path.join(BUILD, f"poziom-{i:02d}.html")
    open(f,"w",encoding="utf-8").write(page(POZIOM_CSS, card_poziom(q,by,shift(ln,-1) if ln!="len-s" else ln)))
    jobs.append((f, "1200,630", f"cytat-poziom-{i:02d}.png"))

# zapisz liste zadan dla render.sh
with open(os.path.join(BUILD,"jobs.tsv"),"w",encoding="utf-8") as fh:
    for html_f, dims, png in jobs:
        fh.write(f"{html_f}\t{dims}\t{png}\n")
print(f"Wygenerowano {len(jobs)} kart HTML w {BUILD}")
