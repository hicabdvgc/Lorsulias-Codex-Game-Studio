# Assessment and authorized advancement

Produce requirement/source, evidence/revision, observed result, limitation and next activity for each
applicable check. Give PASS when all required outcomes pass, CONCERNS for advisory issues only, FAIL
for demonstrated required failure, or NOT ASSESSED for unavailable required evidence. Retain both
known failures and gaps. Missing vertical-slice human/framework evidence cannot become CONCERNS.
Review recommendations are not developer decisions, accepted ADRs or automatic milestone attainment.

Default output is conversational and read-only. An explicitly requested bounded report save is
permitted and must be verified, but is not a receipt for future automatic skipping. Identify the
actual reviewers, required independence and remaining human work. A failed/unassessed gate lists
concrete resolution and reassessment work. Never offer a required-evidence override.

Only an explicit request to advance the identified section authorizes production/stage.txt changes.
Existing authorization carries through; do not repeat a permission prompt. Re-read its current first
nonempty value and the evidence immediately before writing. Require the declared source to match the
assessed canonical phase and its next_phase from the catalog; resolve concurrent changes or legacy
values first. Change only that phase value and preserve other content. An absent marker requires an
explicitly settled current phase before authorized creation. Checkpoints inside implementation and a
null next_phase do not advance the marker. Read back the actual save.

A separately authorized worktree promotion must verify the combined revision; source gate evidence
cannot automatically advance the target. A passing final-acceptance assessment never ships a build.
