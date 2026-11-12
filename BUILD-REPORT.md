# BUILD REPORT — 善心之城 · Kindness City (`kindness-city`)

## 1. Visual Grammar Selection (`uniqueness.md`)

- **Chosen Grammar:** **#6 Cartographic / Field-Guide** (fused with an East Asian Illustrated Handscroll sensibility anchored directly to `kindness_city_master_scroll_2048x8256_retina.jpg`).
- **Why #6 Won:** Kindness City is a living vertical learning world spanning 2,400m from the Alpine Front Gate down to the 120m Lotus Estuary, built around the core ethos **`命好不如习惯好` (Good habits matter more than good fortune)**. A Cartographic / Field-Guide grammar turns the student's vertical scroll into an altitude-calibrated adventure through living districts where technology and nature coexist.
- **Why the Other 8 Grammars Lost:**
  1. *#1 Swiss Precision Grid:* Too clinical and rigid for a hand-inked Gongbi-meets-Ghibli learning adventure.
  2. *#2 Editorial Broadsheet:* Column-ruled newspaper framing breaks the continuous watershed landscape flow.
  3. *#3 Atmospheric Minimalism:* Would remove the cartographic elevation anchors, bilingual stamps, and Three Loves pedagogy that turn the site into a living city front gate.
  4. *#4 Kinetic Typography Poster:* Giant poster typography would cover the custom watercolor architecture and ecological storytelling.
  5. *#5 Archival Specimen Sheet:* Better suited to static artifacts than an active watershed trail linking Python quests and life habits.
  6. *#7 Noir Control Room:* Cold tactical HUD styling contradicts the warm, benevolent ethos of Kindness City.
  7. *#8 Tactile Craft Workshop:* Highlights woodwork, yet misses the continuous mountain-to-estuary adventure.
  8. *#9 Lush Botanical Monograph:* Captures nurseries and lotus blooms, yet underplays Python problem-solving and `小慈` care-bots.

---

## 2. The Signature Move & Project Vision Alignment

**The Watershed Scroll Minimap & Three-Loves Bio-Canopy Attunement (`[data-kc-scrollmap]` + `[data-kc-canopy]`):**

1. **Live Master-Scroll Minimap & Altitude Rail (`[data-kc-scrollmap]`):**
   - Fixed right-hand miniature reproduction of the full `2048 × 8256` master scroll (`assets/master-scroll-minimap.webp`) with a scroll-synchronized viewport lens (`#kc-minimap-lens`), a self-drawing SVG river path (`#kc-river-trace`), live elevation readout (`2,400m · Summit` → `120m · Lotus Hall`), clickable waypoints, and the accessible Full Scroll Atlas modal (`#atlas-modal`).
2. **Three-Loves Bio-Canopy & Python-Habit Seal (`[data-kc-canopy]`):**
   - At the Engineered Peak (**Act 4 · 三愛生機亭 · Three Loves Bio-Canopy**), visitors attune the living tree dome to the canonical Three Loves of Kindness City:
     - **爱自己 · Love Yourself** (`#52E5C7`) — *Python: `while` Habit Loop | Habit: Positive Thinking & Discipline*
     - **爱别人 · Love Others** (`#F2B857`) — *Python: `def care()` Functions | Habit: Compassion & Collaboration*
     - **爱地球 · Love the Earth** (`#8CE563`) — *Python: `if / elif` Eco Sensor | Habit: Responsibility & Eco-Care*
   - Selecting any Love updates `--kc-vow-color`, shifts the canopy's SVG aura rings, updates the live `#kc-quest-line` pairing box and editable pledge, re-tints the rising lanterns in **Act 5 (慶典大廳 · Celebration Hall)**, and exports a custom `960×540` PNG citizen certificate (`命好不如习惯好`) via `#kc-download-seal-btn`.

---

## 3. Fingerprint Gate Result (`scrollcraft/FINGERPRINTS.md`)

- First build in workspace (`kindness-city`), recorded in `scrollcraft/FINGERPRINTS.md` across all 6 structural dimensions.
- Passes all anti-template checks: `5` distinct acts (`~12.5vh` desktop), non-standard right-edge cartographic rail, 5-plane depth hero, non-repeating device families (`scrub > pan > flow > scrub > pin`), and bespoke citizen lantern close.

---

## 4. Feeling Curve & Visual Refinements (`feel.md`)

| Act | Landmark & Elevation | Intended Feeling | Device Cadence | Visual & Motion Realization | Refinements Applied |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Act 1** | **高山天文台 · The Front Gate (2,400m)** | **Wonder & Adventure** | `scrub` (`2.6vh`, `dwell=0.34`) + 5-plane `parallax` | Step through the Front Gate (`Good habits shape every tomorrow.` / `Begin the Adventure`) while snowmelt plunges down the gorge across 5 independently moving depth planes. | Added `-webkit-mask-image` / `mask-image` sky cutout (`kc-hero-mid`) on Plane 3 + oversized `116%` plane bounds so Plane 1 far snow peaks visibly move at `-0.65` parallax behind Plane 2 clouds with zero edge bleed. |
| **Act 2** | **7 Highland & Valley Districts (2,200m to 1,350m)** | **Delight & Habit Discovery** | `pan` (`6.2vh`) + `tilt` (`6deg`) | Unhurried lateral trail (`overflow = 3315px` desktop) gliding past `迎賓廣場 · Welcome Plaza`, `好奇心公園 · Curiosity Park`, `綠能驛站 · 竹水車`, `大地花園 · 梯田育苗園`, `變數村`, `迴圈河`, and `友誼廣場 · 小慈`. | Expanded Act 2 to **7 standalone district illustrations** over `6.2vh`; locked `.kc-rail__card` to `grid-template-rows: minmax(11rem, 1fr) auto` with `z-index: 2` on `.kc-rail__body` and removed forced inner image `aspect-ratio` so `.kc-rail__media` never overlaps card tags or headings under tilt. |
| **Act 3** | **Civic & Woodland Promenade + 15-District Atlas (1,280m to 1,010m)** | **Stillness & Progressive Discovery** | `flow` + `reveal` + `in` + dynamic `curriculum.json` | Alternating vertical footpath walk passing `編碼學院 · Coding Academy`, `生態資源回收站`, `資料區 · Data District`, `邏輯森林 · Logic Forest`, `創意工坊 · Creativity Workshop`, and `創新之塔 · Innovation Tower`, followed by the thumbnail-illustrated 15-District Atlas & 5-Chapter Roadmap. | Added `.kc-promenade` alternating trail stops + **4 new standalone plates** (`flow-data-district.webp`, `flow-logic-forest.webp`, `flow-creativity-workshop.webp`, `flow-innovation-tower.webp`) and added miniature thumbnails + portrait preview + quick-jump buttons for all **15/15 districts** in `#kc-curriculum-sanctuary`. |
| **Act 4 (Peak)** | **三愛生機亭 · Three Loves Bio-Canopy (980m)** | **Awe (Engineered Peak)** | `scrub` (`4.1vh`, `dwell=0.28`) + multi-plane `parallax` + `kinetic` + `[data-kc-canopy]` | Dusk-to-awakened morphing scrub (`04-biocanopy.mp4` blending `biocanopy_twilight` into `biocanopy_awakened_borderless`) paired with Three Loves (`爱自己 · 爱别人 · 爱地球`) attunement, floating `canopy-sky-lanterns.png` & blooming `canopy-fore-vines.png`, and 60fps bioluminescent spore particles. | Staged Window 1 (`0 0.35`) and Window 2 (`0.37 0.70`) cleanly before `0.70..1.00`, dissolving `.kc-canopy-scrim` open right after the Attune card so the radiant canopy eruption blossoms cleanly across the full plaza before descending into Act 5. |
| **Act 5 (Close)** | **慶典大廳 · Celebration Hall (120m)** | **Belonging & Flourishing** | `pin` (`1.4vh`) + `spotlight` + `magnet` | Rising lantern ceremony (`Acts of kindness make the city flourish.`), Pilgrim Scroll Seal preview (`命好不如习惯好`), downloadable PNG seal, and in-stage footer. | Trimmed outer paper frame from `celebration_hall_dusk` + added subtle top twilight haze glaze for a seamless dusk seam exiting Act 4; compact viewport tuning keeps buttons clear on `360×640` phones. |

---

## 5. Custom Asset Inventory (Zero-Repetition Library)

Every card, workshop, hero plane, and close stage renders its own dedicated asset in `scrollcraft/builds/kindness-city/assets/` and root `assets/`:
- **Act 1 Hero Depth Planes & Scrub Clip:** `hero-plane-1-sky-peaks.webp`, `hero-plane-2-cloud-sea.png`, `01-observatory.mp4` (`-g 8`) + `01-observatory-m.mp4` (`-g 4`), `01-poster.webp`, `01-poster-p.webp`, `hero-plane-4-observatory.png`, `hero-plane-5-fore-canopy.png`.
- **Act 2 Pan Rail (7 Separate Illustrations, `1200×900` 4:3):** `pan-00-welcome-plaza.webp` (`welcome_plaza_scene`), `pan-06-curiosity-park.webp` (`curiosity_park_scene`), `pan-01-waterwheel.webp` (Bamboo Waterwheel), `pan-02-nurseries.webp` (`terraced_nurseries_scene`), `pan-05-solvers.webp` (`front_gate_problem_solvers_scene` — Variable Village), `pan-03-loop-river.webp` (`loop_river_bend_scene`), `pan-04-little-ci.webp` (`little_ci_kindness_scene`).
- **Act 3 Civic & Woodland Promenade (6 Separate Illustrations, `1440×960` 3:2):** `flow-coding-academy.webp` (`coding_academy_scene`), `flow-recycling-pavilion.webp` (`recycling_pavilion_scene`), `flow-data-district.webp` (`data_district_scene`), `flow-logic-forest.webp` (`logic_forest_scene_borderless`), `flow-creativity-workshop.webp` (`creativity_workshop_scene`), `flow-innovation-tower.webp` (`innovation_tower_scene`).
- **Act 4 Peak Scrub Clip, Awakening Morph & Parallax Planes:** `04-biocanopy.mp4` (`-g 8`, morphing `biocanopy_twilight` into `biocanopy_awakened_borderless` with ascending root-to-crown waves & 36 pollen motes) + `04-biocanopy-m.mp4` (`-g 4`), `04-poster.webp`, `04-poster-p.webp`, plus flood-fill RGBA parallax planes `canopy-sky-lanterns.png` (`-0.32`) and `canopy-fore-vines.png` (`+0.34`, extracted from `biocanopy_floral_frame_noborder`).
- **Act 5 Close & Master Cartography:** `05-celebration-hall.webp` (borderless trim), `05-celebration-hall-p.webp` (`celebration_hall_dusk`), `master-scroll-minimap.webp`, `master-scroll-atlas.webp`.

---

- Also inside Act 3 (`#act-civic`), `#kc-curriculum-sanctuary` dynamically renders **all 15 Kindness City Districts** (*Welcome Plaza, Function Mountain, Curiosity Park, Green Energy Station, Earth Garden, Variable Village, Loop River, Friendship Square, Coding Academy, Data District, Logic Forest, Recycling Center, Creativity Workshop, Innovation Tower, Celebration Hall*) alongside **5 Progressive Learning Chapters** mapping all **19 Lessons (`L01` to `L19`, `module/l1_pyprint` through `module/l19_ai_challenge`)** directly from `data/curriculum.json` + an offline `#kc-curriculum-fallback` mirror synced by `scripts/sync_curriculum.py`.
- Alongside `#kc-minimap-strip`, a vertical `#kc-flora-svg` botanical spine progressively sprouts 5 living leaf/blossom nodes synced with `--kc-env-bloom`, visually growing nature as the learner descends through the city (rendered fully bloomed immediately under `prefers-reduced-motion: reduce`).

## 6. Verification Results (`verify_scrollcraft.py`) & Post-Card Bio-Canopy Awakening

1. **Act 1 Observatory Matte & Seamless HUD Polish (`scripts/build_assets.py`, `scripts/build_videos.py`, `index.html`):**
   - `build_clean_distant_peaks()`, flood-fill `extract_observatory_crag_rgba()` + `clean_pier_guard`, lower `sil_y = 0.935` fore canopy, locked `scale = 1.0` Act 1 video registration, top-left `.kc-corner-seal`, and Hanging Silk Handscroll Bookmark `.kc-scrollmap`.
2. **Post-Card Bio-Canopy Awakening & Multi-Plane Depth (`biocanopy_awakened_borderless`, `biocanopy_floral_frame_noborder`, `build_videos.py`, `index.html`):**
   - Generated `biocanopy_awakened_borderless` (pixel-registered illuminated transformation of `biocanopy_twilight` with glowing turquoise/gold canopy flowers, glowing boughs, lit solar cottages, and rising lanterns) plus `biocanopy_floral_frame_noborder`, flood-fill split via `extract_biocanopy_floral_planes()` into `canopy-sky-lanterns.png` (`data-sc-parallax="-0.32"`) and `canopy-fore-vines.png` (`data-sc-parallax="0.34"`, CSS `scale` bloom).
   - Updated `build_act4_video()` in `scripts/build_videos.py` to progressively morph from `biocanopy_twilight` into `biocanopy_awakened_borderless` via an ascending root-to-crown ignition wave (`t_open` -> `t_attune` -> `t_surge`), bounding-box bioluminescent pollen motes, and an upward/inward orbital push (`scale 1.02 -> 1.24`).
   - Timed `#act-canopy` (`data-sc-span="4.1"`, `dwell=0.28`) so Window 2 (`.kc-canopy-console`) fades out at `0.70` and `--kc-canopy-scrim-op` opens smoothly across `0.715..0.83`, unveiling the full animated plaza alongside blurred luminous `#kc-canopy-veins`, counter-rotating `#kc-spore-ring`, and 56 scroll-boosted `#kc-canopy-particles` spores.
   - Cropped `celebration_hall_dusk` (`34/1376` pad) in `05-celebration-hall.webp` + added top twilight haze blend so zero tan paper border appears at the Act 4 to Act 5 transition seam.

Verified across all 4 browser passes after the Act 2 card-overlap & 15-district edits (`0` dead scroll, `2/2` scrub clips active whenever on screen, `7/7` cues reach `>= 0.85`, lowest worst composited contrast `12.05:1`):
1. **Desktop (`1440×900` — `scrollcraft/lab/shots/sheet.png` & `10.png`–`15.png`):** `20.4` viewport-heights, `pan rail #1 overflow = 3315px` (`scrollWidth=4755px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`), zero image overlap across all 7 pan cards.
2. **Mobile (`390×844` — `scrollcraft/lab/mobile/sheet.png` & `13.png`):** `24.0` viewport-heights, `pan rail #1 overflow = 2753px` (`scrollWidth=3143px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`), crisp separation between card artwork and body text.
3. **Compact Phone (`360×640` — `scrollcraft/lab/compact/sheet.png` & `12.png`):** `27.4` viewport-heights, `pan rail #1 overflow = 2561px` (`scrollWidth=2921px`), all `7/7` cues reach `>= 0.85`, all `6` visible contrast-measured cues clear `4.5:1` (`lowest worst=12.05:1`; compact height intentionally hides `#kc-passport-card`).
4. **Reduced Motion (`1440×900 --reduced-motion` — `scrollcraft/lab/reduced/sheet.png`):** `20.4` viewport-heights, `pan rail #1 overflow = 3315px` (`scrollWidth=4755px`), native scroll Act 2 rail + static posters and instant full-opacity cues (`7/7` clear `4.5:1`, `lowest worst=12.05:1`).
