# Icon Inventory & Design System

Every visual cue in this repository's README comes from the single icon family
below. There are no emoji anywhere in the documentation — the previous emoji
section marks were replaced 1:1 by these inline SVG line marks.

## The family rules

All icons share one construction and one palette:

| Property | Value |
|---|---|
| Grid | 24 × 24 units, drawn on a centered 12,12 axis |
| Stroke | 2 units, constant weight across the whole family |
| Caps & joins | Round (`stroke-linecap="round"`, `stroke-linejoin="round"`) |
| Fills | None — stroke-only marks; the only fills are terminal dots |
| Corner radius | Rounded terminals throughout; rectangular sub-shapes use `rx="1"` |
| Color (dark theme) | `#8f6024` — the gold accent extracted from `docs/assets/banner.png` |
| Color (light theme) | `#7a5522` — the same hue deepened for cream backgrounds |
| Variants | Every icon ships twice: `icons/<name>.svg` (gold on dark) and `icons/<name>-light.svg` (deep gold on light) |

The palette is the banner's: ink field `#191310` → `#0d0b08`, cream text
`#e0e0d0`, gold accent `#8f6024`. The icons extend the banner's serif
"illuminated manuscript meets terminal" identity down the page instead of
restarting the design at section one.

## The inventory

### Section marks

| Icon | File | Used in | Encodes |
|---|---|---|---|
| Bolt | `docs/assets/icons/bolt.svg` | 01 · Overview | The enforcement firing on its own |
| Shield | `docs/assets/icons/shield.svg` | 02 · Security | The empty, defensive room |
| Scroll | `docs/assets/icons/scroll.svg` | 03 · Background | The two failure patterns, documented |
| Package | `docs/assets/icons/package.svg` | 04 · Install | The portable bundle |
| Pointer | `docs/assets/icons/pointer.svg` | 05 · Usage | The one door the user pulls |
| Grid | `docs/assets/icons/grid.svg` | 06 · Components | The nine components |
| Columns | `docs/assets/icons/columns.svg` | 07 · Philosophy | The first principle, held up |
| Eye | `docs/assets/icons/eye.svg` | 08 · Colophon | The document watching itself |

### Skill marks (used in headings, tables, and the system map)

| Icon | File | Encodes |
|---|---|---|
| Law (scales) | `docs/assets/icons/law.svg` | `form-is-function` — the law |
| Guard (shield-check) | `docs/assets/icons/guard.svg` | `reasoning-execution-design-coherence` — the build guard; also marks verified-install rows |
| Eye | `docs/assets/icons/eye.svg` | `spatial-audit` — the detector |
| Hammer | `docs/assets/icons/hammer.svg` | `fix-my-design` — the rebuild procedure |
| Flame | `docs/assets/icons/flame.svg` | `interrogator` — the pressure |

### Utility marks

| Icon | File | Encodes |
|---|---|---|
| Grid | `docs/assets/icons/grid.svg` | Reused as the components mark |
| Eye | `docs/assets/icons/eye.svg` | Reused as the colophon / detector mark |

Two marks do double duty (`eye`, `grid`) — detector and colophon are both acts
of looking; components and the audit grid are both acts of structure.

## The section ground (the one background texture)

Backgrounds in this README are not flat. The texture chosen for every chapter
is the **ruled-manuscript ground** — the page as an illuminated-manuscript
sheet ruled for writing. It is rendered once as a specimen at
`docs/assets/section-bg.svg` (dark) and `docs/assets/section-bg-light.svg`
(light), and its construction is:

```css
/* The ground, as CSS — layers bottom to top:
   1. ink field with candle-glow   2. ruled baselines every 28px
   3. drop-cap grid (120px squares with inner crosses, faint)
   4. thin gold chapter frame                                       */

.section-ground {
  background-color: #191310;
  background-image:
    /* drop-cap squares: 120px module, outlined with an inner cross */
    repeating-linear-gradient(0deg,  transparent 0 119px, rgba(74,58,30,.55) 119px 120px),
    repeating-linear-gradient(90deg, transparent 0 119px, rgba(74,58,30,.55) 119px 120px),
    /* ruled baselines */
    repeating-linear-gradient(0deg,  transparent 0 27px,  rgba(42,33,24,.9)  27px 28px),
    /* candle glow */
    radial-gradient(120% 90% at 50% 38%, #241c13 0%, #191310 55%, #0d0b08 100%);
  box-shadow: inset 0 0 0 1.5px rgba(143,96,36,.85);
}
```

```svg
<!-- The same ground as the shipped SVG pattern unit (viewBox 0 0 1200 360):
     <radialGradient id="glow" cx="50%" cy="38%" r="72%">
       <stop offset="0%" stop-color="#241c13"/>
       <stop offset="55%" stop-color="#191310"/>
       <stop offset="100%" stop-color="#0d0b08"/>
     </radialGradient>
     <rect width="1200" height="360" fill="url(#glow)"/>
     <!-- ruled baselines, every 28 units -->
     <line x1="0" y1="56" x2="1200" y2="56" stroke="#2a2118" stroke-width="1"/>
     <!-- drop-cap square with inner cross (module 120, at any grid point x,y) -->
     <rect x="40" y="40" width="120" height="120" fill="none"
           stroke="#4a3a1e" stroke-width="1.2"/>
     <line x1="100" y1="86" x2="100" y2="114" stroke="#241a0e" stroke-width="1"/>
     <line x1="86" y1="100" x2="114" y2="100" stroke="#241a0e" stroke-width="1"/>
     <!-- thin gold chapter frame -->
     <rect x="12" y="12" width="1176" height="336" fill="none"
           stroke="#8f6024" stroke-width="1.5" opacity="0.85"/> -->
```

The light variant maps the roles, not the hexes: field → warm paper cream
`#f8f5ec`, rules → `#e6e0d2`, drop-cap strokes → `#d9cfb4`, text → warm ink
`#241f12`, frame stays gold.

## Other page furniture

| Asset | Files | Use |
|---|---|---|
| Ornament divider | `docs/assets/divider.svg`, `-light.svg` | Fading gold rules, diamond-and-dot terminals — one between every pair of chapters |
| System map | `docs/assets/system-map.svg`, `-light.svg` | The law → build guard → detector → procedure → interrogator diagram, EB Garamond set as paths |
| Banner | `docs/assets/banner.png` | The brand anchor every element above extends |
