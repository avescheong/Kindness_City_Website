# 善心之城 · Kindness City Website

> **命好不如习惯好 — Good habits matter more than good fortune.**  
> *Technology is only an enabler. Good habits create lasting success.*

An interactive, hand-inked **scrollytelling gateway into Kindness City** built for young learners. Instead of opening a static course brochure, students step through the Alpine Front Gate at **2,400m** and travel district by district down a living watershed to the **120m Lotus Estuary** — discovering how Python programming empowers **positive thinking, discipline, creativity, perseverance, compassion, and responsibility**.

Every lesson leaves the student with **two harvests**: a concrete Python concept and a positive life habit grounded in one or more of the **Three Loves (`三愛`)**:

- **Love Yourself (`爱自己`)** — Positive thinking, daily discipline, calm debugging, and curiosity
- **Love Others (`爱别人`)** — Compassion, teamwork, listening carefully, and helping neighbors alongside `小慈` care-bots
- **Love the Earth (`爱地球`)** — Environmental stewardship, clean rivers, zero-waste sorting, renewable energy, and living forests

---

## How This Website Is Different from Typical Coding & EdTech Sites

Most coding websites present stacked white feature grids, generic dark glass boxes, or endless collapsible syllabus lists. **Kindness City** is engineered around five deliberate differences:

| Typical Coding Website | 善心之城 · Kindness City |
| :--- | :--- |
| Repeats the same centered headline + 3-column card template down the page | **Five distinct scroll choreographies** (`scrub > pan > flow > scrub > pin`) so no two consecutive sections behave alike |
| Uses generic stock photos or synthetic neon 3D blocks | **31 custom-built watercolor, flood-fill RGBA & scrubbing video assets** anchored to the `2048 × 8256` master vertical scroll (`kindness_city_master_scroll`) |
| Hides learning tracks behind static accordion text pills | **15 illustrated living districts** — visitors travel visually past every landmark (`Welcome Plaza` to `Celebration Hall`) as nature blooms along the margin |
| Portrays coding as speed, hustle, or isolated syntax drills | **Dual-Harvest Pedagogy & Environmental Storytelling** weaving solar roofs, wind turbines, rainwater harvesting, bike paths, and wildlife habitats into every stop |
| Hardcodes lesson cards directly into HTML | **Data-driven `data/curriculum.json` registry** grouping Lessons 1–19 (`module/l1_pyprint` to `module/l19_ai_challenge`) into 5 chapters that unlock and filter dynamically |

### Signature Interactive Experiences

1. **Five-Plane Parallax Alpine Gate (`Act 1` · `2,400m`):** Independent mountain ridges, drifting mist, flood-filled Mountain Observatory crag, foreground pines, and a dense-GOP scrubbing waterfall film introduce Kindness City's core philosophy.
2. **Unhurried Seven-District Valley Glide (`Act 2` · `2,200m → 1,350m`):** Vertical scroll glides laterally across *Welcome Plaza*, *Curiosity Park*, *Green Energy Station (Bamboo Waterwheel)*, *Earth Garden*, *Variable Village*, *Loop River*, and *Friendship Square (`小慈`)*.
3. **Civic & Woodland Promenade + 15-District Atlas (`Act 3` · `1,280m → 1,010m`):** An alternating footpath walk past *Coding Academy*, *Eco-Recycling Pavilion*, *Data District*, *Logic Forest*, *Creativity Workshop*, and *Innovation Tower*, ending at an interactive Three-Loves filterable explorer with thumbnail previews and direct landmark jumps.
4. **Three Loves Bio-Canopy Awakening (`Act 4` · `980m` Peak):** Selecting **Love Yourself**, **Love Others**, or **Love the Earth** attunes the living tree dome's bioluminescence, previews its Python + Habit quest, and unlocks a full-screen twilight-to-blooming canopy transformation as you scroll downward.
5. **Celebration Hall & Pilgrim Scroll Seal (`Act 5` · `120m` Close):** Release a personalized lantern across the lotus pond and download a custom `960 × 540` PNG citizen certificate (`命好不如习惯好`).
6. **Hanging Silk Handscroll Bookmark (`[data-kc-scrollmap]`):** Tracks your live elevation from `2,400m` to `120m`, animates the Loop River trace, sprouts five botanical nodes as you descend, and opens the complete master-scroll atlas modal.

---

## Architecture & Choreography Score

```text
Act 1 (scrub + 5-plane parallax)   2,400m · 高山天文台 / Function Mountain
  └── Act 2 (pan + 3D card tilt)   2,200m → 1,350m · 7 Highland & Valley Districts
        └── Act 3 (flow + reveal)  1,280m → 1,010m · 6 Civic & Woodland Pavilions + 15-District JSON Atlas
              └── Act 4 (scrub + canvas/SVG)  980m · 三愛生機亭 · Three Loves Bio-Canopy Peak
                    └── Act 5 (pin + lantern canvas)  120m · 慶典大廳 · Celebration Hall & PNG Seal
```

- **Accessible by design:** Tested across Desktop (`1440×900`), Mobile (`390×844`), Compact Phones (`360×640`), and `prefers-reduced-motion: reduce` with verified `>= 12.05:1` worst-case text contrast over imagery.

---

## Curriculum Roadmap (`data/curriculum.json`)

| Chapter | Lessons | Git Branches | Featured Districts |
| :--- | :--- | :--- | :--- |
| **Ch. I · Stepping Through the Gate** | L01 Python + `print()`, L02 Environment + Function + `#` Comment | `module/l1_pyprint`, `module/l2_env_func_comment` | Welcome Plaza, Coding Academy |
| **Ch. II · Naming & Observing Our World** | L03–L06 Variable, Practice, Data Types, Data Type Detective | `module/l3_variable` .. `module/l6_datatype_detective` | Variable Village, Earth Garden, Data District, Curiosity Park |
| **Ch. III · Clear Arithmetic & Kind Choices** | L07–L11 Arithmetic, Comparison, Boolean, `if`, `if / else` | `module/l7_arithmetic_ops` .. `module/l11_if_else` | Green Energy Station, Data District, Logic Forest, Recycling Center |
| **Ch. IV · Rivers, Rhythm & Shared Lists** | L12–L15 `for` Loop, `time.sleep()`, `list`, List + `for` Loop | `module/l12_for_loop` .. `module/l15_list_for_loop` | Loop River, Creativity Workshop, Friendship Square |
| **Ch. V · Perseverance, Listening & Kind AI** | L16–L19 `while` Loop, Challenge, `input()`, Python AI Challenge | `module/l16_while_loop` .. `module/l19_ai_challenge` | Green Energy Station, Function Mountain, Celebration Hall, Innovation Tower |

---

## Repository Layout

```text
Kindness_City_Website/
├── index.html                  # Complete semantic scrollytelling landing page & interactive widgets
├── scrollcraft.css             # Core layout tokens & responsive scroll floor (do not modify)
├── scrollcraft.js              # Smooth scrubbing, parallax & reveal runtime (do not modify)
├── data/
│   └── curriculum.json         # Single source of truth for all 15 districts & 19 lessons
├── assets/                     # 31 active WebP plates, RGBA cutout planes & dense-GOP H.264 MP4s
├── scripts/
│   └── sync_curriculum.py      # Refreshes the inline offline JSON snapshot inside index.html
├── .nojekyll                    # Serves cleanly on GitHub Pages with no Jekyll build needed
├── BRIEF.md                    # Authored creative brief & feeling curve
├── BUILD-REPORT.md             # Visual refinement log, asset manifest & browser verification scores
└── agent.md                    # Coding-agent continuity guide & handover log
```

## Extending Lessons & Local Preview

1. Add or edit districts, ecological infrastructure tags, chapters, or lessons in `data/curriculum.json`.
2. Refresh the embedded offline fallback inside `index.html`:
   ```bash
   python scripts/sync_curriculum.py
   ```
3. Preview locally over HTTP (recommended so browser range requests and `fetch('data/curriculum.json')` run cleanly):
   ```bash
   python -m http.server 4500
   ```
   Open `http://localhost:4500` in your browser.

## Static Deployment

No Node bundler or build step is required. Push to GitHub and enable **GitHub Pages** (branch `main`, folder `/ (root)`), or connect directly to **Netlify** / **Vercel** / any static file host.
