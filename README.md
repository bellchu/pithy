<p align="center">
  <img src="docs/hero.svg" alt="Pithy — quiet workflow control for Codex" width="100%">
</p>

<div align="center">

# Pithy

**Quiet decisions. Grounded evidence. Clean recovery.**

[![Validate](https://github.com/bellchu/pithy/actions/workflows/validate.yml/badge.svg)](https://github.com/bellchu/pithy/actions/workflows/validate.yml)
[![Codex Skill](https://img.shields.io/badge/Codex-skill-8B5CF6?logo=openai&logoColor=white)](./skills/pithy/SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-22D3EE.svg)](./LICENSE)

Pithy is a Codex workflow skill for selective exploration, evidence-grounded verification, and structural replanning. Clear tasks stay direct; complex tasks get only the extra work that can change the decision.

</div>

## How it behaves

- **Select:** diverge only when competing mechanisms materially matter.
- **Verify:** reuse valid evidence and avoid equivalent re-checks.
- **Recover:** stop local patching when assumptions fail; request approval before crossing boundaries.

```mermaid
stateDiagram-v2
    [*] --> OPEN
    OPEN --> DIVERGE: material ambiguity
    OPEN --> VERIFY: selected artifact
    DIVERGE --> SELECTED
    SELECTED --> VERIFY
    VERIFY --> CLOSED: sufficient evidence
    VERIFY --> REPLAN_REQUIRED: structural blocker
    REPLAN_REQUIRED --> OPEN: new in-scope delta
    REPLAN_REQUIRED --> WAITING_APPROVAL: boundary expansion
    WAITING_APPROVAL --> OPEN: approved
    REPLAN_REQUIRED --> INCOMPLETE: no viable delta
```

## Install

```bash
git clone https://github.com/bellchu/pithy.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R pithy/skills/pithy "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex or begin a new session, then invoke:

```text
$pithy compare approaches for this migration
$pithy verify this implementation against its acceptance criteria
```

## Design rule

> Add a branch, check, repair, or replan only when it can resolve a decision-relevant uncertainty.

Pithy favors low-noise communication and lower total work, but never uses brevity to hide material evidence, risk, or required authority.

## License

[MIT](./LICENSE) © 2026 Bell Zhu. The divergence pattern is adapted from [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) under MIT.
