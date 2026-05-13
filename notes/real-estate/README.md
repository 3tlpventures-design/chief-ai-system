# Real Estate

Records for TLP Ventures' real-estate activity.

## Layout

| Folder | Contents | Filename |
|---|---|---|
| `properties/` | One file per property — owned, under consideration, or historical | `<address-slug>.md` (e.g. `123-main-street.md`) |
| `deals/` | One file per transaction in progress or closed | `YYYY-MM-DD-<short-slug>.md` |

## How to add an entry

1. Copy the relevant `_template.md` (don't edit it in place).
2. Rename per the filename convention in the table above.
3. Fill in the front matter — `status` must use a value from [INDEX.md](../INDEX.md#status-values).
4. Cross-link: deals should link to the property note; properties should list related deals.

## Status flow

```
prospect → loi → under-contract → closed
                              ↘ dead
```

A `dead` deal stays in `deals/` (don't delete) so we have a record of why it didn't happen.
