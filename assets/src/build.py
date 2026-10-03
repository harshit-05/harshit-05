"""Generate the profile's animated SVGs (light + dark) into assets/.

Run from the repo root:  python assets/src/build.py

Icons in assets/src/icons/: dv-* from devicon (MIT), si-* from simple-icons (CC0).
Everything is self-contained (icons are inlined as data URIs), so the images
render inside GitHub's <img> sandbox without loading anything external.
"""
import base64
import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "assets"
ICONS = pathlib.Path(__file__).parent / "icons"

THEMES = {
    "dark": {
        "bg": "#0d1117", "bg2": "#161b22", "border": "#30363d", "fg": "#e6edf3",
        "muted": "#8b949e", "accent": "#58a6ff", "accent2": "#bc8cff",
        "accent3": "#3fb950", "tile": "#1c2128", "edge": "#30363d",
    },
    "light": {
        "bg": "#ffffff", "bg2": "#f6f8fa", "border": "#d0d7de", "fg": "#1f2328",
        "muted": "#59636e", "accent": "#0969da", "accent2": "#8250df",
        "accent3": "#1a7f37", "tile": "#f6f8fa", "edge": "#d0d7de",
    },
}

SANS = "-apple-system, 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'Cascadia Mono', Menlo, Consolas, 'Liberation Mono', monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------------- header
def header(t):
    w, h = 1200, 320
    rnd = random.Random(7)
    layers = [3, 5, 5, 3]
    xs = [780, 880, 980, 1080]
    nodes = []
    for x, n in zip(xs, layers):
        top = h / 2 - (n - 1) * 26
        nodes.append([(x, top + i * 52) for i in range(n)])
    edges = [(a, b) for l in range(len(nodes) - 1) for a in nodes[l] for b in nodes[l + 1]]

    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Harshit Deswal: Applied ML, MLOps, computer vision">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg']}"/><stop offset="1" stop-color="{t['bg2']}"/></linearGradient>
  <linearGradient id="ink" x1="0" x2="1"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient>
  <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{t['edge']}"/></pattern>
  <clipPath id="type"><rect x="60" y="214" height="34" width="0">
    <animate attributeName="width" from="0" to="480" begin="0.6s" dur="2.6s" fill="freeze"/></rect></clipPath>
</defs>
<style>
  .name {{ font: 700 60px {SANS}; fill: {t['fg']}; }}
  .sub {{ font: 600 24px {SANS}; fill: url(#ink); }}
  .mono {{ font: 400 16px {MONO}; fill: {t['muted']}; }}
  .cmd {{ font: 500 18px {MONO}; fill: {t['accent3']}; }}
  .fade {{ opacity: 0; animation: in .8s ease-out forwards; }}
  .d1 {{ animation-delay: .1s; }} .d2 {{ animation-delay: .35s; }}
  @keyframes in {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
  .cur {{ animation: blink 1s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
</style>
<rect width="{w}" height="{h}" rx="16" fill="url(#bg)"/>
<rect width="{w}" height="{h}" rx="16" fill="url(#dots)" opacity=".6"/>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="16" fill="none" stroke="{t['border']}"/>
<text x="60" y="78" class="mono fade">~/harshit-05 $ python profile.py</text>
<text x="60" y="146" class="name fade d1">Harshit Deswal</text>
<text x="60" y="190" class="sub fade d2">Applied ML · MLOps · Computer Vision</text>
<g clip-path="url(#type)"><text x="60" y="238" class="cmd">&gt; tested, reproducible, honest about limits</text></g>
<rect x="60" y="222" width="10" height="20" fill="{t['accent3']}" class="cur">
  <animate attributeName="x" from="60" to="528" begin="0.6s" dur="2.6s" fill="freeze"/></rect>
''']
    # network
    parts.append(f'<g stroke="{t["edge"]}" stroke-width="1">')
    for (x1, y1), (x2, y2) in edges:
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    parts.append("</g>")
    # signals travelling input -> output along random paths
    for i in range(9):
        path = [rnd.choice(layer) for layer in nodes]
        d = "M" + " L".join(f"{x},{y}" for x, y in path)
        color = t["accent"] if i % 2 else t["accent2"]
        begin = round(i * 0.45, 2)
        parts.append(
            f'<circle r="3.5" fill="{color}" opacity="0"><animateMotion path="{d}" dur="2.4s" begin="{begin}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.85;1" dur="2.4s" begin="{begin}s" repeatCount="indefinite"/></circle>'
        )
    for li, layer in enumerate(nodes):
        for ni, (x, y) in enumerate(layer):
            delay = round((li * 0.6 + ni * 0.15) % 2.4, 2)
            parts.append(
                f'<circle cx="{x}" cy="{y}" r="9" fill="{t["bg2"]}" stroke="{t["accent"] if li in (0, 3) else t["accent2"]}" stroke-width="2">'
                f'<animate attributeName="stroke-opacity" values=".35;1;.35" dur="2.4s" begin="{delay}s" repeatCount="indefinite"/></circle>'
            )
    labels = [("input", xs[0]), ("hidden", (xs[1] + xs[2]) / 2), ("output", xs[3])]
    for text, x in labels:
        parts.append(f'<text x="{x}" y="{h - 34}" text-anchor="middle" class="mono" style="font-size:13px">{text}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


# ------------------------------------------------------------------- terminal
TERMINAL = [
    ("$ whoami", "cmd"),
    ("Harshit Deswal · B.Tech CS & Communication Eng. · class of 2027", "out"),
    ("$ cat now.md", "cmd"),
    ("AI/Software Engineer intern @ Teemo.ai (remote)", "out"),
    ("$ cat before.md", "cmd"),
    ("AI/ML research intern @ DRDO Young Scientist Lab", "out"),
    ("$ ls interests/", "cmd"),
    ("applied-ml/  mlops/  rag/  computer-vision/  slam/", "dir"),
]


def terminal(t):
    w, line_h, top = 640, 30, 74
    h = top + line_h * (len(TERMINAL) + 1) + 10
    rows = []
    for i, (txt, kind) in enumerate(TERMINAL):
        y = top + i * line_h
        fill = {"cmd": t["accent3"], "out": t["fg"], "dir": t["accent"]}[kind]
        rows.append(
            f'<text x="24" y="{y}" fill="{fill}" class="l" style="animation-delay:{0.3 + i * 0.45:.2f}s">{esc(txt)}</text>'
        )
    cy = top + len(TERMINAL) * line_h
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="whoami terminal">
<style>
  .l {{ font: 400 14.5px {MONO}; opacity: 0; animation: show .01s forwards; }}
  @keyframes show {{ to {{ opacity: 1; }} }}
  .cur {{ opacity: 0; animation: show .01s {0.3 + len(TERMINAL) * 0.45:.2f}s forwards, blink 1s {0.3 + len(TERMINAL) * 0.45:.2f}s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
</style>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12" fill="{t['bg2']}" stroke="{t['border']}"/>
<path d="M.5 40.5h{w-1}" stroke="{t['border']}"/>
<circle cx="22" cy="20" r="6" fill="#ff5f57"/><circle cx="42" cy="20" r="6" fill="#febc2e"/><circle cx="62" cy="20" r="6" fill="#28c840"/>
<text x="{w/2}" y="25" text-anchor="middle" fill="{t['muted']}" style="font:400 13px {MONO}">harshit@arch: ~</text>
{chr(10).join(rows)}
<text x="24" y="{cy}" fill="{t['accent3']}" class="l" style="animation-delay:{0.3 + len(TERMINAL) * 0.45:.2f}s">$</text>
<rect x="40" y="{cy - 14}" width="9" height="18" fill="{t['accent3']}" class="cur"/>
</svg>'''


# ---------------------------------------------------------------------- stack
STACK = [
    ("Languages", [("Python", "dv-python"), ("Java", "dv-java"), ("C", "dv-c"), ("SQL", None)]),
    ("ML & vision", [("PyTorch", "dv-pytorch"), ("OpenCV", "dv-opencv"), ("YOLOv8", "si-ultralytics")]),
    ("LLMs & RAG", [("LangChain", "si-langchain"), ("Ollama", "si-ollama"), ("Hugging Face", "si-huggingface"), ("FAISS", None)]),
    ("Backend", [("FastAPI", "dv-fastapi"), ("PostgreSQL", "dv-postgresql"), ("SQLAlchemy", "dv-sqlalchemy"), ("Pydantic", "si-pydantic")]),
    ("Ship & run", [("Docker", "dv-docker"), ("AWS", "dv-amazonwebservices"), ("GitHub Actions", "dv-githubactions"), ("Arch Linux", "dv-archlinux"), ("Git", "dv-git"), ("uv", "si-uv"), ("pytest", "dv-pytest")]),
]
SI_COLORS = {"si-ultralytics": "#111F68", "si-huggingface": "#FFD21E", "si-pydantic": "#E92063", "si-uv": "#DE5FE9"}


def icon_uri(name, t):
    svg = (ICONS / f"{name}.svg").read_text()
    if name.startswith("si-"):
        color = SI_COLORS.get(name, t["fg"])
        if name == "si-ultralytics" and t is THEMES["dark"]:
            color = "#4F7DF3"
        svg = svg.replace("<svg ", f'<svg fill="{color}" ', 1)
    if name == "dv-amazonwebservices" and t is THEMES["dark"]:
        svg = svg.replace("#252f3e", t["fg"])
    if name in ("dv-sqlalchemy",) and t is THEMES["dark"]:
        svg = svg.replace("#333", "#cfcfcf")
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def stack(t):
    tile, gap, label_w, row_h = 72, 14, 150, 112
    cols = max(len(items) for _, items in STACK)
    w = label_w + cols * (tile + gap) + 20
    h = len(STACK) * row_h + 20
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Tech stack">
<style>
  .cat {{ font: 600 15px {SANS}; fill: {t['fg']}; }}
  .lab {{ font: 400 11.5px {SANS}; fill: {t['muted']}; }}
  .txt {{ font: 700 17px {MONO}; fill: {t['accent']}; }}
  .t {{ opacity: 0; animation: pop .5s ease-out forwards; transform-box: fill-box; transform-origin: center; }}
  @keyframes pop {{ from {{ opacity: 0; transform: scale(.85); }} to {{ opacity: 1; transform: none; }} }}
</style>''']
    k = 0
    for r, (cat, items) in enumerate(STACK):
        y = 10 + r * row_h
        out.append(f'<text x="8" y="{y + tile / 2 + 5}" class="cat">{esc(cat)}</text>')
        for c, (name, icon) in enumerate(items):
            x = label_w + c * (tile + gap)
            out.append(f'<g class="t" style="animation-delay:{k * 0.06:.2f}s">')
            out.append(f'<rect x="{x}" y="{y}" width="{tile}" height="{tile}" rx="14" fill="{t["tile"]}" stroke="{t["border"]}"/>')
            if icon:
                out.append(f'<image x="{x + 16}" y="{y + 16}" width="40" height="40" href="{icon_uri(icon, t)}"/>')
            else:
                out.append(f'<text x="{x + tile / 2}" y="{y + tile / 2 + 6}" text-anchor="middle" class="txt">{name}</text>')
            out.append(f'<text x="{x + tile / 2}" y="{y + tile + 18}" text-anchor="middle" class="lab">{esc(name)}</text></g>')
            k += 1
    out.append("</svg>")
    return "\n".join(out)


# --------------------------------------------------------------------- footer
def footer(t):
    w, h = 1200, 120
    wave = "M0 60 Q 150 20 300 60 T 600 60 T 900 60 T 1200 60 T 1500 60 T 1800 60 T 2100 60 T 2400 60 V 120 H 0 Z"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" preserveAspectRatio="none" role="img" aria-label="">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient></defs>
<path d="{wave}" fill="url(#g)" opacity=".35"><animateTransform attributeName="transform" type="translate" from="0 0" to="-600 0" dur="9s" repeatCount="indefinite"/></path>
<path d="{wave}" fill="url(#g)" opacity=".6" transform="translate(-150 14)"><animateTransform attributeName="transform" type="translate" from="-150 14" to="-750 14" dur="6s" repeatCount="indefinite"/></path>
</svg>'''


def main():
    from scenes import SCENES

    for name, theme in THEMES.items():
        for part, fn in (("header", header), ("terminal", terminal), ("stack", stack), ("footer", footer)) + SCENES:
            (OUT / f"{part}-{name}.svg").write_text(fn(theme))
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))


if __name__ == "__main__":
    main()
