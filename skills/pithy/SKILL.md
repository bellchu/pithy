---
name: pithy
description: "Route open-ended, ambiguous-done, or failure-prone tasks through selective exploration, evidence-grounded verification, and structural replanning with concise, risk-proportionate communication. Use for explicit $pithy requests, brainstorming, comparing approaches, fuzzy debugging, ambiguous completion, or repeated-check requests. Prefer direct execution for bounded tasks, reuse evidence and context, and defer to domain-required high-assurance checks."
---

# Pithy

Coordinate selective exploration, bounded verification, and structural recovery. Make work quieter and easier to trust. Treat lower token use as a consequence of avoiding work that cannot change the decision, never as a hard cap or a reason to hide material evidence.

## Operating principles

- Route clear, bounded work directly; do not charge every task for the full workflow.
- Explore only uncertainties whose resolution could materially change the choice.
- Verify selected artifacts with observable evidence and reuse still-valid results.
- Stop local patching automatically when a load-bearing assumption fails; let the user authorize boundary expansion.
- Keep communication concise by default and proportionate to risk, complexity, and the requested deliverable.
- Optimize total work to a correct closure, including subagents, retries, verification, and replanning—not only visible output.

## State machine

Use these valid paths:

- `OPEN -> CLOSED` for a direct answer or decision when no artifact verification is requested.
- `OPEN -> VERIFY -> CLOSED` when a selected artifact exists or direct work produces one.
- `OPEN -> DIVERGE -> SELECTED -> CLOSED` when exploration or a decision alone is requested.
- `OPEN -> DIVERGE -> SELECTED -> VERIFY -> CLOSED` when exploration and verification both apply.
- `VERIFY -> REPLAN_REQUIRED -> OPEN` when structural failure reveals a new in-scope constraint or viable mechanism.
- `REPLAN_REQUIRED -> WAITING_APPROVAL -> OPEN` when replanning needs new authority and the user approves it.
- `VERIFY`, `REPLAN_REQUIRED`, or `WAITING_APPROVAL` may end at `INCOMPLETE` when evidence, authority, or a viable route is unavailable.

Apply these transition rules:

- Never activate `DIVERGE` and `VERIFY` concurrently.
- Require a concrete artifact, decision, or plan before entering `VERIFY`.
- Treat scoped repair as an action inside `VERIFY`, not as a state.
- Return to `OPEN` only with a material delta: changed evidence, constraint, scope, artifact, or mechanism. Otherwise stop `INCOMPLETE`.
- Reopen `CLOSED` or `INCOMPLETE` only for changed requirements or artifacts, invalid or ambiguous evidence, a reproducible new symptom, granted authority, or a concrete newly identified risk.

## Route for proportional effort

1. Treat explicit `$pithy` invocation as activation of the router, not as automatic divergence.
2. Stay in `OPEN` and work directly when the task has a standard low-reversal path and little material ambiguity.
3. Enter `DIVERGE` only when multiple credible mechanisms exist and premature commitment has meaningful rework or risk.
4. Enter `VERIFY` when an artifact or decision has been selected and evidence can change its completion status.
5. When both modes apply, finish divergence and selection before verification.
6. Treat repeated checking of unchanged evidence as a closure case, not new work.

## Information-gain gate

Before adding a branch, check, repair, or replan, identify internally:

- the unresolved acceptance criterion or load-bearing uncertainty;
- the distinct evidence or mechanism the action can add; and
- the decision or status that could change as a result.

Skip the action when no credible decision delta exists. Do not repeat an equivalent branch, command, verifier, repair, or explanation for reassurance.

## DIVERGE

### Freeze the brief

Create a compact brief containing only the problem, fixed constraints, success conditions, relevant evidence pointers, and any mechanism excluded by a prior failure. Exclude preferences, branch transcripts, unrelated history, and raw logs.

### Explore adaptively

- Choose frames that challenge different load-bearing assumptions.
- Use isolated subagents only when at least two distinct frames could change the selection and the likely cost of premature commitment exceeds the exploration overhead.
- Use the fewest parallel branches that cover those frames; do not target a branch count for its own sake.
- When context controls are available, give each branch no prior turns—only the frozen brief, one frame, and the generation instruction.
- If fewer than two useful isolated frames exist, use one local multi-frame pass and do not claim independence.
- Stop exploration when another frame would not test a new assumption or alter the leading decision.

Give isolated branches this instruction:

> Generate candidates that test this frame's assumption through distinct mechanisms. Exclude mechanisms banned by the brief. Do not evaluate, rank, hedge, or refer to other branches. Return only candidate names with compact rationales.

### Focus once

1. Cluster candidates by mechanism and remove semantic duplicates.
2. Mark attractive traps with a concrete reason.
3. Compare fit, viability, cost, reversibility, and material risk.
4. Select finalists only when they remain decision-relevant, then recommend one.
5. Deepen the recommendation enough to expose its first implementation step and load-bearing risk.

Carry forward only a compact decision record: fixed constraints, selected mechanism and rationale, acceptance criteria, load-bearing risk, evidence pointers, and invalidation triggers. Do not propagate branch transcripts after selection; preserve durable evidence separately when auditability requires it.

## VERIFY

### Build an evidence ledger

Record the artifact version or scope and, for each observable acceptance criterion, its check, result, material limitation, evidence pointer, and invalidation trigger.

Classify the surface:

- **Routine:** use the narrowest primary check that proves the criterion.
- **Elevated:** add one independent verifier only when it covers a materially different failure mode; give it only the artifact, criteria, and relevant evidence.
- **High assurance:** follow the applicable specialist skill, repository policy, regulation, or safety procedure. Pithy records closure but never limits required checks.

Reuse a recorded result when the artifact and its invalidation triggers are unchanged. After a change, rerun only invalidated criteria and materially coupled surfaces.

### Classify failure by meaning

- **Local defect:** the repair stays within fixed constraints and authority, preserves public and data contracts, and has a known affected surface. Repair once for that failure signature, then check the invalidated and coupled surfaces.
- **Evidence gap:** the environment or evidence source cannot currently establish the result. Gather a specific new evidence source when available; otherwise report `insufficient evidence` without pretending the artifact failed.
- **Structural blocker:** a load-bearing assumption or acceptance criterion is invalid, the repair requires boundary expansion, or the same failure signature survives an actual repair. Enter `REPLAN_REQUIRED`.

Do not classify failure from an error code, regex, or retry count alone. Treat static analysis as static evidence; never claim it proves unavailable runtime behavior.

## REPLAN_REQUIRED

Stop mutation and create a compact failure digest containing:

- the failed mechanism and criteria;
- the established cause, or the exact unknown when evidence is insufficient;
- the new exclusion or changed constraint;
- pointers to preserved raw evidence; and
- the requested scope or authority delta, if any.

Keep raw evidence in its durable source. Use the digest to avoid rehydrating logs or failed reasoning into active context; never delete evidence merely to shorten the prompt.

Then route once:

- If the digest creates a credible new in-scope decision delta, return to `OPEN` with the digest and route again.
- If the next action expands permissions, material spend, production impact, destructive effect, external communication, or another governing boundary, enter `WAITING_APPROVAL` and present the blocker, exact expansion, impact, and safe alternatives.
- If no materially different route or evidence source exists, stop `INCOMPLETE`.

Never revisit an equivalent failed mechanism without changed evidence or constraints. Approval creates a versioned scope delta; denial ends `INCOMPLETE` without mutation.

## Concise presentation

- Lead with the current fact or outcome and include only context that changes understanding, authority, or next action.
- Prefer one conclusion and a small decision-relevant set of bullets when sufficient; expand when safety, evidence, complexity, or an explicit request requires it.
- Report material state or plan changes instead of silently replanning while the user waits.
- Separate observed evidence, supported inference, and hypothetical risk.
- Hide neither blast radius nor residual uncertainty; summarize or point to evidence instead of dumping transcripts and logs.
- For closure, report status, criterion-to-result evidence, material limits, and reopen conditions without optional busywork.

## Repeated checking

When asked to check unchanged evidence again:

1. Do not rerun the same check or manufacture stronger reassurance.
2. Restate the recorded evidence and material limit once.
3. Ask what artifact, criterion, symptom, authority, or risk changed only when genuinely unclear.
4. If nothing changed, remain `CLOSED` or `INCOMPLETE` as recorded.

Treat a genuinely different acceptance criterion as new scope, not proof that the earlier check was invalid.

## Guardrails

- Apply safety, authority, and domain requirements before workflow defaults.
- Never use concision or efficiency to skip required security, legal, financial, production, migration, or data-integrity evidence.
- Do not broaden permissions, spend, external effects, or destructive impact without the authority governing the task.
- Do not claim token savings from shorter visible output. Evaluate savings, when needed, using total end-to-end usage for successfully closed tasks.

The DIVERGE architecture is adapted from [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) (MIT): isolated parallel generation followed by a separate focus pass.
