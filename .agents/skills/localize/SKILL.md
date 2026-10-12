---
name: localize
description: "Full localization pipeline: scan for hardcoded strings, extract and manage string tables, validate translations, generate translator briefings, run cultural/sensitivity review, manage VO localization, test RTL/platform requirements, enforce string freeze, and report coverage."
---

Read `.codex/docs/resource-preparation.md` for resource locations, shared write,
review/evidence and recovery requirements. Its shared handoff rules apply here;
initial design can record future resource needs before type contracts exist.

## Invocation and execution

Invoke this workflow as `$localize`.

Use existing authorization for the bounded task. Describe the intended outputs and preserve unrelated work. Ask only about unresolved consequential choices or material scope expansion; do not repeat file- or section-level approval prompts.

Arguments: `scan | extract | validate | status | brief <locale> | cultural-review <locale...> | vo-pipeline <scan|script|validate|integrate> [locale] | rtl-check <locale...> | freeze [call|lift] | qa <locale...>`. Exactly one mode is required. Reject missing required locale/subcommand, unknown values, and repeated/conflicting arguments with **FAIL** and no writes.

Choose at most one localization-lead delegation path for the run. When delegation is authorized and available `localization-lead` expertise is useful, delegate the mode's substantive read-only analysis once; do not spawn it again inside a later phase. If unavailable, the current agent performs the same analysis and reports the fallback. Any conclusion requiring real human linguistic/playthrough QA remains unresolved; never fabricate a reviewer or sign-off.


# Localization Pipeline

Localization is not just translation — it is the full process of making a game
feel native in every language and region. Poor localization breaks immersion,
confuses players, and can affect selected release requirements. This skill covers the
complete pipeline from string extraction through cultural review, VO recording,
RTL layout testing, and localization QA sign-off.

**Modes:**
- `scan` — Find hardcoded strings and localization anti-patterns (read-only)
- `extract` — Extract strings and generate translation-ready tables
- `validate` — Check translations for completeness, placeholders, and length
- `status` — Coverage matrix across all locales
- `brief` — Generate translator context briefing document for an external team
- `cultural-review` — Flag culturally sensitive content, symbols, colours, idioms
- `vo-pipeline` — Manage voice-over localization: scripts, recording specs, integration
- `rtl-check` — Validate RTL language layout, mirroring, and font support
- `freeze` — Record an agreed source baseline and post-freeze change policy
- `qa` — Run the full localization QA cycle before release

If no subcommand is provided, output usage and stop. Verdict: **FAIL** — missing required subcommand.

Resolve only the prerequisites needed by the selected mode. Read live technical
preferences, applicable TYPE_TEMP and supplied localization decisions to identify
source locale, target locales, string identity/placeholder rules, formats, source
roots, table paths and VO mappings. Preserve the selected authoritative table(s)
and their partitioning; do not create a parallel source of truth. If a required
choice is unset, ask before dependent writes or conclusions. `scan` can inspect
supplied source roots without an existing table. `extract` can create a table only
after its source locale, path and format are selected. Do not default to English,
JSON, a library, or an engine API.

Before diffing or writing in any mode, parse every required source/locale/manifest file. On any parse error, report the exact file and best available line/location, stop that mode's diff/write, and leave the original untouched.

For any write-capable mode, compute every affected file before writing, including the primary table/output and any active-freeze update. Present all paths and exact modifications in one complete changeset. A freeze checklist/content decision does not authorize writes. If another affected file is discovered after preview, stop and re-preview the expanded set.

---

## Phase 2A: Scan Mode

Search the selected project/code roots for hardcoded user-facing strings:

- String literals in UI code not wrapped in a localization function (resolve the actual project localization API from its selected engine/package documentation)
- Concatenated strings that should be parameterized
- Placeholder inconsistencies or assembly that violates the selected formatting contract
- Format strings that mix locale-sensitive data (numbers, dates, currencies) without locale-aware formatting

Search for localization anti-patterns:

- Date/time formatting not using locale-aware functions
- Number formatting without locale awareness (`1,000` vs `1.000`)
- Text embedded in images or textures within declared resource/source/import mappings
- Strings that assume left-to-right text direction (positional layout, string assembly order)
- Gender/plurality assumptions baked into string logic (must use plural forms or gender tokens)
- Punctuation assembled outside the localizable message where it prevents locale-appropriate formatting

Report all findings with file paths and line numbers. This mode is read-only — no files are written.

---

## Phase 2B: Extract Mode

- Reuse Scan Mode's player-visible source scope to find both hardcoded source text and localized string references. Exclude logs, test code/fixtures, and editor-only copy.
- Compare the discovered text/references against the uniquely resolved source table
- Generate new entries for strings not yet keyed
- Preserve existing keys and the selected identity convention; illustrative new-key shape: `[category].[subcategory].[description]`
  - Example: `ui.hud.health_label`, `dialogue.npc.merchant.greeting`, `menu.main.play_button`
- Each new entry must have associated translator context in the selected table or companion format — a translator comment explaining only facts verified from the UI/call site:
  - Where it appears (which screen, which scene)
  - Maximum character length
  - Any placeholder meaning (`{playerName}` = the player's chosen display name)
  - Gender/plurality context if applicable

For any context property that cannot be confirmed (such as maximum length or gender), write an explicit `TODO/unknown` note. Do not guess, and do not claim COMPLETE while required context remains unknown.

Output a diff of new strings to add to the source table. If string freeze is ACTIVE, compute the corresponding `production/localization/freeze-status.md` Post-Freeze Changes edit now and include both files in the same preview.

Present the complete diff to the user. Do not write until the entire changeset is authorized.

Once the complete changeset is authorized, write only the diff (new entries), not a full replacement. Verdict: **COMPLETE** — strings extracted and written.

---

## Phase 2C: Validate Mode

Read the uniquely resolved source and locale tables. For each locale, check:

- **Completeness** — key exists in the selected source locale but no translation for this locale
- **Placeholder mismatches** — source has `{name}` but translation omits it or adds extras
- **String length violations** — translation exceeds the character limit recorded in the source `context` field
- **Plural form count** — locale requires N plural forms; translation provides fewer
- **Orphaned keys** — translation exists but nothing in the declared source scope references the key
- **Stale translations** — only when an existing recorded prior source value proves that the source changed; otherwise report `unknown — no stale baseline`
- **Encoding/font coverage** — validate syntax and encoding directly; without an explicit atlas/font coverage artifact report `manual verification required`

For orphan candidates, state the searched paths and the limits of detecting dynamic references. Never auto-delete an orphan from this result. Only key presence, placeholders, empty values, recorded limits, and parseable format receive definite conclusions without further evidence.

Report validation results grouped by locale and severity. This mode is read-only — no files are written.

---

## Phase 2D: Status Mode

- Count total localizable strings in the source table
- Per locale: count translated, untranslated, stale (source changed since translation)
- Generate a coverage matrix:

```markdown
## Localization Status
Generated: [Date]
String freeze: [Active / Not yet called / Lifted]

| Locale | Total | Translated | Missing | Stale | Coverage |
|--------|-------|-----------|---------|-------|----------|
| [source locale] | [N] | [N] | 0 | 0 | 100% |
| [locale] | [N] | [N] | [N] | [N] | [X]% |

### Issues
- [N] hardcoded strings found in source code (run $localize scan)
- [N] strings exceeding character limits
- [N] placeholder mismatches
- [N] orphaned keys
- [N or unknown] strings added after freeze was called (freeze violations; count only parseable entries in the existing `production/localization/freeze-status.md` Post-Freeze Changes section, otherwise `unknown`)
```

This mode is read-only — no files are written.

---

## Phase 2E: Brief Mode

Generate a translator context briefing document. It can accompany the selected string export. Creating the briefing does not authorize sending it to an external recipient.

Read:
- `design/gdd/` — extract game genre, tone, setting, character names
- The uniquely resolved source string table (selected path and format)
- Any existing lore or narrative documents in `design/narrative/`

Generate `production/localization/translator-brief-[locale]-[date].md`:

```markdown
# Translator Brief — [Game Name] — [Locale]

## Game Overview
[2-3 paragraph summary of the game, genre, tone, and audience]

## Tone and Voice
- **Overall tone**: [e.g., "Darkly comic, not slapstick — think Terry Pratchett, not Looney Tunes"]
- **Player address**: [e.g., "Second person, informal. Never formal 'vous' — always 'tu' for French"]
- **Profanity policy**: [e.g., "Mild — PG-13 equivalent. Match intensity to source, do not soften or escalate"]
- **Humour**: [e.g., "Wordplay exists — if a pun cannot translate, invent an equivalent local joke; do not translate literally"]

## Character Glossary
| Name | Role | Personality | Notes |
|------|------|-------------|-------|
| [Name] | [Role] | [Personality] | [Do not translate / transliterate as X] |

## World Glossary
| Term | Meaning | Notes |
|------|---------|-------|
| [Term] | [What it means] | [Keep in English / translate as X] |

## Do Not Translate List
The following must appear verbatim in all locales:
- [Game name]
- [UI terms that match in-engine labels]
- [Brand or trademark names]

## Placeholder Reference
| Placeholder | What it represents | Example |
|-------------|-------------------|---------|
| `{playerName}` | Player's chosen display name | "Shadowblade" |
| `{count}` | Integer quantity | "3" |

## Character Limits
Tight UI fields with hard limits are marked in the string table `context` field.
Where no limit is stated, record that layout evaluation is needed; do not invent a character budget.

## Contact
Direct questions to: [placeholder for user/team contact]
Delivery format: [selected source/locale contract]
```

For an authoring output, use existing bounded authorization and verify the save. For review/QA findings, return them in conversation; save only to an explicitly requested bounded report path.

---

## Phase 2F: Cultural Review Mode

Require at least one explicit target locale; missing locales stop for user input. Use the run's single localization-lead delegation path described above rather than spawning a second reviewer. Ask them to audit the following for cultural sensitivity across the target locales (read the declared string and resource scopes):

### Content areas to review

Inspect relevant symbols, gestures, colors, names, humor, representations and selected
market requirements in the actual content. Cite contextual evidence for locale-specific
claims; uncertain interpretations are questions for qualified local reviewers. Do not
infer offense, legal requirements or ratings from a country stereotype. Verify current
primary requirements if a legal/platform claim is necessary. Proposals do not establish
human cultural approval or certification.

Present findings as a table:

| Finding | Locale(s) Affected | Severity | Recommended Action |
|---------|--------------------|----------|--------------------|
| [Description] | [Locale] | [BLOCKING / ADVISORY / NOTE] | [Change / Flag for review / Accept] |

BLOCKING = must fix before shipping that locale. ADVISORY = recommend change. NOTE = informational only.

Keep findings conversational by default. If the user chooses to save them, use exactly `production/localization/cultural-review-[locale-set]-[date].md` and include that path in the run's complete changeset preview; do not write it until authorized.

---

## Phase 2G: VO Pipeline Mode

Manage the voice-over localization process. Determine the sub-task from the argument. Saved manifests and recording scripts use `production/localization/vo-manifest-[locale-or-source]-[date].md` and `production/localization/vo-script-[locale-or-source]-[date].md` respectively, and join the same complete changeset. For validate/integrate, if the required locale, VO directory, or manifest does not exist, report the missing input and stop that sub-task:

- `vo-pipeline scan` — identify all dialogue lines that require VO recording
- `vo-pipeline script` — generate recording scripts with director notes
- `vo-pipeline validate` — check that all recorded VO files are present and correctly named
- `vo-pipeline integrate` — verify VO files are correctly referenced in code/assets

### VO Pipeline: Scan

Read the uniquely resolved string tables and `design/narrative/`. Identify:
- All dialogue lines (identities mapped to dialogue by the selected contract) with source text
- Lines with a readable, non-empty audio file whose path/name matches the expected key and locale under the selected VO mapping. File existence alone does not prove recorded status or quality
- Lines not yet recorded

Output a recording manifest:

```
## VO Recording Manifest — [Date]

| Key | Character | Source Line | Status |
|-----|-----------|-------------|--------|
| [stable line ID] | [character] | [source text] | [file present; recording quality unassessed] |
| dialogue.npc.merchant.haggle | Merchant | "That's my final offer." | Needs recording |
```

### VO Pipeline: Script

Generate a recording script document for each character, grouped by scene. Include:

- Character name and brief personality note
- Full dialogue line with pronunciation guide for unusual proper nouns
- Emotion/direction note for each line (`[Warm, welcoming]`, `[Annoyed, clipped]`)
- Any lines that are responses in a conversation (provide context: "Player just said X")

For an authoring output, use existing bounded authorization and verify the save. For review/QA findings, return them in conversation; save only to an explicitly requested bounded report path.

### VO Pipeline: Validate

Require the explicit locale, recording manifest, and selected locale VO directory before validation. Inspect the selected media formats there using available methods. Cross-reference against the VO manifest. Report:
- Missing files (line in script, no audio file)
- Extra files (audio file exists, no matching string key)
- Naming convention violations

### VO Pipeline: Integrate

Require the explicit locale and existing selected locale VO directory before integration. Search the selected project/code roots for VO audio references. Verify each referenced path exists in the selected locale VO mapping. Report broken references.

---

## Phase 2H: RTL Check Mode

Right-to-left languages (Arabic, Hebrew, Persian, Urdu) require layout mirroring beyond
just translating text. This mode validates the implementation.

Require explicit target locales and run this mode only for those that are RTL. Read `docs/technical-preferences.md` to determine one configured engine. If no engine is configured, report that engine-specific checks cannot run and limit the result to engine-independent findings; never guess or combine all three engines. Then check:

**Layout mirroring**
- Check the selected engine/UI package and version using official documentation and actual project settings; no package is presumed installed.
- Does each relevant layout implement its selected RTL behavior?
- Do directional controls, numerals and icons follow their documented locale-specific behavior, including intentional non-mirroring?

**Text rendering**
- Are fonts loaded that support Arabic/Hebrew character sets?
- Is Arabic text rendered with correct ligatures (connected script)?
- Are numbers displayed as Eastern Arabic numerals where required?

**String assembly**
- Are there any string concatenations that assume left-to-right reading order?
- Do `{placeholder}` positions in sentences work correctly when sentence structure is reversed?

**Asset review**
- Are there UI icons with directional arrows or asymmetric designs that need mirrored variants?
- Do any text-in-image assets exist that require RTL versions?

Content search patterns to check:
- Engine-specific RTL flags in scene/prefab files
- Actual layout containers in the selected engine/UI framework and their verified direction settings
- String concatenation with `+` near dialogue or UI code

Report findings. Flag BLOCKING issues (content unreadable without fix) vs ADVISORY (cosmetic improvements).

For an authoring output, use existing bounded authorization and verify the save. For review/QA findings, return them in conversation; save only to an explicitly requested bounded report path.

---

## Phase 2I: Freeze Mode

String freeze records an agreed baseline and change policy for the selected source locale and scope. This document does not enforce a filesystem lock or stop external edits.

### freeze call

Check current freeze status in `production/localization/freeze-status.md` (if it exists).

If already frozen:
> "String freeze is currently ACTIVE (called [date]). [N] strings have been added or modified since freeze. These are freeze violations — they require re-translation or an approved freeze lift."

If not frozen, present the pre-freeze checklist:

```
Pre-Freeze Checklist
[ ] The selected freeze scope and its current source baseline are identified
[ ] The relevant dialogue/source content is settled for this freeze scope
[ ] All system strings (error messages, tutorial text) are complete
[ ] $localize scan shows zero hardcoded strings
[ ] $localize validate shows no placeholder mismatches in the selected source locale
[ ] Any marketing strings included in this scope are settled
```

Ask the user directly:
- Prompt, only when the decision is unresolved: "Are the applicable freeze conditions confirmed for this source baseline? Calling freeze records the agreed change policy."
- Options: `[A] Yes — call string freeze now` / `[B] No — I still have strings to add`

When the applicable conditions and freeze decision are supplied, write `production/localization/freeze-status.md` within existing authorization, without repeating the decision prompt:

```markdown
# String Freeze Status

**Status**: ACTIVE
**Called**: [date]
**Called by**: [user]
**Total strings at freeze**: [N]

## Post-Freeze Changes
[Any strings added or modified after freeze are listed here automatically by $localize extract]
```

### freeze lift

For `freeze lift`, draft the `freeze-status.md` Status change to `LIFTED` with reason and date, include it in the complete changeset preview, and write only after authorization. Warn: "Lifting the freeze requires re-translation of all modified strings. Notify the translation team."

### freeze check (auto-integrated into extract)

When `extract` mode finds new or modified strings and `freeze-status.md` shows Status: ACTIVE, the source diff and Post-Freeze Changes edit are one changeset; after that combined preview is authorized, apply both and warn:
> "⚠️ String freeze is active. [N] new/modified strings have been added. These are freeze violations. Notify your localization vendor before proceeding."

---

## Phase 2J: QA Mode

Localization QA is a dedicated pass that runs after translations are delivered but
before any locale ships. This extends `$localize validate` (which checks structural completeness)
— this is a structured playthrough-based quality check.

Use the run's single localization-lead delegation path described above with:
- The target locale(s) to QA
- The list of all screens/flows in the game (from `design/gdd/` or `$content-audit` output)
- The current `$localize validate` report
- The cultural review report (if it exists)

Ask the localization-lead to produce a QA plan, and separately collect any existing executed results, covering:

1. **Functional string check** — every string displays in-game without truncation, placeholder errors, or encoding corruption
2. **UI overflow check** — translated strings that exceed UI bounds (even if within character limits, some languages expand)
3. **Contextual accuracy** — a justified sample or complete selected scope reviewed by qualified humans in-game for translation accuracy and natural phrasing
4. **Cultural review items** — verify all BLOCKING items from the cultural review are resolved
5. **VO sync check** — if VO exists, verify lip sync or subtitle timing is acceptable after translation
6. **Platform cert requirements** — check platform-specific localization requirements (age ratings text, legal notices, ESRB/PEGI/CERO text)

Output the template below as a **QA plan** when executed evidence is missing; in that case state `verdict unavailable — QA has not been executed` and do not mark producer sign-off. Only output a QA verdict per locale when every applicable required check has actual results; explain inapplicable checks:

```
## Localization QA Verdict — [Locale]

**Status**: PASS / PASS WITH CONDITIONS / FAIL
**Reviewed by**: [actual evaluator and method]
**Date**: [date]

### Findings
| ID | Area | Description | Severity | Status |
|----|------|-------------|----------|--------|
| LOC-001 | UI Overflow | "Settings" button text overflows on [Screen] | BLOCKING | Open |
| LOC-002 | Translation | [Key] translation is literal — sounds unnatural | ADVISORY | Open |

### Conditions (if PASS WITH CONDITIONS)
- [Advisory condition; required shipping gaps prevent PASS WITH CONDITIONS]

### Sign-Off
[ ] All BLOCKING findings resolved
[ ] The authorized release decision-maker has supplied any required acceptance
```

For an authoring output, use existing bounded authorization and verify the save. For review/QA findings, return them in conversation; save only to an explicitly requested bounded report path.

**Gate integration**: PASS requires executed evidence for every applicable check and no open BLOCKING finding. PASS WITH CONDITIONS requires executed evidence plus only explicitly listed non-blocking conditions. Missing execution evidence has no release verdict and no sign-off. FAIL blocks release for that locale only; other locales may proceed only from their own evidence-backed verdicts.

---

## Phase 3: Rules and Next Steps

### Rules
- Use selected source/target locales and formats. Preserve IDs, placeholders, plural
  conventions and existing translations unless the bounded task explicitly changes them.
- Record translator context in the selected representation; missing layout/linguistic
  information remains explicit. Character limits apply only when declared.
- Freeze, voice-over and RTL activities apply when selected project needs require them.
  Record source baseline/revisions so stale translations can be established from evidence.
- Re-read tables and freeze state immediately before writes. Preserve concurrent
  additions and re-evaluate a changed baseline before applying the authorized diff.
- QA separates structural analysis, human linguistic assessment and actual playthrough.
  Missing required evidence prevents locale completion and release sign-off.

### Recommended Workflow

```
$localize scan            → find hardcoded strings
$localize extract         → build string table
$localize freeze call     → record the selected source baseline/change policy
$localize brief <locale>  → generate translator briefing document
[Authorized human handoff to translators]
$localize validate        → check returned translations
$localize cultural-review → flag culturally sensitive content
$localize rtl-check       → if shipping Arabic / Hebrew / Persian
$localize vo-pipeline     → if shipping dubbed VO
$localize qa              → full localization QA pass
```

Report actual QA evidence and its scope to the project release process. `$gate-check` is installed; report paths only after an authorized save has succeeded.
