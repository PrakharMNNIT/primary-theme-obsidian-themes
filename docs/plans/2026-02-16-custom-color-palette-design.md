# Custom Color Palette for Primary Obsidian Theme

## Date: 2026-02-16

## Architecture Analysis

### How Colors Work in Primary

Primary uses a **single palette file** as the sole source of all color definitions:

```
src/scss/10_foundations/palettes/_classic-original.scss
```

This file is imported by `src/scss/index.scss`, and ALL 40+ component/window/editor SCSS files reference CSS custom properties (variables) — never the palette directly.

### Palette File Structure

The palette file has 3 sections:

| Section | Scope | Purpose |
|---------|-------|---------|
| `body { }` | Both modes | Non-color variables (sizing, spacing, fonts, animations) |
| `.theme-light { }` | Light mode | All light mode color definitions + derived variables |
| `.theme-dark { }` | Dark mode | All dark mode color definitions + derived variables |

### Color Primitive System

Each mode defines color primitives in HSL:

| Category | Variables | Role |
|----------|-----------|------|
| **Grayscale** | 14 steps (gray-10→140) | Surface backgrounds, text, borders, icons |
| **Red** | 4 shades (10→40) + alpha | Bold text, errors, folder colors |
| **Orange** | 4 shades + alpha | Warnings, in-progress states |
| **Yellow** | 4 shades + alpha | Internal links, highlights |
| **Green** | 4 shades + alpha | Checkboxes, external links, success |
| **Blue** | 4 shades + alpha | Italic text, tags, loading |
| **Purple** | 4 shades + alpha | Folder 6, graph nodes |
| **Accent** | H/S/L values | Interactive elements |
| **Special RGB** | 9 named colors | Canvas, graph, special UI |

**Total: ~80 primitive color variables per mode (~160 total)**

### Why Swapping Is Safe

1. All 40+ component files use CSS custom property NAMES, not values
2. Shadows use mode-independent `rgba(0,0,0)` / `rgba(255,255,255)`
3. `color-mix()` functions auto-adapt to new base colors
4. Variable names are the CONTRACT — values are the implementation

---

## Implementation Plan

### Step 1: Copy Palette File
```
cp src/scss/10_foundations/palettes/_classic-original.scss \
   src/scss/10_foundations/palettes/_custom.scss
```

### Step 2: Modify Only Color Values
In `_custom.scss`, change ONLY the `hsla()` and `rgb()` values.
Keep all variable NAMES, all non-color variables, all structural code identical.

### Step 3: Swap Import
In `src/scss/index.scss`:
```scss
// Before:
@use '10_foundations/palettes/classic-original';

// After:
@use '10_foundations/palettes/custom';
```

### Step 4: Build
```bash
npx grunt
```

### Grayscale Contrast Requirements

The 14-step grayscale MUST maintain proper contrast progression:

**Light Mode:**
- gray-10: ~98% lightness (lightest surface)
- gray-140: ~17% lightness (darkest text)
- Minimum 4.5:1 contrast for text on backgrounds

**Dark Mode:**
- gray-10: ~85% lightness (lightest text)
- gray-140: ~9% lightness (darkest surface)
- Same contrast requirements apply

### Semantic Color Guidelines

- **Shade 10**: Lightest/softest variant (hover states, backgrounds)
- **Shade 20**: Standard variant (default state)
- **Shade 30**: Strong variant (text on light/dark backgrounds)
- **Shade 40**: Darkest/most saturated (high contrast needs)
- **Alpha**: 20% opacity version for highlights/selections

---

## Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Breaking component styles | ZERO | Variables are contracts, only values change |
| Breaking shadows/effects | ZERO | Shadows use mode-independent rgba |
| Poor contrast/readability | MEDIUM | Must maintain grayscale progression |
| Color clashing | MEDIUM | Need cohesive palette design |
| Build failure | ZERO | Same file structure, just different values |

---

---

## Suggested Palette Directions (from UI/UX Pro Max analysis)

### Option A: 🌊 "Slate Ocean" — Cool & Modern
| Role | Light Mode | Dark Mode |
|------|-----------|-----------|
| Base gray hue | ~210-220 (slate blue) | ~215-225 (deep slate) |
| Background | #F8FAFC / #FAFAFA | #0F172A / #1E293B |
| Text | #020617 / #0F172A | #F8FAFC / #E2E8F0 |
| Bold (Red→Rose) | #E11D48 | #FB7185 |
| Italic (Blue→Cyan) | #0369A1 | #22D3EE |
| Links (Yellow→Amber) | #D97706 | #FBBF24 |
| External (Green→Emerald) | #059669 | #34D399 |
| Tags (Blue→Indigo) | #4F46E5 | #818CF8 |
| Mood: Clean, professional, Notion-like. WCAG AAA. |

### Option B: 🌸 "Rosé Stone" — Warm Elegant
| Role | Light Mode | Dark Mode |
|------|-----------|-----------|
| Base gray hue | ~350-10 (warm pink-stone) | ~340-355 (deep rose-stone) |
| Background | #FDF2F8 / #FFF1F2 | #1C1017 / #2A1520 |
| Text | #831843 / #881337 | #FDF2F8 / #FECDD3 |
| Bold (Red→Pink) | #DB2777 | #F472B6 |
| Italic (Blue→Mauve) | #7C3AED | #A78BFA |
| Links (Yellow→Gold) | #CA8A04 | #FBBF24 |
| External (Green→Sage) | #059669 | #6EE7B7 |
| Tags (Blue→Violet) | #6D28D9 | #C4B5FD |
| Mood: Editorial, refined, magazine-like. Romantic warmth. |

### Option C: 🌲 "Evergreen" — Nature & Earth
| Role | Light Mode | Dark Mode |
|------|-----------|-----------|
| Base gray hue | ~140-150 (muted sage) | ~150-160 (deep forest) |
| Background | #F0FDF4 / #ECFDF5 | #0A1F13 / #14261D |
| Text | #14532D / #064E3B | #ECFDF5 / #D1FAE5 |
| Bold (Red→Terracotta) | #C2410C | #FB923C |
| Italic (Blue→Teal) | #0D9488 | #5EEAD4 |
| Links (Yellow→Amber) | #B45309 | #FCD34D |
| External (Green→Leaf) | #15803D | #4ADE80 |
| Tags (Blue→Pine) | #0F766E | #99F6E4 |
| Mood: Grounding, natural, cabin-in-the-woods. Gruvbox-adjacent. |

### Option D: 🌙 "Midnight Neon" — Deep & Vivid
| Role | Light Mode | Dark Mode |
|------|-----------|-----------|
| Base gray hue | ~230-240 (cool indigo) | ~235-245 (near-black indigo) |
| Background | #EFF6FF / #F8FAFC | #0F0F23 / #1E1B4B |
| Text | #1E3A8A / #1E40AF | #F8FAFC / #E2E8F0 |
| Bold (Red→Crimson) | #DC2626 | #F87171 |
| Italic (Blue→Electric) | #2563EB | #60A5FA |
| Links (Yellow→Orange) | #EA580C | #F97316 |
| External (Green→Neon) | #16A34A | #4ADE80 |
| Tags (Blue→Violet) | #7C3AED | #A78BFA |
| Mood: Dev-focused, VS Code-inspired, high contrast. |

---

## How Each Option Maps to Primary's Variable System

The palette swap only touches these sections in the new `_custom.scss` file:

```
.theme-light / .theme-dark {
  /* CHANGE THESE ↓ */
  --color-{l|d}-gray-10 through 140     (14 vars × 2 modes = 28)
  --color-{l|d}-red-10 through 40       (4 vars × 2 = 8)
  --color-{l|d}-orange-10 through 40    (4 × 2 = 8)
  --color-{l|d}-yellow-10 through 40    (4 × 2 = 8)
  --color-{l|d}-green-10 through 40     (4 × 2 = 8)
  --color-{l|d}-blue-10 through 40      (4 × 2 = 8)
  --color-{l|d}-purple-10 through 40    (4 × 2 = 8)
  --color-{l|d}-alpha-*                 (7 × 2 = 14)
  --accent-h, --accent-s, --accent-l   (3 × 2 = 6)
  --color-*-rgb + --color-*             (18 × 2 = 36)

  /* DON'T TOUCH THESE ↓ */
  Everything else: backgrounds, text, icons, etc. are DERIVED
  from the primitives above via var() references.
}
```

Total changes: ~160 HSL/RGB values. Zero structural changes.

---

## Next Step

**Pick a direction (A/B/C/D or describe your own) and I'll generate the complete palette file, swap the import, and build the theme.**
