#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generuje warstwy tekstowe (transparent PNG przez Chrome) dla video packu.
   Tekst renderowany przez Chrome -> prawdziwe fonty marki (Bricolage + IBM Plex),
   bo ffmpeg drawtext nie ma tych fontow lokalnie. Faktografia 1:1 ze strona."""
import os
SRC = os.path.dirname(os.path.abspath(__file__))

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800'
         '&family=IBM+Plex+Sans:wght@500;600&display=swap" rel="stylesheet">')

def pion(body_html, base="", w=1080, h=1920):
    css = """*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%dpx;height:%dpx;background:transparent;overflow:hidden}
.stage{position:relative;width:%dpx;height:%dpx;display:flex;flex-direction:column;justify-content:flex-end;font-family:"IBM Plex Sans",sans-serif}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,transparent 50%%,rgba(15,17,21,.85) 100%%)}
.top{position:absolute;top:64px;left:64px;display:flex;align-items:center;gap:16px;font-weight:600;font-size:30px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.5)}
.dot{width:24px;height:24px;border-radius:50%%;background:#d8362a;box-shadow:0 0 0 8px rgba(216,54,42,.30)}
.body{position:relative;padding:0 70px 230px}
h1{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:104px;line-height:.96;letter-spacing:-.02em;color:#fff;text-shadow:0 4px 30px rgba(0,0,0,.6);max-width:13ch}
h1.red{color:#ff6b5e}
.dom{margin-top:26px;font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:62px;color:#fff;letter-spacing:-.01em}
.dom span{color:#ff6b5e}
.ai{position:absolute;bottom:56px;right:64px;font-size:20px;font-weight:500;letter-spacing:.04em;color:#fff;opacity:.6;text-transform:uppercase;text-shadow:0 2px 10px rgba(0,0,0,.6)}""" % (w,h,w,h)
    return (f'<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8">{FONTS}<style>{css}</style></head>'
            f'<body><div class="stage"><div class="fade"></div>'
            f'<div class="top"><span class="dot"></span><span>Jeżyce ↔ Sołacz</span></div>'
            f'{body_html}<div class="ai">wizualizacja AI</div></div></body></html>')

# KLIP A — overlaye scen
scenes = {
    "overlay-A-s1": '<div class="body"><h1>Tory dzielą Jeżyce i Sołacz.</h1></div>',
    "overlay-A-s2": '<div class="body"><h1>Miasto wpisało przejście do planu w 2024.</h1></div>',
    "overlay-A-s3": '<div class="body"><h1 class="red">Wciąż go nie ma.</h1></div>',
    "overlay-A-s4": '<div class="body"><h1>Poprzyj &mdash; to 30 sekund.</h1>'
                    '<div class="dom">jezyce-solacz<span>.</span>pl</div></div>',
}
for name, body in scenes.items():
    open(os.path.join(SRC, name+".html"), "w", encoding="utf-8").write(pion(body))

# KLIP D — pasek dolny na kwadrat 1080x1080
d_css = """*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1080px;background:transparent;overflow:hidden}
.stage{position:relative;width:1080px;height:1080px;font-family:"IBM Plex Sans",sans-serif}
.fade{position:absolute;left:0;right:0;bottom:0;height:340px;background:linear-gradient(180deg,transparent,rgba(15,17,21,.88))}
.bar{position:absolute;left:0;right:0;bottom:0;padding:0 56px 56px;color:#fff}
.dot{display:inline-block;width:18px;height:18px;border-radius:50%;background:#d8362a;box-shadow:0 0 0 6px rgba(216,54,42,.3);vertical-align:middle;margin-right:14px}
.t{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:60px;line-height:1;letter-spacing:-.02em;text-shadow:0 3px 18px rgba(0,0,0,.6)}
.t span{color:#ff6b5e}
.s{margin-top:16px;font-size:30px;font-weight:600;opacity:.95}"""
d_html = ('<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8">'+FONTS+
          '<style>'+d_css+'</style></head><body><div class="stage"><div class="fade"></div>'
          '<div class="bar"><div class="t">Połączmy Jeżyce z <span>Sołaczem</span></div>'
          '<div class="s"><span class="dot"></span>jezyce-solacz.pl · wizualizacja AI</div></div></div></body></html>')
open(os.path.join(SRC, "overlay-D-pasek.html"), "w", encoding="utf-8").write(d_html)

print("Overlaye gotowe:", ", ".join(list(scenes)+["overlay-D-pasek"]))
