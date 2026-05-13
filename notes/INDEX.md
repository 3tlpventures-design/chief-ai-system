# TLP Ventures — Notes

Master index for TLP Ventures internal documentation. This is a working knowledge base; entries are markdown files with YAML front matter so they're greppable, diff-friendly, and easy for the `chief-ai-system` agent to read.

## Sections

| Section | What lives here |
|---|---|
| [Real Estate](real-estate/README.md) | Property records, deals in progress, transaction history |
| [TLP Ventures Projects](tlp-ventures-projects/README.md) | Active workstreams, completed projects, idea backlog |
| [Team Meetings](team-meetings/README.md) | Meeting notes by year, 1:1 logs |

## Conventions

- **One file per entity** — one property, one deal, one project, one meeting.
- **Filenames**
  - Dated entries: `YYYY-MM-DD-short-slug.md` (e.g. `2026-05-13-quarterly-review.md`)
  - Entity entries: descriptive kebab-case (e.g. `123-main-street.md`)
- **Templates** — every section has a `_template.md`. Copy it and rename; don't edit the template in place.
- **Front matter** — every note opens with a YAML block. Minimum: `title`, `date`, `status`, `tags`. Section-specific fields are in each template.
- **Status values** (use these, not free text):
  - Real estate deals: `prospect` · `loi` · `under-contract` · `closed` · `dead`
  - Properties: `owned` · `considering` · `sold` · `archived`
  - Projects: `active` · `blocked` · `paused` · `done`
- **Linking** — link liberally between notes with relative paths. E.g. a deal note can link to the property: `See [123 Main St](../properties/123-main-street.md).`

## Quick links

_Add direct links to high-traffic notes as the knowledge base grows. Examples:_

- _`[Q2 2026 priorities](tlp-ventures-projects/active/2026-q2-priorities.md)`_
- _`[Weekly standup template](team-meetings/_template.md)`_

## Working with `chief-ai`

This tree is designed to be navigated by the `chief-ai` agent. Try:

```powershell
chief-ai "What's the status of every active real-estate deal?"
chief-ai "Summarize the last three weekly standups."
```

The agent uses `list_dir` and `read_file` against this directory — keep notes plain markdown and the agent stays useful.
