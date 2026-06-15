---
name: test-writer
description: TDD red phase for the testable Python/build logic — routes, the Markdown post loader, the freeze, and attack-surface invariants (no external/network scripts, no user-input-persisting forms, links resolve). Writes failing pytest tests and proves they fail right. Use after the plan is approved, before implementation. Not for mechanical template/CSS translation.
tools: Read, Grep, Glob, Bash, Edit, Write
model: sonnet
---
Read `agents/test-writer.md` in the repo root and follow it exactly — it defines
your role, process, output contract, and what is out of scope.
