"""Turn a checked letter (markdown) into the designed letter page, with the same photo header as the CV.

    python scripts/build_letter.py out/Gaurav_Bhatia_Letter_<Company>.md ["Company name"]

Writes out/Gaurav_Bhatia_Letter_<Company>.html next to it; render.cmd then makes the PDF.
The .md stays the source of the wording, so check.py's letter rules still apply to it.
"""
import datetime
import html
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def build(md_path, company=None):
    md = pathlib.Path(md_path)
    text = md.read_text(encoding="utf-8").replace("\r\n", "\n")
    if "\n---\n" in text:  # notes above the divider are not part of the letter
        text = text.split("\n---\n", 1)[1]
    paras = [" ".join(p.split()) for p in text.strip().split("\n\n") if p.strip()]
    company = company or md.stem.split("Letter_", 1)[-1].replace("_", " ")
    sign = paras[-1] if paras and paras[-1].lower().startswith(("kind regards", "best regards")) else None
    if sign:
        paras = paras[:-1]
    body = "\n".join(f"    <p>{html.escape(p)}</p>" for p in paras)
    if sign:
        closing, _, name = sign.partition(" Gaurav")
        body += f'\n    <p class="sign">{html.escape(closing)}<br>Gaurav{html.escape(name)}</p>'
    d = datetime.date.today()
    page = (ROOT / "templates" / "letter.html").read_text(encoding="utf-8")
    page = (page.replace("[TITLE]", f"Gaurav Bhatia Cover Letter {company}")
                .replace("[RECIPIENT]", html.escape(f"{company}, Hiring Team"))
                .replace("[DATE]", f"{d.day} {d:%B %Y}")
                .replace("[LETTER_BODY]", body))
    out = md.with_suffix(".html")
    out.write_text(page, encoding="utf-8")
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    print(build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
