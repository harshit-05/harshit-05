"""Illustrative animated scenes: tracking, RAG retrieval, training curve, divider.

These are illustrations of how the projects work, not recordings of real output.
"""
import math
import random

from build import MONO, SANS, THEMES


def person(x, y, s, color, stride=0.9):
    """A simple walking figure whose feet are at (x, y), scaled by s."""
    leg = (
        '<rect x="{x}" y="-24" width="7" height="24" rx="3" fill="{c}">'
        '<animateTransform attributeName="transform" type="rotate" values="{a} {p} -24;{b} {p} -24;{a} {p} -24" dur="{d}s" repeatCount="indefinite"/></rect>'
    )
    return (
        f'<g transform="translate({x} {y}) scale({s})">'
        f'<circle cx="0" cy="-62" r="9" fill="{color}"/>'
        f'<rect x="-11" y="-51" width="22" height="30" rx="8" fill="{color}"/>'
        + leg.format(x=-9, c=color, a=-12, b=12, p=-5, d=stride)
        + leg.format(x=2, c=color, a=12, b=-12, p=5, d=stride)
        + "</g>"
    )


def tracking(t):
    w, h = 480, 300
    red = "#f85149" if t is THEMES["dark"] else "#cf222e"
    fig = t["muted"]
    # (track id, ground y, scale, duration s, start offset s, confidence, suspect)
    walkers = [
        (4, 178, 0.7, 16, -11, "0.79", False),
        (2, 200, 0.8, 14, -5, "0.88", True),
        (1, 238, 1.0, 11, 0, "0.91", False),
        (3, 268, 1.15, 9, -6, "0.94", False),
    ]
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Illustration: people tracked with bounding boxes and IDs, one marked as suspect with a zoomed view">
<style>
  .lbl {{ font: 600 10px {MONO}; }}
  .hud {{ font: 500 11px {MONO}; fill: {t['muted']}; }}
  .rec {{ animation: blink 1.2s steps(1) infinite; }}
  @keyframes blink {{ 50% {{ opacity: 0; }} }}
</style>
<defs><clipPath id="frame"><rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="12"/></clipPath></defs>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="12" fill="{t['bg2']}" stroke="{t['border']}"/>
<g clip-path="url(#frame)">
<g stroke="{t['edge']}" stroke-width="1">''']
    for i in range(7):
        out.append(f'<line x1="{-200 + i * 140}" y1="{h}" x2="{180 + i * 20}" y2="140"/>')
    out.append(f'<line x1="0" y1="140" x2="{w}" y2="140"/></g>')
    for tid, gy, s, dur, off, conf, sus in walkers:
        col = red if sus else t["accent"]
        bw, bh = 34 * s, 80 * s
        label = f"SUSPECT #{tid}" if sus else f"person {conf} #{tid}"
        lw = len(label) * 6.2 + 8
        out.append(
            f'<g><animateTransform attributeName="transform" type="translate" from="-80 0" to="{w + 80} 0" dur="{dur}s" begin="{off}s" repeatCount="indefinite"/>'
            + person(0, gy, s, fig)
            + f'<rect x="{-bw / 2:.1f}" y="{gy - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{col}" fill-opacity=".08" stroke="{col}" stroke-width="{2 if sus else 1.5}"/>'
            f'<rect x="{-bw / 2:.1f}" y="{gy - bh - 15:.1f}" width="{lw:.1f}" height="15" fill="{col}"/>'
            f'<text x="{-bw / 2 + 4:.1f}" y="{gy - bh - 4:.1f}" class="lbl" fill="{t["bg"]}">{label}</text></g>'
        )
    out.append(f'''<rect x="0" y="0" width="{w}" height="3" fill="{t['accent']}" opacity=".25"><animate attributeName="y" from="0" to="{h}" dur="3.5s" repeatCount="indefinite"/></rect>
</g>
<circle cx="20" cy="22" r="5" fill="{red}" class="rec"/>
<text x="32" y="26" class="hud">CAM 02 · REC</text>
<text x="16" y="{h - 14}" class="hud">YOLOv8 → DeepSORT</text>
<g transform="translate({w - 136} 14)">
  <rect width="122" height="96" rx="6" fill="{t['bg']}" stroke="{red}" stroke-width="2"/>
  <g transform="translate(61 92)">{person(0, 0, 1.0, fig, stride=1.12)}</g>
  <rect x="0" y="0" width="64" height="15" fill="{red}"/>
  <text x="5" y="11" class="lbl" fill="{t['bg']}">PiP · #2</text>
</g>
</svg>''')
    return "\n".join(out)


def rag(t):
    w, h, cyc = 480, 300, 9
    rnd = random.Random(3)
    q = (330, 120)
    pts = [(rnd.uniform(215, 455), rnd.uniform(52, 200)) for _ in range(34)]
    near = sorted(pts, key=lambda p: (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)[:5]
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Illustration: a question is embedded, the five nearest chunks are retrieved and a cited answer is generated">
<style>
  .s {{ font: 500 11px {MONO}; fill: {t['muted']}; }}
  .q {{ font: 500 12px {SANS}; fill: {t['fg']}; }}
  .a {{ font: 400 11.5px {SANS}; fill: {t['fg']}; }}
  .c {{ font: 600 11px {MONO}; fill: {t['accent']}; }}
  .k1 {{ animation: k1 {cyc}s infinite; }} .k2 {{ animation: k2 {cyc}s infinite; }}
  .k3 {{ animation: k3 {cyc}s infinite; }} .k4 {{ animation: k4 {cyc}s infinite; }}
  @keyframes k1 {{ 0%,4% {{ opacity: 0; }} 8%,92% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
  @keyframes k2 {{ 0%,18% {{ opacity: 0; }} 24%,92% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
  @keyframes k3 {{ 0%,34% {{ opacity: 0; }} 42%,92% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
  @keyframes k4 {{ 0%,52% {{ opacity: 0; }} 60%,92% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
</style>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="12" fill="{t['bg2']}" stroke="{t['border']}"/>
<text x="16" y="28" class="s">1 · question</text>
<g class="k1"><rect x="16" y="40" width="180" height="58" rx="10" fill="{t['bg']}" stroke="{t['border']}"/>
<text x="28" y="64" class="q">How does the system detect</text><text x="28" y="82" class="q">crowds and threats?</text></g>
<text x="214" y="28" class="s">2 · embed + nearest chunks (FAISS)</text>
<rect x="206" y="40" width="258" height="170" rx="10" fill="none" stroke="{t['border']}" stroke-dasharray="4 4"/>''']
    for x, y in pts:
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{t["edge"]}"/>')
    out.append('<g class="k3">')
    for x, y in near:
        out.append(
            f'<line x1="{q[0]}" y1="{q[1]}" x2="{x:.1f}" y2="{y:.1f}" stroke="{t["accent2"]}" stroke-width="1.2"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="none" stroke="{t["accent2"]}" stroke-width="2"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{t["accent2"]}"/>'
        )
    out.append(f'''</g>
<g class="k2"><path d="M196 69 C 250 69, 260 {q[1]}, {q[0] - 10} {q[1]}" fill="none" stroke="{t['accent']}" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="{q[0]}" cy="{q[1]}" r="7" fill="{t['accent']}"><animate attributeName="r" values="6;9;6" dur="1.4s" repeatCount="indefinite"/></circle></g>
<text x="16" y="232" class="s">3 · local LLM answers from the top 5 chunks</text>
<g class="k4"><rect x="16" y="242" width="448" height="44" rx="10" fill="{t['bg']}" stroke="{t['border']}"/>
<text x="28" y="261" class="a">Object detection plus anomaly recognition: people are counted</text>
<text x="28" y="277" class="a">and tracked across frames …  <tspan class="c">[1] p.10  [2] p.3</tspan></text></g>
</svg>''')
    return "\n".join(out)


def training(t):
    w, h = 480, 220
    x0, y0, x1, y1 = 48, 30, 460, 180
    n = 50

    def curve(f):
        return "M" + " L".join(
            f"{x0 + (x1 - x0) * i / n:.1f},{y0 + (y1 - y0) * (1 - f(i)):.1f}" for i in range(n + 1)
        )

    tr = curve(lambda i: 0.08 + 0.9 * math.exp(-i / 9))
    va = curve(lambda i: 0.16 + 0.82 * math.exp(-i / 11) + 0.0009 * max(0, i - 30) ** 1.6)
    grid = "".join(
        f'<line x1="{x0}" y1="{y0 + k * 37.5}" x2="{x1}" y2="{y0 + k * 37.5}" stroke="{t["edge"]}" stroke-dasharray="3 4"/>'
        for k in range(5)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Illustration: training and validation loss curves drawing over 50 epochs">
<style>
  .s {{ font: 500 11px {MONO}; fill: {t['muted']}; }}
  .ln {{ fill: none; stroke-width: 2.4; stroke-linecap: round; stroke-dasharray: 1; stroke-dashoffset: 1; animation: draw 7s ease-in-out infinite; }}
  @keyframes draw {{ 0% {{ stroke-dashoffset: 1; opacity: 1; }} 70%,90% {{ stroke-dashoffset: 0; opacity: 1; }} 100% {{ stroke-dashoffset: 0; opacity: 0; }} }}
  .bar {{ animation: fill 7s ease-in-out infinite; transform-box: fill-box; transform-origin: left; }}
  @keyframes fill {{ 0% {{ transform: scaleX(0); }} 70%,100% {{ transform: scaleX(1); }} }}
</style>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="12" fill="{t['bg2']}" stroke="{t['border']}"/>
{grid}
<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{t['border']}"/>
<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" stroke="{t['border']}"/>
<text x="14" y="{y0 + 4}" class="s">1.0</text><text x="14" y="{y1 + 4}" class="s">0.0</text>
<path d="{tr}" pathLength="1" class="ln" stroke="{t['accent']}"/>
<path d="{va}" pathLength="1" class="ln" stroke="{t['accent2']}"/>
<text x="{x1 - 150}" y="{y0 + 4}" class="s"><tspan fill="{t['accent']}">― loss</tspan>   <tspan fill="{t['accent2']}">― val_loss</tspan></text>
<text x="{x0}" y="{h - 14}" class="s">epoch 1 → 50</text>
<rect x="{x0 + 110}" y="{h - 24}" width="{x1 - x0 - 110}" height="8" rx="4" fill="{t['edge']}"/>
<rect x="{x0 + 110}" y="{h - 24}" width="{x1 - x0 - 110}" height="8" rx="4" fill="{t['accent3']}" class="bar"/>
</svg>'''


def divider(t):
    w, h = 1200, 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" preserveAspectRatio="none" role="img" aria-label="">
<defs>
  <linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{t['accent']}"/><stop offset="1" stop-color="{t['accent2']}"/></linearGradient>
  <linearGradient id="shine" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".8"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
</defs>
<rect y="3" width="{w}" height="2" rx="1" fill="url(#g)" opacity=".7"/>
<rect y="2" width="160" height="4" rx="2" fill="url(#shine)"><animate attributeName="x" from="-160" to="{w}" dur="4s" repeatCount="indefinite"/></rect>
</svg>'''


SCENES = (("tracking", tracking), ("rag", rag), ("training", training), ("divider", divider))
