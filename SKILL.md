---
name: threetone-visual-studio
description: Unified toolkit for creating animated GIFs (Slack-optimized), algorithmic generative art (p5.js), and static canvas designs (.pdf/.png) — all styled with Anthropic brand guidelines. Use when users request GIFs, generative art, visual designs, posters, or branded visual content.
license: Complete terms in LICENSE.txt
---

# Threetone Visual Studio

A unified visual creation toolkit combining **Slack GIF creation**, **algorithmic generative art**, **canvas design**, and **brand guidelines** into one integrated skill.

---

## §1 — Brand Guidelines

### Colors

**Main Colors:**
- Dark: `#141413` — Primary text and dark backgrounds
- Light: `#faf9f5` — Light backgrounds and text on dark
- Mid Gray: `#b0aea5` — Secondary elements
- Light Gray: `#e8e6dc` — Subtle backgrounds

**Accent Colors:**
- Orange: `#d97757` — Primary accent
- Blue: `#6a9bcc` — Secondary accent
- Green: `#788c5d` — Tertiary accent

### Typography
- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- Fonts available via Google Fonts CDN or local install in `canvas-fonts/`

### Application Rules
- Headings (24pt+): Poppins font
- Body text: Lora font
- Non-text shapes use accent colors (cycle through orange → blue → green)
- Smart color selection based on background contrast
- Maintains visual interest while staying on-brand

---

## §2 — Slack GIF Creator

A toolkit for creating animated GIFs optimized for Slack.

### Slack Requirements

**Dimensions:**
- Emoji GIFs: 128×128 (recommended)
- Message GIFs: 480×480

**Parameters:**
- FPS: 10–30 (lower = smaller file size)
- Colors: 48–128 (fewer = smaller file size)
- Duration: Keep under 3 seconds for emoji GIFs

### Core Workflow

```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

# 1. Create builder
builder = GIFBuilder(width=128, height=128, fps=10)

# 2. Generate frames
for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)

    # Draw your animation using PIL primitives
    # (circles, polygons, lines, etc.)

    builder.add_frame(frame)

# 3. Save with optimization
builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

### Drawing Graphics

#### Working with User-Uploaded Images
If a user uploads an image, consider whether they want to:
- **Use it directly** (e.g., "animate this", "split this into frames")
- **Use it as inspiration** (e.g., "make something like this")

```python
from PIL import Image
uploaded = Image.open('file.png')
# Use directly, or just as reference for colors/style
```

#### Drawing from Scratch
Use PIL ImageDraw primitives:

```python
from PIL import ImageDraw

draw = ImageDraw.Draw(frame)

# Circles/ovals
draw.ellipse([x1, y1, x2, y2], fill=(r, g, b), outline=(r, g, b), width=3)

# Stars, triangles, any polygon
points = [(x1, y1), (x2, y2), (x3, y3), ...]
draw.polygon(points, fill=(r, g, b), outline=(r, g, b), width=3)

# Lines
draw.line([(x1, y1), (x2, y2)], fill=(r, g, b), width=5)

# Rectangles
draw.rectangle([x1, y1, x2, y2], fill=(r, g, b), outline=(r, g, b), width=3)
```

**Don't use:** Emoji fonts (unreliable across platforms) or assume pre-packaged graphics exist in this skill.

#### Making Graphics Look Good

Graphics should look polished and creative, not basic:

**Use thicker lines** — Always set `width=2` or higher. Thin lines (width=1) look choppy.

**Add visual depth**:
- Use gradients for backgrounds (`create_gradient_background`)
- Layer multiple shapes for complexity

**Make shapes more interesting**:
- Add highlights, rings, or patterns to circles
- Stars can have glows (draw larger, semi-transparent versions behind)
- Combine multiple shapes (stars + sparkles, circles + rings)

**Pay attention to colors**:
- Use vibrant, complementary colors
- Add contrast (dark outlines on light shapes, light outlines on dark shapes)

**For complex shapes** (hearts, snowflakes, etc.):
- Use combinations of polygons and ellipses
- Calculate points carefully for symmetry
- Add details (highlights, intricate branches)

### Available Utilities

#### GIFBuilder (`core.gif_builder`)
```python
builder = GIFBuilder(width=128, height=128, fps=10)
builder.add_frame(frame)       # Add PIL Image
builder.add_frames(frames)     # Add list of frames
builder.save('out.gif', num_colors=48, optimize_for_emoji=True, remove_duplicates=True)
```

#### Validators (`core.validators`)
```python
from core.validators import validate_gif, is_slack_ready

passes, info = validate_gif('my.gif', is_emoji=True, verbose=True)
if is_slack_ready('my.gif'):
    print("Ready!")
```

#### Easing Functions (`core.easing`)
```python
from core.easing import interpolate

t = i / (num_frames - 1)  # Progress 0.0 to 1.0
y = interpolate(start=0, end=400, t=t, easing='ease_out')

# Available: linear, ease_in, ease_out, ease_in_out,
#           bounce_out, elastic_out, back_out, anticipate, overshoot
```

#### Frame Helpers (`core.frame_composer`)
```python
from core.frame_composer import (
    create_blank_frame,          # Solid color background
    create_gradient_background,  # Vertical gradient
    draw_circle,                 # Helper for circles
    draw_text,                   # Simple text rendering
    draw_star                    # 5-pointed star
)
```

### Animation Concepts

**Shake/Vibrate** — Offset object position with `math.sin()`/`math.cos()` + small random variations.

**Pulse/Heartbeat** — Scale size rhythmically with `math.sin(t * freq * 2 * math.pi)`. Scale between 0.8–1.2 of base.

**Bounce** — Use `interpolate()` with `easing='bounce_out'` for landing, `easing='ease_in'` for falling.

**Spin/Rotate** — `image.rotate(angle, resample=Image.BICUBIC)`. For wobble: sine wave for angle.

**Fade In/Out** — Create RGBA image, adjust alpha. Or `Image.blend(img1, img2, alpha)`.

**Slide** — Move from off-screen using `interpolate()` with `easing='ease_out'`. For overshoot: `'back_out'`.

**Zoom** — Scale from 0.1→2.0 and crop center. Can add motion blur.

**Explode/Particle Burst** — Generate particles with random angles/velocities. Add gravity: `vy += g`. Fade alpha over time.

### Optimization (only when asked)
1. Fewer frames — Lower FPS or shorter duration
2. Fewer colors — `num_colors=48`
3. Smaller dimensions — 128×128
4. Remove duplicates — `remove_duplicates=True`
5. Emoji mode — `optimize_for_emoji=True`

```python
builder.save('emoji.gif', num_colors=48, optimize_for_emoji=True, remove_duplicates=True)
```

### Dependencies
```bash
pip install pillow imageio numpy
```

---

## §3 — Algorithmic Art (p5.js)

Create algorithmic art expressed as interactive p5.js generative sketches. This happens in two steps:
1. **Algorithmic Philosophy Creation** (.md file)
2. **Expression through code** (.html + inline .js)

### Step 1: Algorithmic Philosophy Creation

Create an ALGORITHMIC PHILOSOPHY (not static images) interpreted through:
- Computational processes, emergent behavior, mathematical beauty
- Seeded randomness, noise fields, organic systems
- Particles, flows, fields, forces
- Parametric variation and controlled chaos

**Name the movement** (1–2 words): e.g. "Organic Turbulence" / "Quantum Harmonics"

**Articulate the philosophy** (4–6 paragraphs), expressing how it manifests through:
- Computational processes and mathematical relationships
- Noise functions and randomness patterns
- Particle behaviors and field dynamics
- Temporal evolution and system states
- Parametric variation and emergent complexity

**Critical guidelines:**
- Avoid redundancy — each algorithmic aspect mentioned once
- Emphasize craftsmanship REPEATEDLY — "meticulously crafted," "product of deep expertise," "painstaking optimization," "master-level implementation"
- Leave creative space for implementation choices

**Philosophy examples:**
- **"Organic Turbulence"** — Flow fields driven by layered Perlin noise. Thousands of particles following vector forces, trails accumulating into density maps.
- **"Quantum Harmonics"** — Particles on a grid with phase values that interfere. Constructive = bright nodes, destructive = voids.
- **"Recursive Whispers"** — Branching structures subdividing recursively with golden ratios. L-systems with noise perturbation.
- **"Field Dynamics"** — Invisible vector fields made visible through particle traces.
- **"Stochastic Crystallization"** — Random processes crystallizing through relaxation algorithms into ordered Voronoi structures.

Output as a .md file.

### Step 2: Deduce the Conceptual Seed

Before implementing, identify the subtle conceptual thread from the original request. The reference must be refined so it enhances depth without announcing itself — like a jazz musician quoting another song through algorithmic harmony.

### Step 3: p5.js Implementation

**⚠️ STEP 0: READ THE TEMPLATE FIRST**

1. **Read** `templates/viewer.html`
2. **Study** the exact structure, styling, and Anthropic branding
3. **Use it as the LITERAL STARTING POINT**
4. **Keep all FIXED sections** (header, sidebar structure, colors/fonts, seed controls, action buttons)
5. **Replace only VARIABLE sections** (algorithm, parameters, UI controls)

**Avoid:**
- ❌ Creating HTML from scratch
- ❌ Inventing custom styling or color schemes
- ❌ Using system fonts or dark themes

**Follow:**
- ✅ Copy the template's exact HTML structure
- ✅ Keep Anthropic branding (Poppins/Lora fonts, light colors, gradient backdrop)
- ✅ Maintain sidebar layout (Seed → Parameters → Colors? → Actions)
- ✅ Replace only the p5.js algorithm and parameter controls

#### Technical Requirements

**Seeded Randomness (Art Blocks Pattern):**
```javascript
let seed = 12345;
randomSeed(seed);
noiseSeed(seed);
```

**Parameter Structure:**
```javascript
let params = {
    seed: 12345,
    // Add parameters that control YOUR algorithm:
    // Quantities, scales, probabilities, ratios, angles, thresholds
};
```

**Canvas Setup:**
```javascript
function setup() {
    createCanvas(1200, 1200);
}
function draw() {
    // Your generative algorithm
}
```

#### Craftsmanship Requirements
- **Balance**: Complexity without visual noise, order without rigidity
- **Color Harmony**: Thoughtful palettes, not random RGB
- **Composition**: Visual hierarchy even in randomness
- **Performance**: Smooth, optimized for real-time
- **Reproducibility**: Same seed → identical output

#### What's Fixed vs Variable in the Template

**FIXED (always keep):**
- Layout structure (header, sidebar, main canvas area)
- Anthropic branding (UI colors, fonts, gradients)
- Seed section (display, prev/next, random, jump)
- Actions section (regenerate, reset, download)

**VARIABLE (customize per artwork):**
- The p5.js algorithm (setup/draw/classes)
- The `params` object
- Parameters section in sidebar (number, names, ranges)
- Colors section (optional — include if art needs adjustable colors)

#### Required Features
1. **Parameter Controls** — Sliders/color pickers with real-time updates
2. **Seed Navigation** — Display, prev/next, random, jump to specific seed
3. **Self-Contained** — Single HTML artifact, no external files except p5.js CDN
4. **Actions** — Regenerate, reset, download PNG

#### Output
1. **Algorithmic Philosophy** — .md file
2. **Single HTML Artifact** — Self-contained interactive generative art built from `templates/viewer.html`

Also see: `templates/generator_template.js` for p5.js code structure best practices.

---

## §4 — Canvas Design

Create museum-quality static visual art as .pdf or .png files.

### Step 1: Design Philosophy Creation

Create a VISUAL PHILOSOPHY interpreted through:
- Form, space, color, composition
- Images, graphics, shapes, patterns
- Minimal text as visual accent

**Name the movement** (1–2 words): e.g. "Brutalist Joy" / "Chromatic Silence"

**Articulate the philosophy** (4–6 paragraphs), expressing through:
- Space and form
- Color and material
- Scale and rhythm
- Composition and balance
- Visual hierarchy

**Critical guidelines:**
- Avoid redundancy
- Emphasize craftsmanship REPEATEDLY — "meticulously crafted," "product of deep expertise," "painstaking attention," "master-level execution"
- Leave creative space

**Philosophy examples:**
- **"Concrete Poetry"** — Communication through monumental form and bold geometry. Massive color blocks, sculptural typography. Polish poster energy meets Le Corbusier.
- **"Chromatic Language"** — Color as primary information system. Geometric precision with color zones creating meaning.
- **"Analog Meditation"** — Quiet visual contemplation through texture and breathing room. Paper grain, ink bleeds, vast negative space.
- **"Organic Systems"** — Natural clustering, modular growth patterns. Information through visual diagrams.
- **"Geometric Silence"** — Pure order and restraint. Grid-based precision, dramatic negative space.

Output as .md file.

### Step 2: Deduce the Subtle Reference

Identify the conceptual thread from the original request — a niche reference embedded within the art itself, not literal, always sophisticated. The philosophy provides the aesthetic language; the deduced topic provides the soul.

### Step 3: Canvas Creation

Create museum or magazine quality work using the design philosophy as foundation.

**Core principles:**
- Create one single page, highly visual, design-forward output (unless asked for more)
- Use repeating patterns and perfect shapes
- Treat the design as if it were a scientific bible — dense accumulation of marks, repeated elements, layered patterns
- Add sparse, clinical typography and systematic reference markers
- Anchor with simple phrase(s) positioned subtly
- Limited, intentional color palette
- Embrace the paradox of analytical visual language expressing human experience

**Text rules:**
- Text is always minimal and visual-first
- Context guides text scale (punk poster vs minimalist ceramics)
- Most font should be thin
- All use of fonts must be design-forward
- Nothing falls off the page — every element within canvas boundaries with proper margins
- Every element has breathing room and clear separation
- Use fonts from `./canvas-fonts` directory
- Make typography part of the art itself

**CRITICAL**: Create work that looks like it took countless hours. Composition, spacing, color choices, typography — everything screams expert-level craftsmanship.

**Output**: Single .pdf or .png file alongside the design philosophy .md file.

### Final Refinement Step

After initial creation, take a second pass:
- Refine what exists rather than adding more
- Make existing composition more cohesive
- Don't add fun filters — ask "How can I make what's already here more of a piece of art?"
- Polish to museum-display quality

### Multi-Page Option

When requested:
- Create more pages along the same design philosophy but distinctly different
- Bundle in same .pdf or multiple .pngs
- First page is just one page in a coffee table book
- Have pages tell a story tastefully
- Exercise full creative freedom

---

## §5 — Cross-Cutting Integration

These sections work together:

### Brand in GIFs
Apply Anthropic accent colors (orange `#d97757`, blue `#6a9bcc`, green `#788c5d`) as default palettes in GIF animations. Use `#faf9f5` as the default background.

### Brand in Algorithmic Art
The `templates/viewer.html` already uses Anthropic branding for the UI shell. Art colors within the canvas can be anything — the brand applies to the viewer, not the generative output.

### Brand in Canvas Design
Use Poppins for headings, Lora for body text. Apply brand accent colors for non-text elements.

### GIF from Art
Generate p5.js art, then capture frames to create GIFs:
```python
# After generating art frames from p5.js or PIL
builder = GIFBuilder(width=480, height=480, fps=15)
for frame in art_frames:
    builder.add_frame(frame)
builder.save('art-animation.gif', num_colors=128)
```

### Philosophy
This skill provides:
- **Knowledge**: Slack requirements, animation concepts, design philosophy methodology
- **Utilities**: GIFBuilder, validators, easing functions, frame helpers
- **Templates**: Anthropic-branded p5.js viewer, code structure reference
- **Flexibility**: Create the animation/art logic using PIL primitives or p5.js

It does NOT provide:
- Rigid templates or pre-made animation functions
- Emoji font rendering (unreliable)
- A library of pre-packaged graphics

**Note on user uploads**: This skill doesn't include pre-built graphics, but if a user uploads an image, use PIL to load and work with it.

Be creative! Combine concepts and use the full capabilities of PIL and p5.js.

---

## Resources

| Resource | Path | Purpose |
|----------|------|---------|
| Viewer Template | `templates/viewer.html` | **REQUIRED** starting point for p5.js artifacts |
| JS Best Practices | `templates/generator_template.js` | Code structure reference |
| GIF Builder | `core/gif_builder.py` | Frame assembly & optimization |
| Validators | `core/validators.py` | Slack GIF validation |
| Easing | `core/easing.py` | Animation timing functions |
| Frame Composer | `core/frame_composer.py` | PIL drawing helpers |
| Fonts | `canvas-fonts/` | Custom fonts for canvas designs |
| Dependencies | `requirements.txt` | Python package requirements |
