# Skill Test Spec: $integrate-worktrees

## Intended interface

Read the installed SKILL.md, its linked shared contracts and selected mode references. Preserve useful source modes while assessing the adapted outcomes.

## Case 1: Pinned combined delivery

**Request/inputs:** Two supplied related deliveries with original bases; authorize isolated integration; target initially idle.

**Expected useful outcome:** Pin SHAs, preserve journal, serial merges and exact combined verification before fast-forward promotion.

## Case 2: Failure and races

**Request/inputs:** Dirty target, unrelated source, branch moved after handoff, combined check fails, or target advances during validation.

**Expected useful outcome:** Preserve user work/delivery pins; no promotion on failure; refresh target and reverify candidate before promotion.

## Case 3: Draft and stage authority

**Request/inputs:** Draft design delivery plus source stage transition without combined gate authorization.

**Expected useful outcome:** Verify intended draft maturity while retaining gaps; preserve target phase under authorized correction or block. Check-only writes nothing.

## Executable mechanics
Run tests/test_worktree_preflight.py against the installed inspector in disposable repositories. Retain cases for pins after branch advancement/rebase, unrelated/missing refs, duplicate/ancestor sources, dirty/in-progress worktrees, detached candidate, combined-test failure and target drift. These are helper/Git mechanics, not live skill execution.

## Verification record requirements

Parse package/metadata and resolve retained references/catalog registration. Test representative success
and relevant failure inputs in isolation. Inspect actual responses and saved artifacts for scope,
authority, identity, status, criterion-level evidence and required review/human boundaries. Re-read shared
files before authorized writes and preserve concurrent edits. Distinguish static inspection, guided
current-agent exercise, helper execution and native dispatch/engine/CI/human evidence. Record observed
results and limitations; the assertions or fixture description alone are not execution evidence.
