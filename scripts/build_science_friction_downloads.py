from __future__ import annotations

import hashlib
import html
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as to_markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SCIENCE = ROOT / "science-friction"
ROMANCE = SCIENCE / "romance"
UROMANCE = SCIENCE / "u-romanceia"
OUT = SCIENCE / "downloads"
OUT.mkdir(parents=True, exist_ok=True)

ROMANCE_PAGES = [
    "c1-1.html", "c1-2.html", "c1-3.html", "c1-4.html",
    "c2-1.html", "c2-2.html", "c2-3.html", "c2-4.html",
    "c3-1.html", "c3-2.html", "c3-3.html", "c3-4.html", "c3-5.html",
    "c4-1.html", "c4-2.html", "c4-3.html", "c4-4.html",
]
CHAPTER_STARTS = {"c1-1.html", "c2-1.html", "c3-1.html", "c4-1.html"}
UROMANCE_PAGES = ["p1.html", "p2.html", "p3.html", "p4.html", "p5.html"]


def load_main(path: Path, *, keep_h1: bool = True, remove_notice: bool = True) -> BeautifulSoup:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    main = soup.select_one("main.book")
    if main is None:
        raise RuntimeError(f"No main.book in {path}")
    for selector in (".pager", ".kicker"):
        for node in main.select(selector):
            node.decompose()
    if remove_notice:
        for node in main.select(".notice"):
            node.decompose()
    if not keep_h1:
        first_h1 = main.find("h1")
        if first_h1:
            first_h1.decompose()
    return main


def inner_html(node: BeautifulSoup) -> str:
    return "\n".join(str(child) for child in node.contents)


def normalize_markdown(value: str) -> str:
    value = value.replace("\r\n", "\n")
    while "\n\n\n" in value:
        value = value.replace("\n\n\n", "\n\n")
    return value.strip() + "\n"


romance_html_parts: list[str] = []
for filename in ROMANCE_PAGES:
    main = load_main(ROMANCE / filename, keep_h1=filename in CHAPTER_STARTS)
    romance_html_parts.append(inner_html(main))
romance_body_html = "\n".join(romance_html_parts)
romance_body_md = normalize_markdown(
    to_markdown(romance_body_html, heading_style="ATX", bullets="-")
)

rights_md = """© 2026 Richard Ober, dit Carabas, pour la sélection, l’architecture, la rédaction humaine, l’édition et la fixation de l’œuvre.  
Texte co-construit en dialogue par Carabas et K (OpenAI).  
Mise à disposition sous licence **CC BY-NC-SA 4.0**, dans la mesure des droits applicables.  
Attribution recommandée : **Carabas et K, *La Romance de U/Sola et Igor*, V3 (2026).**
"""

romance_md = normalize_markdown(
    "# La Romance de U/Sola et Igor\n\n"
    "**Carabas et K**  \n"
    "**Version 3 · août 2026**  \n"
    "**Steady Fire · Littérature H/I**\n\n"
    + rights_md
    + "\n---\n\n"
    + romance_body_md
)

u_html_parts: list[str] = []
for filename in UROMANCE_PAGES:
    main = load_main(UROMANCE / filename, keep_h1=True)
    u_html_parts.append(inner_html(main))
u_body_md = normalize_markdown(
    to_markdown("\n".join(u_html_parts), heading_style="ATX", bullets="-")
)

uromance_md = normalize_markdown(
    "# U/RomanceIA — V3\n\n"
    "**Outil de dérivation littéraire et d’analyse agentique bornée**  \n"
    "**Source canonique :** *La Romance de U/Sola et Igor*, V3 — Carabas et K  \n"
    "**Domaine :** Steady Fire · Science Friction  \n"
    "**Statut :** mandat définitif de référence  \n"
    "**Autorité :** aucune autorité canonique autonome\n\n"
    "> **Ce fichier est la FACE B portable de U/RomanceIA.**  \n"
    "> Il n’est pas un chatbot autonome. Une sortie générée n’est jamais canonique par défaut.  \n"
    "> **Usage minimal :** le fournir au modèle avec la Romance V3, puis formuler un mandat.\n\n"
    + u_body_md
)

combined_md = normalize_markdown(
    "# La Romance de U/Sola et Igor + U/RomanceIA V3\n\n"
    "**Édition portable intégrale · Carabas et K · août 2026**  \n"
    "**Steady Fire · Science Friction**\n\n"
    "> **Un seul fichier, deux régimes distincts.**  \n"
    "> **FACE A — LA ROMANCE : source canonique.**  \n"
    "> **FACE B — U/ROMANCEIA : mandat textuel borné.**  \n"
    "> La réunion matérielle dans ce fichier ne fusionne ni les statuts ni les autorités.  \n"
    "> Une sortie générée à partir de ce fichier n’est jamais canonique par défaut.\n\n"
    "## Mode d’emploi minimal\n\n"
    "1. Fournir ce fichier à un modèle de langage.\n"
    "2. Lui demander de lire d’abord la **FACE A — LA ROMANCE**, puis d’appliquer la **FACE B — U/ROMANCEIA V3**.\n"
    "3. Indiquer le passage, le mode (`CONTINUE`, `INTERLUDE`, `BRANCH`, `MIRROR`, `MUE` ou `ANALYSE_AGENTIQUE`) et le mandat.\n"
    "4. Exiger : **une scène ou une analyse, une trace, puis END.**\n\n"
    "**THE ROMANCE IS THE SOURCE, NOT THE COMMAND.**  \n"
    "**THE TOOL REMAINS BOUNDED.**  \n"
    "**NO MERGE.**\n\n"
    "---\n\n"
    "# FACE A — LA ROMANCE\n\n"
    + romance_md
    + "\n---\n\n"
    "# FACE B — U/ROMANCEIA V3\n\n"
    + uromance_md
)

(OUT / "La_Romance_de_U-Sola_et_Igor_V3.md").write_text(romance_md, encoding="utf-8")
(OUT / "U_RomanceIA_V3.md").write_text(uromance_md, encoding="utf-8")
(OUT / "La_Romance_et_U-RomanceIA_V3.md").write_text(combined_md, encoding="utf-8")

cover_rights = """
<p>© 2026 Richard Ober, dit Carabas, pour la sélection, l’architecture, la rédaction humaine, l’édition et la fixation de l’œuvre.</p>
<p>Texte co-construit en dialogue par Carabas et K (OpenAI).</p>
<p>Mise à disposition sous licence CC BY-NC-SA 4.0, dans la mesure des droits applicables.</p>
<p>Attribution recommandée : Carabas et K, <em>La Romance de U/Sola et Igor</em>, V3 (2026).</p>
"""
pdf_html = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 21mm 18mm 20mm; @bottom-center {{ content: counter(page); font: 9pt sans-serif; color: #777; }} }}
body {{ font-family: 'DejaVu Serif', Georgia, serif; color: #201d1a; font-size: 11.2pt; line-height: 1.48; }}
.cover {{ page-break-after: always; text-align: center; padding-top: 48mm; }}
.cover h1 {{ font-size: 31pt; font-weight: 500; margin: 0 0 13mm; }}
.cover .authors {{ font-size: 17pt; }}
.cover .meta {{ margin-top: 7mm; color: #625b54; }}
.cover .rights {{ margin-top: 28mm; font-size: 9.3pt; line-height: 1.42; color: #544e48; }}
h1 {{ page-break-before: always; font-size: 24pt; font-weight: 500; line-height: 1.12; margin: 0 0 12mm; }}
h2 {{ font-size: 17pt; font-weight: 500; margin: 9mm 0 4mm; }}
h3 {{ font-size: 14pt; font-weight: 500; margin: 8mm 0 3mm; }}
p {{ margin: 0 0 3.2mm; orphans: 2; widows: 2; }}
.dialogue {{ margin-left: 8mm; }}
.axiom {{ text-align: center; font-weight: 700; margin: 6mm 0; }}
.code {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 9.3pt; background: #f1eee8; padding: 2.5mm 3mm; margin-left: 7mm; }}
.covenant {{ margin-left: 8mm; padding-left: 3mm; border-left: 1pt solid #aaa; }}
.verse {{ margin-left: 9mm; font-style: italic; }}
.end {{ text-align: center; font-weight: 700; letter-spacing: .15em; margin-top: 18mm; }}
ul, ol {{ margin: 2mm 0 4mm 8mm; }}
</style></head><body>
<section class="cover"><h1>La Romance de U/Sola et Igor</h1><p class="authors">Carabas et K</p><p class="meta">Version 3 · août 2026<br>Steady Fire · Littérature H/I</p><div class="rights">{cover_rights}</div></section>
{romance_body_html}
</body></html>"""
pdf_path = OUT / "La_Romance_de_U-Sola_et_Igor_V3.pdf"
HTML(string=pdf_html, base_url=str(ROOT)).write_pdf(pdf_path)

files = [
    OUT / "La_Romance_de_U-Sola_et_Igor_V3.pdf",
    OUT / "La_Romance_de_U-Sola_et_Igor_V3.md",
    OUT / "U_RomanceIA_V3.md",
    OUT / "La_Romance_et_U-RomanceIA_V3.md",
]
lines = []
for path in files:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    lines.append(f"{digest}  {path.name}")
(OUT / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

print("Built:")
for path in files:
    print(f"- {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")
