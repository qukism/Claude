# Handoff — Allston living room project

Read this first when picking the project up in a new Claude session.
Everything below was worked out in a cloud session between 2026-09-28 and 2026-10-10.

## The person and the goal

Furnishing the living room of an Allston apartment (Unit 4, Boston, 02134) shared with roommates.
Main open decision: **which counter-height table to buy** (plus optionally a coffee table and a floor lamp).
They prefer short, direct answers, and want real product links with prices.

## Files in this folder

| File | What it is |
|---|---|
| `README.md` | Short index |
| `HANDOFF.md` | This file: full context and next steps |
| `CLAUDE.md` | Auto-loaded instructions for a Claude session opened in this folder |
| `room-notes.md` | Current state of the room, fixed features, spec corrections, walkway table |
| `shopping-lists.md` | All product lists with sizes, prices seen and links |
| `furniture-spec-original.md` | The person's original tape-measured spec (2026-09-27), unchanged |
| `living-room-3d/index.html` | Interactive 3D model (three.js r128 from CDN). Published at https://claude.ai/artifact/T21HUxgBbjmDFC2KvSR73T |
| `tools/walkway_calc.py` | The geometry script behind the walkway numbers |
| `images/` | Product screenshots the person sent (3 tables, the rug); `images/session-screenshots/` has two app screenshots |

## Decisions made (don't re-ask)

- Couch placement is fixed (left wall, x 0–45, y 35.5–148.5).
- Ottoman goes against the couch front as a chaise (x 45–73, y 92.5–148.5), long side parallel to the couch. Same white/navy fabric as the couch.
- Rug **bought**: LUXE WEAVERS Daphnes 2735, Navy, 8×10, at x 26–122, y 32–152.
- 5 stools owned, all 24" seats: 2 black adjustable swivel with backs, 2 grey with backs, 1 grey backless.
- Router moved forward in the gap past the couch end; an arc floor lamp (base ≤ 6") is wanted in the back corner, arcing over the couch.
- Recessed cabinets on the TV wall: closed doors on the lower half, open shelves on the upper half.
- Porch doors stay closed.

## Key findings

- The **kitchen-door walkway** is the binding constraint: the path from the kitchen door runs between the couch's top arm (45, 35.5) and anything on the porch-door wall. 30" is comfortable, 24" a squeeze.
- Best layout: table **rotated 90°** (short end against the porch-door wall), long edges at about x 86–110, 2 stools per side.
- Ideal table: **~48 × 24 × 35–36"**. Top picks found: **Linon Claridge** (47.25 × 23.75 × 36, solid rubberwood, ~$170) and **Linon Concord black** ($149).
- Of the three tables the person originally sent: Bike (17 Stories, $77.99) > Rectangle (Ophelia & Co., $118.99) > Square (too big).
- Square tables only work at 28–31.5"; picks: August Grove 31.5" with storage ($161.99, Wayfair) or TRIBEWOOD 31.5" solid wood.
- Coffee table pick (if swapped for the ottoman): BH&G Greyson ($128, Walmart).

## Not verified yet

All prices came from web-search snippets. Stock, shipping to Boston (02134) and live prices were **not** checked,
because store sites (Wayfair, Amazon, Walmart, Target, Home Depot, IKEA, Facebook) were blocked in the cloud session.

## Next steps (why this moved to a local session)

1. **Look at the person's Wayfair saved items** (Account → Lists) using Claude in Chrome with their sign-in.
   Check each saved item against the room: fits? walkway left? height vs 24" stools? Add good ones to `shopping-lists.md`.
2. Re-verify prices, stock and shipping to 02134 for the top picks in `shopping-lists.md`.
3. Optionally browse Facebook Marketplace (Allston, ~10 mi) with the searches listed in `shopping-lists.md`.
4. If a table is chosen, add it to the 3D model (`living-room-3d/index.html` → `TABLES` object) and republish.

## Ground rules from the person

- **Don't search or read their email.** They stopped a Gmail search; ask before touching any account other than the one they point to.
- Keep files in this folder; they want everything accessible on their computer.
