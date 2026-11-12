# AGENT.md · 善心之城 · Kindness City (`scroll-craft` Handoff Guide)

Welcome, next agent. This file documents the architecture, asset pipeline, verification harness, and design constraints for the **善心之城 · Kindness City** scroll-driven landing page built with the [`scroll-craft`](https://github.com/nateherkai/scroll-craft) skill pack (`v0.3.0`, approved ten-site collection standard).

---

## Mandatory Rule: Task-Completion Handover Protocol

> **ENFORCED ON EVERY TASK COMPLETION:** Every time you finish a task in this workspace (feature work, bug fix, asset rebuild, copy edit, or configuration/documentation change), you **MUST** complete the handover steps below **before** sending your final response to the user.

1. **Sync Canonical Build & Root Mirrors *(if HTML, brief, report, or assets changed)*:**
   - Copy updated files between `scrollcraft/builds/kindness-city/` (`index.html`, `BRIEF.md`, `BUILD-REPORT.md`, `assets/*`) and the workspace root (`f:\000_Ai Project\FlashGame\`) using the sync commands in **Section 5**.
   - Never modify `scrollcraft.js` or `scrollcraft.css`.
2. **Run Required Verification *(if UI, code, styles, scripts, or assets changed)*:**
   - Re-run `build_assets.py` / `build_videos.py` if source artwork or video logic changed.
   - Run `scripts/verify_scrollcraft.py` across all 4 passes (Desktop `1440x900`, Mobile `390x844`, Compact Phone `360x640`, and `--reduced-motion`) and visually inspect each `sheet.png`.
   - Confirm `0` console/network errors, zero dead scroll, continuous scrub playback, cue peaks `>= 0.85`, pan rail overflow `> 0`, and composited contrast `>= 4.5:1`.
3. **Update Build Ledgers *(when scope, architecture, or builds change)*:**
   - Append to `scrollcraft/FINGERPRINTS.md` if adding a new build or altering any of the 6 structural fingerprint dimensions.
   - Update `BUILD-REPORT.md` (both canonical and root copies) if pacing, visual grammar, assets, or verification scores change.
4. **Record a Handover Entry in `agent.md` (**Section 7**) & Refresh Backlog (**Section 6**):**
   - Add a new dated entry at the top of **Section 7 (Handover Log)** covering:
     - **Timestamp & Task Summary:** What the user requested and what was completed.
     - **Files Added / Modified:** Exact workspace paths.
     - **Verification Status:** Exact commands run and observed results (state explicitly if any check was skipped because the change was docs-only, or if only a subset of viewports ran).
     - **Open Issues / Constraints / Decisions:** Any caveats, edge cases, or design decisions the next agent must preserve.
     - **Next Steps for Next Agent:** Concrete starting point for continuation.
   - Cross off completed items or add newly discovered follow-ups in **Section 6**.
5. **Confirm Handover in Final Reply:**
   - End your final response to the user by confirming that `agent.md` was updated with the task handover entry.

---

## 1. Repository & Workspace Map

```text
f:\000_Ai Project\FlashGame\
├── agent.md                                      # This handoff guide & mandatory handover log
├── BRIEF.md                                      # Mirror of the canonical build brief
├── BUILD-REPORT.md                               # Mirror of the canonical build & verification report
├── index.html                                    # Root-served mirror of the finished landing page
├── scrollcraft.css                               # Untouched scroll-craft CSS engine (synced)
├── scrollcraft.js                                # Untouched scroll-craft JS runtime (synced)
├── assets\                                       # Root mirror of all production WebP, PNG & MP4 assets
├── data\
│   └── curriculum.json                           # Root mirror of the expandable 15-district & 19-lesson JSON registry
├── kindness_city_master_scroll_2048x8256_retina.jpg  # Supplied 2048x8256 master vertical scroll artwork
├── Scrollcraft.zip                               # Original supplied skill pack archive
├── scroll-craft\                                 # Extracted scroll-craft skill pack (SKILL.md, references/, engine/, scripts/)
├── .agents\skills\scroll-craft\                  # Agent skill discovery copy of scroll-craft
├── scripts\
│   ├── build_assets.py                           # Extracts RGBA alpha planes, cleaned WebP plates & minimap from master scroll
│   ├── build_videos.py                           # Synthesizes & encodes dense-GOP H.264 scrub clips (-g 8 / -g 4) + WebP posters
│   ├── sync_curriculum.py                        # Syncs curriculum.json -> root mirror & embedded #kc-curriculum-fallback snapshot
│   └── verify_scrollcraft.py                     # Headless Chrome (CDP) + FFmpeg verification harness (shoot.mjs port)
└── scrollcraft\                                  # Canonical scroll-craft workspace
    ├── FINGERPRINTS.md                           # Append-only fingerprint registry (6 dimensions per build)
    ├── builds\
    │   └── kindness-city\                        # Canonical build directory
    │       ├── BRIEF.md                          # Step 0-2 brief, feeling curve, layer contract & score table
    │       ├── BUILD-REPORT.md                   # Verification evidence, feel-check diff & fingerprint gate record
    │       ├── index.html                        # Canonical semantic HTML + token overrides + bespoke signature move
    │       ├── scrollcraft.css                   # Engine stylesheet (NEVER edit per project)
    │       ├── scrollcraft.js                    # Engine runtime (NEVER edit per project)
    │       ├── data\
    │       │   └── curriculum.json               # Canonical expandable JSON registry (15 districts, 5 chapters, 19 lessons)
    │       └── assets\                           # Production assets for the build
    └── lab\
        ├── shots\                                # Desktop (1440x900) verification frames, sheet.png & report.json
        ├── mobile\                               # Mobile (390x844) verification frames, sheet.png & report.json
        ├── compact\                              # Compact phone (360x640) verification frames, sheet.png & report.json
        └── reduced\                              # Reduced-motion verification frames, sheet.png & report.json
```

> **Synchronization Rule:** Whenever you edit `scrollcraft/builds/kindness-city/index.html`, `BRIEF.md`, `BUILD-REPORT.md`, or `assets/*`, copy the updated files to the root (`f:\000_Ai Project\FlashGame\`) so the project works seamlessly whether served from the workspace root or from `scrollcraft/builds/kindness-city/`.

---

## 2. Toolchain on This Machine

1. **Python 3.13** (`C:\Program Files\Python313\python.exe` — available as `python` on PATH):
   - Installed packages include `pillow`, `numpy`, `httpx`, `websockets`, `uvicorn`, `matplotlib`.
2. **Full FFmpeg 9.0 Build** (587 filters, includes `libx264`, `libwebp`, `scale`, `tile`, `psnr`):
   - Path: `C:\Users\Asus\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin\ffmpeg.exe`
3. **Google Chrome** (with hardware/software H.264 decoder required for scrub video verification):
   - Path: `C:\Program Files\Google\Chrome\Application\chrome.exe`
4. **Why `scripts/*.py` exist alongside `scroll-craft/scripts/*.mjs`:**
   - Node.js is not currently on the default system PATH on this machine. To ensure zero-friction asset building and mechanical verification without requiring Node installation, `scripts/build_assets.py`, `scripts/build_videos.py`, and `scripts/verify_scrollcraft.py` execute the exact `scroll-craft` pipelines using Python 3.13 + Chrome DevTools Protocol (CDP) + FFmpeg 9.0. If Node.js is added later, the original `scroll-craft/scripts/*.mjs` scripts are also preserved intact in `scroll-craft/scripts/`.

---

## 3. Page Architecture & Design Decisions

### 3.1 World & Style Preamble (`scroll-craft/references/worlds.md`)
**善心之城 · Kindness City** is a genuinely illustrated world anchored by `kindness_city_master_scroll_2048x8256_retina.jpg`. Every generated companion asset uses this exact verbatim **Style Preamble**:

> `"Hand-inked East Asian botanical and architectural scroll illustration with luminous watercolor washes on warm antique parchment paper. Fine dark sepia ink outlines, soft mineral green, turquoise river blue, warm cedar timber, and golden lantern highlights. Studio Ghibli and Song Dynasty blue-green landscape scroll aesthetic, warm organic paper grain. No text, no letters, no watermarks, no 3D plastic CGI."`

### 3.2 Page Grammar: `Cartographic Living Scroll` (`cartographic-scroll`)
- **Organizing Logic:** The visitor descends a painted vertical watershed from the **2,400m Alpine Summit (`高山天文台`)** down to the **120m Lotus Estuary (`慶典大廳 · 迎向未來`)**.
- **Explicit Structural Bans:**
  1. **No top marketing bar:** Replaced by a corner scroll seal (`.kc-corner-seal`) + a persistent right-edge **Master-Scroll Watershed Minimap & Altitude Rail (`[data-kc-scrollmap]`)**.
  2. **No invented stat counters (`[data-sc-count]`):** Strictly banned for illustrated/concept worlds per `devices.md` §7.
  3. **No identical 3-column card grids, no `01 / 06` section counters, no scroll nudge arrows, and no em dashes (`—`).**
  4. **At most two `scrub` acts**, and **never the same device family twice in a row**.

### 3.3 Act Score, Feeling Curve & Engineered Peak (`5 Acts, ~12.5vh`)

| Act | ID & Elevation | Master Scroll Landmark | Emotion | Device Family | Span / Config |
|---|---|---|---|---|---|
| **Act 1** | `#act-summit` (`2,400m`) | `高山天文台` · Front Gate Observatory & Waterfall | **Wonder** | `scrub` + 5-plane `parallax` | `data-sc-act="scrub"` `data-sc-span="2.6"` `data-sc-dwell="0.34"` |
| **Act 2** | `#act-watershed` (`1,650m`) | `竹水車` · `梯田育苗園` · `迴圈河` · `小慈` · `迎向未來` | **Delight** | `pan` + `tilt` | `data-sc-act="pan"` `data-sc-span="3.4"` `data-sc-pan="0.06"` |
| **Act 3** | `#act-civic` (`1,280m`) | `編碼學院` & `生態資源回收站` | **Stillness** *(Quiet before Peak)* | `flow` + `reveal` + `in` | `data-sc-act="flow"` (~`1.5vh`, reduced top padding) |
| **Act 4 (PEAK)** | `#act-canopy` (`980m`) | `三愛生機亭` · Three Loves Bio-Canopy | **Awe** *(Engineered Peak)* | `scrub` + `pin` + `kinetic` + `[data-kc-canopy]` | `data-sc-act="scrub"` `data-sc-span="3.8"` `data-sc-dwell="0.45"` |
| **Act 5 (CLOSE)** | `#act-celebration` (`120m`) | `慶典大廳` · Lotus Pond & `迎向未來` | **Belonging** *(Resolved Ending)* | `pin` + `spotlight` + `magnet` | `data-sc-act="pin"` `data-sc-span="1.4"` |

### 3.4 Act 1 Hero Layer Contract (`hero-depth.md` & `devices.md` §6)
1. **Plane 1 (`assets/hero-plane-1-sky-peaks.webp`):** Far snow peaks & dawn parchment sky (`data-sc-parallax="-0.65"`, revealed cleanly behind Plane 3 via `.kc-hero-mid` CSS mask-image gradient), with the right-hand observatory removed so it never duplicates Plane 4.
2. **Plane 2 (`assets/hero-plane-2-cloud-sea.png`):** Genuine RGBA translucent alpine cloud band (`data-sc-parallax="-0.42"`).
3. **Plane 3 (`assets/01-observatory.mp4` + `assets/01-poster.webp`):** Midground gorge & scrubbing turquoise waterfall (`data-sc-scrub`, masked across the upper sky with `.kc-hero-mid` so Plane 1 moves independently behind it).
4. **Plane 4 (`assets/hero-plane-4-observatory.png`):** Genuine RGBA cutout of `高山天文台` (Mountain Observatory) anchored to its rocky eastern crag (`data-sc-parallax="-0.18"`).
5. **Plane 5 (`assets/hero-plane-5-fore-canopy.png`):** Genuine RGBA pine & bamboo foreground framing (`data-sc-parallax="0.28"`), shaped to dip low under `.sc-copy--lead` and filled solid below its silhouette, topped by `.kc-hero-floor` gradient fade.

### 3.5 Signature Move (`[data-kc-scrollmap]` + `[data-kc-canopy]`)
1. **Live Master-Scroll Minimap & River Trace (`[data-kc-scrollmap]`):** Tracks scroll position on a miniature strip of `kindness_city_master_scroll_2048x8256_retina.jpg`, animates the turquoise Loop River (`#kc-river-trace`) via SVG `stroke-dashoffset`, updates the altitude readout (`2,400m` → `120m`), and opens the **Full Master Scroll Atlas Modal (`#atlas-modal`)**.
2. **Three-Loves Bio-Canopy Attunement & Downloadable Citizen Seal (`[data-kc-canopy]`):** In Act 4, visitors attune the living tree dome to **爱自己 (Love Yourself)**, **爱别人 (Love Others)**, or **爱地球 (Love the Earth)** to preview each Love's **Python Concept + Positive Habit** quest pairing (`#kc-quest-line`) and customize their pledge. This selection updates `--kc-vow-color`, carries into Act 5's **Celebration Hall Lanterns (`#kc-lantern-canvas`)**, updates the **Pilgrim Scroll Seal Card (`命好不如习惯好`)**, and exports a custom-rendered `960×540` PNG certificate via `#kc-download-seal-btn`.

---

## 4. Non-Negotiable `scroll-craft` Rules for Future Edits

1. **Never edit `scrollcraft.js` or `scrollcraft.css`.** All styling and bespoke behaviors live in `index.html`.
2. **Scrims must be siblings of `[data-sc-cue]`, never children.** The contrast verification harness hides `[data-sc-cue], [data-sc-cue] *` when photographing the backdrop. If you attach a scrim inside a cue element or as `.my-cue::before`, the harness will hide your scrim and report a false contrast failure.
3. **Only Act 5 (the final act) may use one-value hold cues (`data-sc-cue="0.06"`).** Every cue on Act 1 and Act 4 must use a two-value window that closes at or before `1.0`.
4. **Magnetic CTAs (`[data-sc-magnet]`) must include `data-sc-rise="0"`** when paired with `data-sc-cue` so `cue` and `magnet` do not fight over `transform`.
5. **Videos must be encoded for scrubbing (dense GOP), not playback:**
   - Desktop: `-g 8 -keyint_min 8 -sc_threshold 0 -crf 20 -pix_fmt yuv420p -an -movflags +faststart`
   - Mobile: `-g 4 -keyint_min 4 -sc_threshold 0 -crf 24 -pix_fmt yuv420p -an -movflags +faststart`
   - Posters (`01-poster.webp`, `04-poster.webp`) must be extracted from the **encoded** `.mp4` files, never from pre-encode stills.

---

## 5. Commands to Rebuild Assets & Run Verification

### Rebuild Static WebP Plates & RGBA Alpha Cutouts
```powershell
python "f:\000_Ai Project\FlashGame\scripts\build_assets.py"
```

### Rebuild & Encode Dense-GOP Scrub Videos + Posters
```powershell
python "f:\000_Ai Project\FlashGame\scripts\build_videos.py"
```

### Run the Full Verification Suite (Desktop, Mobile, Compact Phone, Reduced Motion)
```powershell
# 1. Desktop (1440x900)
python "f:\000_Ai Project\FlashGame\scripts\verify_scrollcraft.py" --out "f:\000_Ai Project\FlashGame\scrollcraft\lab\shots" --width 1440 --height 900

# 2. Mobile (390x844)
python "f:\000_Ai Project\FlashGame\scripts\verify_scrollcraft.py" --out "f:\000_Ai Project\FlashGame\scrollcraft\lab\mobile" --width 390 --height 844

# 3. Compact Phone (360x640)
python "f:\000_Ai Project\FlashGame\scripts\verify_scrollcraft.py" --out "f:\000_Ai Project\FlashGame\scrollcraft\lab\compact" --width 360 --height 640

# 4. Reduced Motion (1440x900, prefers-reduced-motion: reduce)
python "f:\000_Ai Project\FlashGame\scripts\verify_scrollcraft.py" --out "f:\000_Ai Project\FlashGame\scrollcraft\lab\reduced" --width 1440 --height 900 --reduced-motion
```

### Sync Curriculum JSON Registry & Canonical Build to Root
```powershell
python "f:\000_Ai Project\FlashGame\scripts\sync_curriculum.py"
Copy-Item "f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BRIEF.md" "f:\000_Ai Project\FlashGame\BRIEF.md" -Force
Copy-Item "f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BUILD-REPORT.md" "f:\000_Ai Project\FlashGame\BUILD-REPORT.md" -Force
Copy-Item "f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\assets\*" "f:\000_Ai Project\FlashGame\assets\" -Force
```

---

## 6. Backlog & Ideas for the Next Agent

1. **Interactive Bilingual Toggle (`EN / 繁體中文`):** All landmark names already pair Traditional Chinese and English (`高山天文台 · Mountain Observatory`). You can add a zero-reflow prose toggle that switches body descriptions between English and Traditional Chinese while keeping the one-line CTA constraint intact.
2. **District Detail Modals on the Full Scroll Atlas:** Inside `#atlas-modal`, add clickable SVG hotspot pins over the 10 landmarks on `assets/master-scroll-atlas.webp` that preview architectural notes for each building.
3. **Second Build in Workspace (`scrollcraft/builds/<next-name>`):** If asked to build a second page (e.g., a dedicated interactive surface for `編碼學院 · Coding Academy`), check `scrollcraft/FINGERPRINTS.md` first and ensure the new build differs on at least **4 of 6 dimensions** (grammar, nav treatment, hero device, act-sequence shape, close pattern, signature move).

---

## 7. Handover Log (Newest Entry First)

Use this template for every completed task:

```markdown
### [YYYY-MM-DD HH:MM] — <Short Task Title>
- **Request:** <What the user asked for>
- **Summary of Changes:** <What was built, fixed, or updated>
- **Files Touched:** `<path1>`, `<path2>`
- **Verification Status:** <Exact commands run + pass/fail/caveats, or "Docs-only edit; runtime verification skipped">
- **Constraints / Open Decisions:** <Anything important for the next agent>
- **Next Recommended Steps:** <Where the next agent should start>
```

### [2026-11-12 20:24] — Pack Clean Static Website Copy for GitHub (`D:\000. GITHUB\Kindness_City_Website`)
- **Request:** User asked to pack a clean copy to `D:\000. GITHUB\Kindness_City_Website` to prepare for a future GitHub push (without initializing/pushing yet).
- **Summary of Changes:**
  - Copied verified runtime website (`index.html`, `scrollcraft.css`, `scrollcraft.js`, `data/curriculum.json`), docs (`BRIEF.md`, `BUILD-REPORT.md`, `agent.md`), and the exact **31 referenced files** in `assets/` (excluding unused legacy plates `02-waterwheel-wide.webp`, `03-civic-terrace-wide.webp`, `.zip`, master retina JPG, Chrome profiles, and lab screenshots) into `D:\000. GITHUB\Kindness_City_Website`.
  - Added GitHub-ready `.gitignore`, `.nojekyll`, [`README.md`](file:///D:/000.%20GITHUB/Kindness_City_Website/README.md), and a portable relative-path [`scripts/sync_curriculum.py`](file:///D:/000.%20GITHUB/Kindness_City_Website/scripts/sync_curriculum.py).
  - Left Git uninitialized / unpushed per user request.
- **Files Touched:**
  - `D:\000. GITHUB\Kindness_City_Website\{index.html,scrollcraft.css,scrollcraft.js,data\curriculum.json,assets\*,BRIEF.md,BUILD-REPORT.md,agent.md,README.md,.gitignore,.nojekyll,scripts\sync_curriculum.py}`
  - `f:\000_Ai Project\FlashGame\agent.md`
- **Verification Status:** Ran portable `scripts/sync_curriculum.py` (`Synced 15 districts and 19 lessons into index.html.`), verified `refs == actual` across all 31 assets, audited package size (`42` files, `41.35 MB` total, largest file `assets\04-biocanopy.mp4` at `7.34 MB`), and confirmed SHA256 parity of `index.html`, `scrollcraft.css`, `scrollcraft.js`, and `data\curriculum.json` against workspace root. Browser screenshots were not re-run since page HTML/CSS/assets did not change from the `[2026-11-12 20:06]` verified build.
- **Constraints / Open Decisions:** No `git init` or remote push was executed; ready for `git init` whenever the user is ready.
- **Next Recommended Steps:** In `D:\000. GITHUB\Kindness_City_Website`, run `git init`, add remote, commit, and push when ready.

### [2026-11-12 20:06] — Fix Act 2 Pan Card Image-Over-Text Overlap (`kc-rail__card` Grid & Z-Index Layering)
- **Request:** User attached a screenshot (`media_1794483857743_97879837.jpg`) showing `.kc-rail__media` overlapping and blocking `.kc-rail__tag` and card headings (`While Loops + Discipline`, `Conditionals + Positive Mind`, `For-In Iteration + Perseverance`) inside `.kc-rail__card`.
- **Summary of Changes:**
  - [`scrollcraft/builds/kindness-city/index.html`](file:///f:/000_Ai%20Project/FlashGame/scrollcraft/builds/kindness-city/index.html) — Replaced `aspect-ratio: 4 / 3` + `grid-template-rows: auto 1fr` on `.kc-rail__card` with `grid-template-rows: minmax(11rem, 1fr) auto` (`height: min(82vh, 45rem)` on `.kc-rail`), placed `.kc-rail__media` cleanly at `z-index: 1; height: 100%; min-height: 0;` and `.kc-rail__body` at `position: relative; z-index: 2;` with compact desktop heading scale (`clamp(1.18rem, 1.4vw + 0.45rem, 1.55rem)`), and tuned `@media (max-width: 860px)` (`minmax(10.5rem, 1fr) auto`) and `@media (max-height: 680px)` (`minmax(9.5rem, 1fr) auto`).
  - Synced canonical `index.html` and `BUILD-REPORT.md` to root via `sync_curriculum.py` + `Copy-Item`, verified SHA256 parity.
- **Files Touched:**
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\index.html` & `f:\000_Ai Project\FlashGame\index.html`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BUILD-REPORT.md` & `f:\000_Ai Project\FlashGame\BUILD-REPORT.md`
  - `f:\000_Ai Project\FlashGame\agent.md`
- **Verification Status:** `verify_scrollcraft.py` passed across all 4 viewports after final CSS fix (`0` dead scroll, `2/2` scrub clips active, `7/7` cues reaching `>= 0.85`), with `shots/10.png..15.png`, `mobile/13.png`, `compact/12.png`, and all 4 contact sheets inspected confirming zero overlap:
  - Desktop (`1440x900`): `20.4` vh, `overflow=3315px` (`scrollWidth=4755px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
  - Mobile (`390x844`): `24.0` vh, `overflow=2753px` (`scrollWidth=3143px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
  - Compact (`360x640`): `27.4` vh, `overflow=2561px` (`scrollWidth=2921px`), `6` visible contrast-measured cues clear `4.5:1` (`lowest worst=12.05:1`).
  - Reduced Motion (`1440x900 --reduced-motion`): `20.4` vh, `overflow=3315px` (`scrollWidth=4755px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
- **Constraints / Open Decisions:** Never apply a rigid height-expanding `aspect-ratio` inside a capped-height `.kc-rail__card` media track alongside GPU-promoted `data-sc-tilt`; keep `minmax(..., 1fr) auto` + explicit `z-index` separation.
- **Next Recommended Steps:** Proceed to Section 6 backlog items when requested.

### [2026-11-12 19:58] — Complete 15-District Visual Assets & Extended Landmark-by-Landmark City Journey
- **Request:** User pointed out missing artwork in the 15-district list (`media_1794483668046_74131fe7.jpg`) and asked to make the scroll longer so students travel asset by asset through Kindness City enjoying the journey.
- **Summary of Changes:**
  1. Generated all 6 missing standalone borderless 16:9 watercolor district scenes via `image-generator` (`welcome_plaza_scene`, `curiosity_park_scene`, `data_district_scene`, `logic_forest_scene_borderless`, `creativity_workshop_scene`, `innovation_tower_scene`).
  2. [`scripts/build_assets.py`](file:///f:/000_Ai%20Project/FlashGame/scripts/build_assets.py) — Exported `pan-00-welcome-plaza.webp` & `pan-06-curiosity-park.webp` (`1200x900` 4:3) and `flow-data-district.webp`, `flow-logic-forest.webp`, `flow-creativity-workshop.webp`, & `flow-innovation-tower.webp` (`1440x960` 3:2) to both canonical and root `assets/`.
  3. [`scrollcraft/builds/kindness-city/data/curriculum.json`](file:///f:/000_Ai%20Project/FlashGame/scrollcraft/builds/kindness-city/data/curriculum.json) — Added `"image"` paths (now 15/15 unique illustrated district plates), calibrated `unlockAt` milestones across the longer page (`14 / 15` blooming on arrival at `#kc-curriculum-sanctuary`), and linked exact `#stop-*` scroll anchors.
  4. [`scrollcraft/builds/kindness-city/index.html`](file:///f:/000_Ai%20Project/FlashGame/scrollcraft/builds/kindness-city/index.html) — Extended Act 2 `#act-watershed` (`data-sc-span="6.2"`) across all 7 highland/valley stations; built `.kc-promenade` in Act 3 as an unhurried alternating footpath stroll passing `Coding Academy`, `Recycling Center`, `Data District`, `Logic Forest`, `Creativity Workshop`, and `Innovation Tower`; upgraded `#kc-district-strip` chips with `28x20px` landscape thumbnails and `#kc-district-detail` with a full-width illustration preview and `Visit Stop` jump button.
  5. Updated `BRIEF.md` & `BUILD-REPORT.md`, ran `build_assets.py` & `sync_curriculum.py`, verified all 15/15 district assets + 19 lessons in JSON, and mirrored all canonical files to root.
- **Files Touched:**
  - `f:\000_Ai Project\FlashGame\scripts\build_assets.py`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\data\curriculum.json` & `f:\000_Ai Project\FlashGame\data\curriculum.json`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\index.html` & `f:\000_Ai Project\FlashGame\index.html`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BRIEF.md` & `f:\000_Ai Project\FlashGame\BRIEF.md`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BUILD-REPORT.md` & `f:\000_Ai Project\FlashGame\BUILD-REPORT.md`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\assets\{pan-00-welcome-plaza,pan-06-curiosity-park,flow-data-district,flow-logic-forest,flow-creativity-workshop,flow-innovation-tower}.webp` & root mirrors
  - `f:\000_Ai Project\FlashGame\agent.md`
- **Verification Status:** `verify_scrollcraft.py` passed across all 4 viewports after final asset/code edits (`0` dead scroll, `2/2` scrub clips active whenever on screen, `7/7` cues reaching `>= 0.85`), with all 4 contact sheets + frames (`18.png`–`20.png`) visually inspected:
  - Desktop (`1440x900` — `scrollcraft/lab/shots/sheet.png`): `20.4` vh, `overflow=3315px` (`scrollWidth=4755px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
  - Mobile (`390x844` — `scrollcraft/lab/mobile/sheet.png`): `24.0` vh, `overflow=2683px` (`scrollWidth=3073px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
  - Compact (`360x640` — `scrollcraft/lab/compact/sheet.png`): `27.4` vh, `overflow=2497px` (`scrollWidth=2857px`), `6` visible contrast-measured cues clear `4.5:1` (`lowest worst=12.05:1`; compact height hides `#kc-passport-card`).
  - Reduced Motion (`1440x900 --reduced-motion` — `scrollcraft/lab/reduced/sheet.png`): `20.4` vh, `overflow=3315px` (`scrollWidth=4755px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
- **Constraints / Open Decisions:** Never edit `scrollcraft.js` or `scrollcraft.css`; keep `.kc-promenade-media` `data-sc-reveal-at` windows early (`0.01..0.64`) inside the `flow` act so cards uncover completely before centering on tall screens.
- **Next Recommended Steps:** Tackle an item from Section 6 (`EN / 繁體中文` toggle or interactive lesson branch modal preview).

### [2026-11-12 09:38] — Animated Post-Card Bio-Canopy Awakening, Parallax Foliage & Borderless Celebration Hall Seam
- **Request:** User attached a screenshot (`media_1794445225519_e580b303.jpg`) and requested making the background Bio-Canopy animate dynamically when scrolling down after the **Attune the Three Loves Bio-Canopy** card (with new assets allowed).
- **Summary of Changes:**
  1. Generated two new style-matched illustrations in the artifact dir (`biocanopy_awakened_borderless_1794446349675.jpg` pixel-registered full bioluminescent blossom state of `biocanopy_twilight`, and `biocanopy_floral_frame_noborder_1794446348718.jpg` borderless willow vine & sky lantern framing plate).
  2. [`scripts/build_assets.py`](file:///f:/000_Ai%20Project/FlashGame/scripts/build_assets.py) — Added `extract_biocanopy_floral_planes()` to flood-fill isolate `canopy-sky-lanterns.png` (`-0.32` parallax) and `canopy-fore-vines.png` (`+0.34` parallax) cleanly while protecting candle highlights via `~is_lantern_zone`; cropped the outer paper margin (`34/1376` pad) on `celebration_hall_dusk` + top dusk glaze for a seamless `05-celebration-hall.webp` transition seam.
  3. [`scripts/build_videos.py`](file:///f:/000_Ai%20Project/FlashGame/scripts/build_videos.py) — Updated `build_act4_video()` so `04-biocanopy.mp4` (`-g 8` desktop / `-g 4` mobile) smoothly morphs from `biocanopy_twilight` into `biocanopy_awakened_borderless` with a rising root-to-crown ignition wave (`t_open -> t_attune -> t_surge`), 36 fast local-slice ascending pollen motes, and an upward orbital canopy push (`scale 1.02 -> 1.24`).
  4. [`scrollcraft/builds/kindness-city/index.html`](file:///f:/000_Ai%20Project/FlashGame/scrollcraft/builds/kindness-city/index.html) — Adjusted `#act-canopy` timing (`data-sc-span="4.1"`, `dwell=0.28`) so Window 2 (`0.37 0.70`) clears before the post-card awakening (`0.70..1.00`), dissolving `--kc-canopy-scrim-op` (`1 -> 0.14` across `0.715..0.83`) to reveal the full illuminated square; layered `canopy-sky-lanterns.png`, scaling `canopy-fore-vines.png`, blurred sapphire `#kc-canopy-veins`, counter-rotating `#kc-spore-ring`, and 56 Three-Loves-tinted scroll-reactive `#kc-canopy-particles` spores.
  5. Updated `BRIEF.md` & `BUILD-REPORT.md`, ran `build_assets.py`, `build_videos.py`, and `sync_curriculum.py` (`Synced 15 districts and 19 lessons cleanly.`), and mirrored updates to root.
- **Files Touched:**
  - `f:\000_Ai Project\FlashGame\scripts\build_assets.py`
  - `f:\000_Ai Project\FlashGame\scripts\build_videos.py`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\index.html` & `f:\000_Ai Project\FlashGame\index.html`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BRIEF.md` & `f:\000_Ai Project\FlashGame\BRIEF.md`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BUILD-REPORT.md` & `f:\000_Ai Project\FlashGame\BUILD-REPORT.md`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\assets\{canopy-sky-lanterns.png,canopy-fore-vines.png,04-biocanopy.mp4,04-biocanopy-m.mp4,04-poster.webp,04-poster-p.webp,05-celebration-hall.webp,05-celebration-hall-p.webp}` & root mirrors
  - `f:\000_Ai Project\FlashGame\agent.md`
- **Verification Status:** `verify_scrollcraft.py` passed across all 4 viewports after final asset/code edits (`0` dead scroll, `2/2` scrub clips active whenever on screen, `7/7` cues reaching `>= 0.85`), with all 4 contact sheets + frames visually verified:
  - Desktop (`1440x900` — `scrollcraft/lab/shots/sheet.png`, `30.png`, `32.png`): `14.3` vh, `overflow=2285px` (`scrollWidth=3725px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
  - Mobile (`390x844` — `scrollcraft/lab/mobile/sheet.png`, `30.png`): `16.8` vh, `overflow=2016px` (`scrollWidth=2406px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
  - Compact (`360x640` — `scrollcraft/lab/compact/sheet.png`): `18.7` vh, `overflow=1878px` (`scrollWidth=2238px`), `6` visible contrast-measured cues clear `4.5:1` (`lowest worst=12.05:1`; compact height hides `#kc-passport-card`).
  - Reduced Motion (`1440x900 --reduced-motion` — `scrollcraft/lab/reduced/sheet.png`): `14.3` vh, `overflow=2285px` (`scrollWidth=3725px`), `7/7` cues clear `4.5:1` (`lowest worst=12.05:1`).
- **Constraints / Open Decisions:** Never edit `scrollcraft.js` or `scrollcraft.css`; keep `#kc-canopy-particles` / `#kc-canopy-svg` / new Act 4 parallax plates behind `.kc-canopy-scrim` (`z-index: 2` < `z-index: 3`) so Window 1/2 cue contrast stays `>= 12:1`.
- **Next Recommended Steps:** Tackle an item from Section 6 (`EN / 繁體中文` toggle or Full Scroll Atlas hotspot pins) when requested.

### [2026-11-12 09:16] — Seamless Act 1 Observatory Matte, Registered Video & Hanging Handscroll Bookmark Polish
- **Request:** User attached a screenshot of the top-right Observatory & `.kc-scrollmap` area (`media_1794445124246_563fcc36.jpg`) and asked to make that region nicer and more seamless.
- **Summary of Changes:**
  1. [`scripts/build_assets.py`](file:///f:/000_Ai%20Project/FlashGame/scripts/build_assets.py) — Added `build_clean_distant_peaks()` (mirrored ridge continuation replacing the horizontal peak streak in `hero-plane-1-sky-peaks.webp`), replaced blurred edge extraction with ink-contour flood-fill sky matting (`extract_observatory_crag_rgba()` + `clean_pier_guard`) for a halo-free `hero-plane-4-observatory.png`, and adjusted `hero-plane-5-fore-canopy.png` (`sil_y = 0.935`) to remove the duplicate stone bridge slice.
  2. [`scripts/build_videos.py`](file:///f:/000_Ai%20Project/FlashGame/scripts/build_videos.py) — Updated `build_act1_video()` in `01-observatory.mp4` to use locked `scale = 1.0` registration over the observatory-removed ridge so waterfall mist, spray, and sunbeams animate without parallax double-edges against Plane 4/5.
  3. [`scrollcraft/builds/kindness-city/index.html`](file:///f:/000_Ai%20Project/FlashGame/scrollcraft/builds/kindness-city/index.html) — Returned `.kc-corner-seal` to Top-Left with `.kc-act-civic` top clearance (`clamp(4.6rem, 7.5vh, 6rem)`), freeing 100% of the Observatory rooster weather vane and sunlit sky; redesigned `.kc-scrollmap` into a frameless-at-rest Hanging Silk Handscroll Bookmark (`34px x 206px` `.kc-scrollmap__strip`, antique cedar dowel endcaps, integrated `14px` `#kc-flora-svg` spine, slim `#kc-alt-readout` badge, hover/focus `.kc-scrollmap__meta` drawer, and expanded desktop right padding `clamp(5.5rem, 8vw, 8rem)` on `.kc-civic-spread, .kc-sanctuary`).
  4. Synced canonical assets/HTML/JSON/reports to root via `scripts/sync_curriculum.py` (`Synced 15 districts and 19 lessons cleanly.`) and verified SHA256 parity across `index.html`, `data/curriculum.json`, `BRIEF.md`, `BUILD-REPORT.md`, `hero-plane-1-sky-peaks.webp`, `hero-plane-4-observatory.png`, `hero-plane-5-fore-canopy.png`, `01-observatory.mp4`, and `01-poster.webp`.
- **Files Touched:**
  - `f:\000_Ai Project\FlashGame\scripts\build_assets.py`
  - `f:\000_Ai Project\FlashGame\scripts\build_videos.py`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\index.html` & `f:\000_Ai Project\FlashGame\index.html`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BUILD-REPORT.md` & `f:\000_Ai Project\FlashGame\BUILD-REPORT.md`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\assets\*` & `f:\000_Ai Project\FlashGame\assets\*`
  - `f:\000_Ai Project\FlashGame\agent.md`
- **Verification Status:** `verify_scrollcraft.py` passed across all 4 viewports after final HTML/asset edits (`0` dead scroll, `2/2` scrub clips active whenever on screen, `7/7` cues reaching `>= 0.85`, lowest worst composited contrast `12.05:1`), plus visual inspection of all 4 contact sheets:
  - Desktop (`1440x900` — `scrollcraft/lab/shots/sheet.png` & `00.png`): `14.0` viewport-heights, `pan rail #1 overflow = 2285px` (`scrollWidth=3725px`).
  - Mobile (`390x844` — `scrollcraft/lab/mobile/sheet.png`): `16.5` viewport-heights, `pan rail #1 overflow = 2016px` (`scrollWidth=2406px`).
  - Compact (`360x640` — `scrollcraft/lab/compact/sheet.png`): `18.4` viewport-heights, `pan rail #1 overflow = 1878px` (`scrollWidth=2238px`).
  - Reduced Motion (`1440x900 --reduced-motion` — `scrollcraft/lab/reduced/sheet.png`): `14.0` viewport-heights, `pan rail #1 overflow = 2285px` (`scrollWidth=3725px`), static posters and instant cue visibility.
- **Constraints / Open Decisions:** Keep `scroll-craft/engine/scrollcraft.js` and `scrollcraft.css` untouched; always sync canonical `scrollcraft/builds/kindness-city/` changes to root (`index.html`, `data/curriculum.json`, `BRIEF.md`, `BUILD-REPORT.md`, `assets/*`); `node` is not on PATH so continue using `scripts/verify_scrollcraft.py`.
- **Next Recommended Steps:** Proceed to the next pending task in Section 6 (e.g., interactive lesson/branch detail modal or Python sandbox preview for `curriculum.json` entries).

### [2026-11-12 08:52] — Add Expandable 15-District City Atlas, Living Environmental Storytelling & Data-Driven 19-Lesson Curriculum (`curriculum.json`)
- **Request:** Make the scrollytelling experience unlock districts, animate nature growth & progressive chapter unlocking on scroll, include all 15 themed districts with Earth-care environmental storytelling (`Recycling Center`, `Tree Planting Area`, `Community Garden`, `Solar Panels`, `Wind Turbines`, `Clean River`, `Wildlife Habitat`, `Rainwater Harvesting`, `Bicycle Paths`, `Green Buildings`), and build an extensible data-driven JSON curriculum registry grouping Lessons 1–19 (`module/l1_pyprint` through `module/l19_ai_challenge`) into logical chapters.
- **Summary of Changes:**
  - Created [`scrollcraft/builds/kindness-city/data/curriculum.json`](file:///f:/000_Ai%20Project/FlashGame/scrollcraft/builds/kindness-city/data/curriculum.json) (mirrored to [`data/curriculum.json`](file:///f:/000_Ai%20Project/FlashGame/data/curriculum.json)) holding the expandable city vision, Three Loves metadata, all 15 districts with eco-infrastructure tags and scroll unlock thresholds, and 5 progressive chapters mapping all 19 lessons + exact git `module/*` branch names.
  - Built [`scripts/sync_curriculum.py`](file:///f:/000_Ai%20Project/FlashGame/scripts/sync_curriculum.py) to sync `curriculum.json` to root and keep the offline `<script id="kc-curriculum-fallback">` snapshot inside `index.html` identical while `fetch('data/curriculum.json')` loads live over HTTP.
  - Added progressive flora bloom (`#kc-flora-svg` botanical spine in `.kc-scrollmap` + growing `.kc-flora-divider` vine in Act 3 driven by `--kc-env-bloom`), eco stewardship pills on Act 2 pan cards (`.kc-rail__eco`), and the interactive `#kc-curriculum-sanctuary` District Atlas + 5-Chapter Lesson Roadmap with `All / 爱自己 / 爱别人 / 爱地球` filtering inside Act 3.
  - Added desktop `@media (min-width: 861px)` right-gutter clearance (`13rem..17rem`) for `.kc-civic-spread` & `.kc-sanctuary` so long branch names clear `.kc-scrollmap` completely, plus mobile/compact refinements for `360x640` Pan Rail cards.
- **Files Touched:**
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\data\curriculum.json` & `f:\000_Ai Project\FlashGame\data\curriculum.json`
  - `f:\000_Ai Project\FlashGame\scripts\sync_curriculum.py`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\index.html` & `f:\000_Ai Project\FlashGame\index.html`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BRIEF.md` & `f:\000_Ai Project\FlashGame\BRIEF.md`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BUILD-REPORT.md` & `f:\000_Ai Project\FlashGame\BUILD-REPORT.md`
  - `f:\000_Ai Project\FlashGame\agent.md`
- **Verification Status:**
  - `python scripts/sync_curriculum.py`: synced 15 districts and 19 lessons cleanly; canonical-to-root SHA256 hashes verified identical (`index.html`, `curriculum.json`, `BRIEF.md`, `BUILD-REPORT.md`).
  - All 4 passes of `scripts/verify_scrollcraft.py` completed cleanly AFTER final CSS/layout edits, with all contact sheets visually inspected:
    - Desktop (`1440x900` — `scrollcraft/lab/shots/sheet.png`): `14.2vh`, pan overflow `2285px`, `0` dead scroll, `2/2` scrub clips active, `7/7` cues `>= 0.85`, lowest worst contrast `12.05:1`.
    - Mobile (`390x844` — `scrollcraft/lab/mobile/sheet.png`): `16.4vh`, pan overflow `2016px`, `0` dead scroll, `2/2` scrub clips active, `7/7` cues `>= 0.85`, lowest worst contrast `12.05:1`.
    - Compact (`360x640` — `scrollcraft/lab/compact/sheet.png`): `18.3vh`, pan overflow `1878px`, `0` dead scroll, `2/2` scrub clips active, `7/7` cues `>= 0.85`, lowest worst contrast `12.05:1`.
    - Reduced Motion (`1440x900 --reduced-motion` — `scrollcraft/lab/reduced/sheet.png`): `14.2vh`, `0` dead scroll, `7/7` cues `>= 0.85`, all 15 districts & all 5 flora spine nodes bloomed immediately (`contrast >= 12.05:1`).
- **Constraints / Open Decisions:**
  - To add Lesson 20+, new Chapters, or new Districts in the future, edit ONLY `scrollcraft/builds/kindness-city/data/curriculum.json` and run `python scripts/sync_curriculum.py` — zero HTML or CSS redesign required.
  - Keep `.kc-civic-spread` and `.kc-sanctuary` desktop right padding (`min-width: 861px`) >= `13rem` so the persistent right-hand `.kc-scrollmap` rail never covers long module branch labels.
- **Next Recommended Steps:**
  - Add lesson launch links or per-lesson starter Python snippets inside `data/curriculum.json` (and expose them in `.kc-lesson-row` as a collapsible preview Drawer) when lessons move from roadmap planning to interactive code play.

### [2026-11-12 08:31] — Align Project Vision (`命好不如习惯好` / Three Loves) & Build 6 Non-Repeating Custom Illustrations
- **Request:** Align the site deeply with the Kindness City Project Vision (**命好不如习惯好**, technology as an enabler, every lesson teaching a Python concept + positive life habit across **Love Yourself `爱自己`**, **Love Others `爱别人`**, and **Love the Earth `爱地球`**) and expand custom illustrations so cards/panels do not repeat.
- **Summary of Changes:**
  - Generated 6 bespoke 16:9 illustrations via `image-generator` subagent (`terraced_nurseries_scene`, `loop_river_bend_scene`, `little_ci_kindness_scene`, `coding_academy_scene`, `recycling_pavilion_scene`, `front_gate_problem_solvers_scene`) with zero unintended text or shared crops.
  - Updated [`scripts/build_assets.py`](file:///f:/000_Ai%20Project/FlashGame/scripts/build_assets.py) and rebuilt [`assets/`](file:///f:/000_Ai%20Project/FlashGame/assets) so Act 2 has 5 unique `1200×900` (4:3) plates (`pan-01-waterwheel.webp`..`pan-05-solvers.webp`) and Act 3 has 2 unique `1440×960` (3:2) plates (`flow-coding-academy.webp`, `flow-recycling-pavilion.webp`).
  - Rewrote Act 1–5 copy, CSS (`aspect-ratio: 4 / 3` media framing, `.kc-hero-mid` upper-sky mask uncovering Plane 1 parallax peaks, `.kc-quest-strip` Python+Habit bar), Act 4 Three-Loves selector (`爱自己 · 爱别人 · 爱地球`), and PNG Citizen Seal export in [`scrollcraft/builds/kindness-city/index.html`](file:///f:/000_Ai%20Project/FlashGame/scrollcraft/builds/kindness-city/index.html) (and synced root [`index.html`](file:///f:/000_Ai%20Project/FlashGame/index.html)), [`BRIEF.md`](file:///f:/000_Ai%20Project/FlashGame/BRIEF.md), and [`BUILD-REPORT.md`](file:///f:/000_Ai%20Project/FlashGame/BUILD-REPORT.md).
- **Files Touched:**
  - `f:\000_Ai Project\FlashGame\scripts\build_assets.py`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\index.html` & `f:\000_Ai Project\FlashGame\index.html`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BRIEF.md` & `f:\000_Ai Project\FlashGame\BRIEF.md`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\BUILD-REPORT.md` & `f:\000_Ai Project\FlashGame\BUILD-REPORT.md`
  - `f:\000_Ai Project\FlashGame\scrollcraft\builds\kindness-city\assets\pan-01..05.webp`, `flow-coding-academy.webp`, `flow-recycling-pavilion.webp` (and root `assets\`)
  - `f:\000_Ai Project\FlashGame\agent.md`
- **Verification Status:**
  - All 4 passes of `scripts/verify_scrollcraft.py` completed and passed AFTER final `index.html` polish, with contact sheets visually inspected:
    - Desktop (`1440x900` — `scrollcraft/lab/shots/sheet.png`): `12.5vh`, pan overflow `2285px`, `0` dead scroll, `2/2` scrub clips active, `7/7` cues `>= 0.85`, lowest worst contrast `12.05:1`.
    - Mobile (`390x844` — `scrollcraft/lab/mobile/sheet.png`): `13.0vh`, pan overflow `2016px`, `0` dead scroll, `7/7` cues `>= 0.85`, lowest worst contrast `12.05:1`, zero Window 1/2 overlap.
    - Compact (`360x640` — `scrollcraft/lab/compact/sheet.png`): `13.6vh`, pan overflow `1878px`, `0` dead scroll, `7/7` cues `>= 0.85`, lowest worst contrast `12.05:1`.
    - Reduced Motion (`1440x900 --reduced-motion` — `scrollcraft/lab/reduced/sheet.png`): `12.5vh`, `0` dead scroll, `7/7` cues `>= 0.85`, posters clean (`contrast >= 12.05:1`).
- **Constraints / Open Decisions:**
  - Strictly avoid `node` calls unless Node.js is installed; continue using `scripts/build_assets.py`, `scripts/build_videos.py`, and `scripts/verify_scrollcraft.py`.
  - Keep Act 4 cue windows non-overlapping (`0 0.42 0 0.18` and `0.45 0.96 0.16 0.14`) so mobile cards never double-stack during fade transitions.
- **Next Recommended Steps:**
  - Explore **Section 6 (Backlog)**: e.g., an Interactive Lesson Explorer page or sub-page (`scrollcraft/builds/coding-academy`), interactive bilingual `EN / 中文` body toggle, or hotspot pins inside `#atlas-modal`.

### [2026-11-12 08:10] — Add Mandatory Task-Completion Handover Rule to `agent.md`
- **Request:** Add a handover rule in `agent.md` to be followed every time a task is completed.
- **Summary of Changes:**
  - Added the **Mandatory Rule: Task-Completion Handover Protocol** section near the top of `agent.md`, defining required sync, verification, ledger, handover-log, and final-reply steps upon every task completion.
  - Updated **Section 1** and **Section 5** in `agent.md` to include `BUILD-REPORT.md` in the root-mirror file list and PowerShell sync commands.
  - Added **Section 7 (Handover Log)** with a reusable template and recorded the current project handover baseline.
- **Files Touched:** `f:\000_Ai Project\FlashGame\agent.md`
- **Verification Status:**
  - Documentation-only edit in this session; no code, CSS, HTML, or asset files were modified, so `verify_scrollcraft.py` was not re-run.
  - Prior landing-page build baseline (`2026-11-11`): `mobile` (`390x844`) passed after the final `@media (max-width: 860px)` close-panel edit (`0` dead scroll, all `7` cues `>= 0.85`, lowest worst contrast `12.05:1`); `shots` (`1440x900`), `compact` (`360x640`), and `reduced` (`1440x900 --reduced-motion`) passed immediately prior (`shots` and `reduced` are unaffected by the `<= 860px` media query, while `compact` `360x640` should be re-run before publishing if post-final-edit confirmation on compact phones is needed).
- **Constraints / Open Decisions:**
  - `node` is not on the default system PATH; continue using `python scripts/build_assets.py`, `python scripts/build_videos.py`, and `python scripts/verify_scrollcraft.py` (uses Chrome + CDP + FFmpeg 9.0).
  - Never modify `scrollcraft.js` or `scrollcraft.css`; keep canonical build files in `scrollcraft/builds/kindness-city/` synchronized with the workspace root.
- **Next Recommended Steps:**
  - If resuming frontend/QA work on `kindness-city`, run `python "f:\000_Ai Project\FlashGame\scripts\verify_scrollcraft.py" --out "f:\000_Ai Project\FlashGame\scrollcraft\lab\compact" --width 360 --height 640` to confirm the final `@media (max-width: 860px)` close-panel layout on compact phones, or pick up any item from **Section 6 (Backlog)**.
