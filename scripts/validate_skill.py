#!/usr/bin/env python3

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "pithy"
SKILL_MD = SKILL_DIR / "SKILL.md"
AGENT_YAML = SKILL_DIR / "agents" / "openai.yaml"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


skill_text = SKILL_MD.read_text(encoding="utf-8")
match = re.match(r"^---\n(.*?)\n---", skill_text, re.DOTALL)
require(match is not None, "SKILL.md must start with YAML frontmatter")

frontmatter = yaml.safe_load(match.group(1))
require(set(frontmatter) == {"name", "description"}, "frontmatter must contain only name and description")
require(frontmatter["name"] == "pithy", "skill name must be pithy")
require("$pithy" in frontmatter["description"], "description must include the explicit trigger")

for marker in (
    "Information-gain gate",
    "DIVERGE",
    "VERIFY",
    "REPLAN_REQUIRED",
    "WAITING_APPROVAL",
    "INCOMPLETE",
):
    require(marker in skill_text, f"missing workflow marker: {marker}")

agent = yaml.safe_load(AGENT_YAML.read_text(encoding="utf-8"))
require(agent["interface"]["display_name"] == "Pithy", "display name must be Pithy")
require("$pithy" in agent["interface"]["default_prompt"], "default prompt must invoke $pithy")

combined = skill_text + AGENT_YAML.read_text(encoding="utf-8")
require("psycho" not in combined.lower(), "legacy name remains in the installable skill")
require("60 words" not in combined.lower(), "hard output budget remains in the skill")
require("max_total_tokens" not in combined, "hard token cap remains in the skill")

print("Pithy skill contract is valid")
