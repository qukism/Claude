# Living Room — Furniture & Layout Spec

Allston apartment, Unit #4. All units in **inches**. Source: tape-measured
on site 2026-09-27.

Purpose: input for a 3D render / layout tool.

---

## 1. Coordinate System

```
        TOP WALL (kitchen + porch)
        y = 0
   x=0 ┌──────────────────────────┐ x=137
       │                          │
  LEFT │                          │ RIGHT
  WALL │                          │ WALL
       │                          │
       └──────────────────────────┘
        BOTTOM WALL (hallway)
        y = 155
```

- **Origin** `(0, 0, 0)` = top-left floor corner
- **+X** → right, 0 to 137 (room width)
- **+Y** → down/toward bottom wall, 0 to 155 (room length)
- **+Z** → up from floor
- All object positions below are given as `x_min–x_max`, `y_min–y_max`
- Ceiling height: **NOT MEASURED** — assume 96 unless supplied

---

## 2. Room Shell

| Dimension | Value |
|---|---|
| Width (left→right) | **137** |
| Length (top→bottom) | **155** |
| Floor area | 147 sq ft |
| Ceiling | unmeasured (assume 96) |
| Flooring | hardwood |

### 2.1 Measurement discrepancies

Raw segment sums don't perfectly match wall totals. Values below are
**normalized** to the wall totals. Flagged for the renderer:

- Top wall segments sum to 139.5 vs. 137 actual → **−2.5 absorbed**
- Bottom wall segments sum to 138 vs. 137 actual → **−1.0 absorbed**
- Right wall segments sum to 154.7 vs. 155 actual → **+0.3, within tolerance**

---

## 3. Wall Features

### 3.1 Top wall (y = 0) — measured right→left

| Feature | Raw | x-range (normalized) | Notes |
|---|---|---|---|
| Porch doors | 74 | 63.0 – 137.0 | Double doors that open. **Kept closed permanently.** Second porch access exists via kitchen. |
| Wall | 27.5 | 35.5 – 63.0 | |
| Kitchen door | 32.5 | 3.0 – 35.5 | Active traffic — keep clear |
| Wall | 5.5 | 0.0 – 3.0 | |

### 3.2 Bottom wall (y = 155) — measured right→left

| Feature | Raw | x-range (normalized) | Notes |
|---|---|---|---|
| Wall | 15 | 122.0 – 137.0 | |
| Hallway doorway | 66 | 56.0 – 122.0 | Only real exit. Ottoman partially blocks — accepted. |
| Wall | 57 | 0.0 – 56.0 | |

### 3.3 Right wall (x = 137) — measured top→bottom

| Feature | Size | y-range | Projection |
|---|---|---|---|
| Radiator | 41.5 | 0.0 – 41.5 | **9 deep** into room (occupies x 128–137) |
| Clear wall | 73.0 | 41.5 – 114.5 | TV zone |
| Trim | 4.2 | 114.5 – 118.7 | OK to cover |
| Recessed cabinets | 36.0 | 118.7 – 154.7 | Do NOT cover with TV. OK to cover with stand. |

### 3.4 Left wall (x = 0)

Unbroken, **155** long. Couch wall.

---

## 4. Owned Furniture

### 4.1 Couch — PLACED

Free Facebook Marketplace find. White/blue Sunbrella, two twin pull-out
beds, currently being cleaned.

| Property | Value |
|---|---|
| Length | 113 |
| Depth | 45 |
| Height | unmeasured — assume 36 |
| Position | `x: 0 – 45`, `y: 35.5 – 148.5` |
| Orientation | Flat against left wall, facing +X (toward TV) |
| Color | white body, navy piping/trim |

- **6.5 gap** at bottom end (y 148.5–155) reserved for wifi router, possibly a lamp
- Straight, **not** an L. Decision settled.
- Couch centerline: `y = 92`
- Face-to-TV-wall distance: **92**

### 4.2 Storage ottoman — PLACED (loosely)

| Property | Value |
|---|---|
| Footprint | 28 × 56 (approximate) |
| Height | same as couch seat |
| Position | near hallway doorway, partially blocking. Exact placement TBD. |

### 4.3 TV — PLACED

| Property | Value |
|---|---|
| Screen size | 65" diagonal |
| Panel width | ~57 |
| Panel height | ~33 |
| Screen center | `y = 90` (2 off couch centerline — acceptable) |
| Panel y-range | 61.5 – 118.5 |
| Mount | on stand, not wall-mounted |

Separate from the 55" TV in the bedroom.

---

## 5. Candidate Products (not yet purchased)

### 5.1 TV stand — LEADING CANDIDATE

| Property | Value |
|---|---|
| Width | 70 |
| Depth | 15 |
| Height | 15 |
| Position | `x: 122 – 137`, `y: 55 – 125` |

- Covers trim (OK) and ~13 of cabinets (OK)
- Clears radiator by 15
- Leaves 77 to couch face
- **Concern:** 15 H puts screen center at ~33, roughly 7–9 below seated
  eye level (~40–42). 20–24 H preferred if available.
- Verify weight rating ≥ 60 lb

### 5.2 Counter-height table — REJECTED CANDIDATE

Wayfair "63" Solid Wood Counter Height Dining Table" by Ophelia & Co.,
SKU W115125820, $118.99.

| Property | Value |
|---|---|
| Length | 62.99 |
| Depth | 19.69 |
| Height | 37.4 |
| Top thickness | 1.77 |
| Apron drop | 2.75 |
| Leg footprint | 17.52 deep, solid panel |

**Rejected.** Fits the space fine but depth of 19.69 makes it one-sided —
seats 3, not the 5–6 target. Solid panel legs block both ends.
Knee clearance ~32.9 underside is tight.

### 5.3 Counter-height table — TARGET SPEC

| Property | Value |
|---|---|
| Length | 60 – 72 |
| Depth | **30 – 36** (critical — enables two-sided seating) |
| Height | 36 (standard counter height) |
| Seats | 6 (3 per side) |

**Placement zone:** `x: 45 – 128`, `y: 0 – 30`

- Usable run: **83**
- Left bound x=45: couch depth
- Right bound x=128: radiator projection
- Stool clearance: add 24 behind each seating side
- Total projection into room with stools: ~54 → `y: 0 – 54`
- Kitchen door (x 3–35.5) stays clear

### 5.4 Stools

7 high-top chairs already owned, stored in basement. **Heights
unmeasured and varied.** Need ~26–28 seat height for a 36 table.

### 5.5 Rug — TARGET SPEC

| Property | Value |
|---|---|
| Size | **9' × 12'** (108 × 144) |
| Position | `x: 6 – 114`, `y: ~5 – 149` |

- Front legs of couch sit on rug (anchor rule)
- Far edge stops ~8 short of TV stand at x=122
- Rug pad required (hardwood + heavy couch)
- **Style:** dark, patterned. White couch + 4 roommates + Allston.

### 5.6 Coffee table — TARGET SPEC

| Property | Value |
|---|---|
| Depth | 20 – 24 |
| Position | `x: 61 – 85`, centered on couch at `y = 92` |

- 16 gap from couch face (x=45) to table
- ~37 walkway remaining between table and TV stand

### 5.7 Beer fridge — UNPLACED

EdgeStar wine fridge, currently in Belmont garage. No dimensions
recorded, no spot assigned.

---

## 6. Constraints & Preferences

### Hard constraints
1. Kitchen door (top wall, x 3–35.5) must stay clear — active traffic
2. Radiator projects 9 into room at x 128–137, y 0–41.5 — no furniture
3. TV panel must not overlap recessed cabinets (y > 118.7)
4. Couch position is fixed and settled
5. Router gap at y 148.5–155 on left wall stays open

### Soft constraints
6. TV stand *may* cover trim and *may* cover part of the cabinets
7. Porch doors stay closed — that wall run is usable
8. Ottoman may partially block the hallway doorway
9. Table should seat 4 comfortably, 5 regularly, 6 ideal — but not at
   the cost of floor space

### Sightlines
- Couch face to TV wall: 92
- 65" 4K optimal viewing: 65–98 → **in range**
- Seated eye level: ~40–42

---

## 7. Open Items

| Item | Status | Blocking |
|---|---|---|
| Ceiling height | unmeasured | accurate render |
| Couch height | unmeasured | assume 36 |
| Stool seat heights | unmeasured (7 in basement) | table height match |
| High-top table | not purchased | main layout gap |
| TV stand | candidate identified | — |
| Coffee table | spec'd, not purchased | — |
| Rug | spec'd, not purchased | — |
| Beer fridge | no dims, no location | — |

---

## 8. Render Notes

- Right-handed coordinate system, Y-down in plan view
- Doors: render as wall openings, not swinging geometry (porch doors
  stay shut; hallway is an open doorway)
- Radiator is the only wall feature with meaningful projection (9)
- Recessed cabinets are set *into* the wall — render flush or inset,
  not protruding
- Suggested material palette: hardwood floor, white walls, white/navy
  couch, dark patterned rug, natural wood table
