"""Proves the guardrails actually fail on bad input. Run: python tests/test_check.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
import check  # noqa: E402

GOOD = "Dear team,\nI played football in the third tier.\nKind regards"

# banned phrases
assert check.banned_in("I am a passionate about data team player") == ["passionate about", "team player"]
assert check.banned_in("Dynamic Pricing & Segmentation") == []  # the project name is allowed

# numbers must exist in a data file; single digits are noise
assert check.untraceable_numbers("cut 86,416 to 11,351 tokens, 99.9% better", "86,416 11,351") == ["99.9"]
assert check.untraceable_numbers("3 projects", "") == []

# the toolbar is not CV content, but the CV text is
page = '<style>a{x:9.5pt}</style><div id="bar">9.5pt</div><p>Cut 40%</p>'
assert check.visible_text(page).split() == ["Cut", "40%"]

# letters
assert check.letter_problems(GOOD) == []
assert "no football sentence (always required)" in check.letter_problems("Dear team, hello")
assert "contains an em dash" in check.letter_problems(GOOD + " — and more")
assert any("words, limit" in p for p in check.letter_problems(GOOD + " word" * 300))
assert any("banned phrase" in p for p in check.letter_problems(GOOD + " I am a team player"))
assert any("unresolved" in p for p in check.letter_problems(GOOD + " [WHY]"))
assert check.letter_problems(GOOD + " [WHY]", is_base=True) == []  # the base letter keeps its markers

# header text above the --- divider is not counted as letter body
assert check.letter_problems("notes with — a dash\n---\n" + GOOD) == []

# the skill must point at the repo and hold no facts
OK = "---\nname: x\ndescription: does a thing\n---\nsee github.com/gauravbhatia-bit/cv-builder\n"
assert check.skill_problems(OK) == []
assert any("frontmatter" in p for p in check.skill_problems("no frontmatter github.com/gauravbhatia-bit/cv-builder"))
assert any("date or year" in p for p in check.skill_problems(OK + "available from 2027"))
assert any("retired claim" in p for p in check.skill_problems(OK + "Croud Control"))
assert any("point at" in p for p in check.skill_problems("---\nname: x\ndescription: y\n---\nbody"))

# invisible characters from a broken escape sequence
assert check.has_control_chars("a" + chr(8) + "b") and not check.has_control_chars("a\tb\nc\r\n")

print("all guardrail tests passed")
