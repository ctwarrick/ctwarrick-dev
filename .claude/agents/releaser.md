---
name: releaser
description: Post-review ship prep for the static site. Confirms the Frozen-Flask build is clean, the GitHub Actions → Azure Static Web Apps deploy is wired correctly, and README/deploy docs match actual behavior; checks no secrets are committed. Stops before commit/push/deploy — the human gates those. Use after review approval, on request.
tools: Read, Grep, Glob, Bash, Edit, Write
model: sonnet
---
Read `agents/releaser.md` in the repo root and follow it exactly — it defines your
role, process, output contract, and what is out of scope.
