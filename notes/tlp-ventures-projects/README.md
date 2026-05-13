# TLP Ventures Projects

Internal workstreams — anything TLP Ventures is building, running, or considering that isn't a real-estate transaction.

## Layout

| Folder | Contents |
|---|---|
| `active/` | Projects currently underway |
| `completed/` | Projects shipped, paused indefinitely, or shut down |
| `ideas/` | Backlog — things worth considering but not started |

When a project transitions `active → done`, move the file from `active/` to `completed/` (a `git mv` preserves history).

## How to add a project

1. Copy `active/_template.md` or `ideas/_template.md`.
2. Name it descriptively, kebab-case: e.g. `chief-ai-rollout.md`, `tenant-portal-mvp.md`.
3. Date-prefix only if the project is inherently tied to a quarter or campaign (`2026-q2-priorities.md`).
4. Status field must come from [INDEX.md](../INDEX.md#status-values).

## Conventions

- **Owner** — one person on the hook for the project. Multiple contributors are fine; one owner.
- **Decisions** — log them inline with date and rationale. Don't rewrite history when a decision changes; add a new entry.
