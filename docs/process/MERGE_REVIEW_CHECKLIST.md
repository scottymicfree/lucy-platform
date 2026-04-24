# Lucy Standalone — Merge Review Checklist

Use this checklist before merging any donor build, ZIP, AI output, code block, or architecture proposal into Lucy.

This document exists to stop fragmentation, fake progress, architectural drift, and unsafe capability jumps.

If a donor build fails this checklist, do **not** merge it into Lucy as-is.
Use it only as a donor/reference and extract the good parts carefully.

---

## 1. First Question — What is this actually for?

Classify the material:

- UI donor — layout, panels, styling, shell feel
- logic donor — internal behavior or module structure
- data donor — sample payloads, schema, API mapping
- execution donor — future controlled execution lane
- theory/spec donor — planning/spec reference only

If it is not clear which one it is, do not merge it.

---

## 2. Source Classification

Mark the donor with one of these:

- KEEP_AS_DONOR_ONLY
- EXTRACT_PARTS_ONLY
- SAFE_TO_MERGE_NOW
- ARCHIVE_FOR_LATER
- DO_NOT_USE

Never skip this classification.

---

## 3. Architecture Fit Check

### 3.1 Does it fit Lucy’s core rule?

Lucy must remain:

- local-first
- proposal-first
- auditable
- human-boundary-safe
- modular

If the donor assumes cloud-first control, direct execution without proposals, hidden actions, or no audit trail, it fails.

### 3.2 Does it preserve the power structure?

Correct power structure:

- Human owns intent and final authority
- Lucy plans/proposes/explains/builds in approved lanes
- Emma governs Lucy outputs, not the human’s mind

If a donor confuses this, reject or rewrite.

### 3.3 Does it preserve the human boundary?

Human lane must remain:

- observation-only
- auditable
- non-routable into Lucy reasoning

If a donor lets Lucy treat human events as Lucy/system reasoning input, do not merge as-is.

---

## 4. Reality Check — Is it real or fake progress?

### 4.1 Does it imply capability without real internals?

Look for:

- empty routes with impressive names
- mocked telemetry displayed as real intelligence
- placeholder state pretending to be live
- demo language that sounds more complete than the code

If yes, label it MOCKED and EXTRACT_PARTS_ONLY.

### 4.2 Does it claim live data without real ingestion?

If features are described as live but are hardcoded/mocked, they are not real capabilities.

### 4.3 Does it claim execution but only simulate output?

Verify whether it really:

- writes files
- validates paths
- stays inside sandbox
- audits actions

If not, it is a demo.

---

## 5. Shell vs Spine Check

### 5.1 Shell good, internals weak?

Keep the shell; replace the spine. Do not let UI redefine architecture.

### 5.2 Spine good, UI weak?

Extract internal logic; fit it under Lucy shell.

---

## 6. Startup / Runtime Check

### 6.1 What actually launches?

Verify whether the donor runs as Vite-only, Electron, backend+UI, or full local stack.

### 6.2 Is runtime using mocks?

Check for mock bridges or fake backend data. Acceptable in prototypes, but flag honestly.

---

## 7. Proposal-First Compliance Check

All meaningful action should follow:

Intent → Plan → Proposal → Approval → Controlled Action → Audit

If the donor jumps directly to action, reject or rewrite.

Proposals should include:

- id, type, mode, status, confidence, request, payload/steps, timestamp

---

## 8. Controlled Execution Check

Reject uncontrolled execution:

- raw exec
- arbitrary shell execution
- raw filesystem mutation from UI

To be mergeable, execution must be bounded with:

- allowed root path
- bounded command list / templates
- human approval gate
- audit logging
- no path escape

---

## 9. Toolbelt Check

Docs/handbooks should be structured and planning-only by default. Docs do not automatically grant execution rights.

---

## 10. Earth / Live Data Check

Live data donors should clearly use real sources (NOAA/USGS/etc.) and avoid full hard-refresh UI freezes.

---

## 11. Quantum Music Check

Must be local and optional. Reject surveillance patterns.

---

## 12. File-Level Review Checklist

For every file:

1. Which Lucy layer does it belong to?
2. Does it duplicate Lucy already?
3. Is it better than current?
4. Donor-only or production?
5. Break human boundary?
6. Skip proposals?
7. Skip audit?
8. Fake progress?
9. Assume cloud dependency?
10. Fit build order?

If more than 2 answers are bad, do not merge directly.

---

## 13. Merge Strategy Decision Tree

- UI good, logic bad → keep UI only
- logic good, UI bad → extract logic only
- both partial → donor only
- opens execution too early → archive for later
- breaks human boundary → reject/redesign

---

## 14. Required Labels After Review

### 14.1 Merge label
- SAFE_TO_MERGE_NOW
- EXTRACT_PARTS_ONLY
- KEEP_AS_DONOR_ONLY
- ARCHIVE_FOR_LATER
- DO_NOT_USE

### 14.2 Reality label
- REAL
- PARTIAL
- MOCKED
- INFLATED

### 14.3 Layer label
- SHELL
- CONTROL_SPINE
- HUMAN_BOUNDARY
- TOOLBELT
- EARTH
- MUSIC
- BUILD_LANE
- BRIDGE
- STARTUP
- PACKAGING

---

## 15. Safe Merge Rules

- merge one subsystem at a time
- never merge two competing shells at once
- never merge uncontrolled execution blindly
- keep checkpoint zips before big merges

---

## 16. Hard Stop Conditions

Do not merge if it:

- treats human actions as governed by Emma
- uses raw shell execution without boundaries
- presents mocked data as real
- rewrites architecture without reason
- depends on cloud-only services for core identity
- destroys the stable shell

---

## 17. What “Good Donor” Usually Means

Usually one useful piece:

- stable shell/UI feel
- strong panel design
- Earth widget rendering idea
- safe local sandbox UX
- proposal-card presentation
- folder/template structure
- API normalization pattern

---

## 18. Final Merge Question

**Does this make Lucy more real, or just look more complete?**

Only merge what increases:

- truth
- stability
- control
- auditability
- bounded capability

---

## 19. Recommended Review Workflow

For each donor:

1. classify
2. identify shell/spine value
3. mark real vs mocked
4. mark merge label
5. decide extract vs merge
6. checkpoint
7. patch Lucy
