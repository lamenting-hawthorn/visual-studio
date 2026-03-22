# \ Visual Studio 🎨

> **The ultimate visual skill for Antigravity AI.** A unified toolkit for creating Slack-optimized animated GIFs, algorithmic generative art (p5.js), and museum-quality static canvas designs, all styled with Anthropic/Threetone brand guidelines.

## 🌟 Features

- **Slack GIF Creator**: Programmatically generate and assemble optimized animated GIFs using PIL and ImageIO. Includes built-in Slack validation (dimensions, sizes, frames).
- **Algorithmic Art**: A workflow and p5.js template for generating interactive, seed-based generative art, bundled as self-contained HTML artifacts.
- **Canvas Design**: A methodology for creating sophisticated, abstract, and minimalist `.png` or `.pdf` designs using programmatic drawing.
- **Brand Guidelines**: Enforced styling rules (Anthropic/Threetone colors: Orange `#d97757`, Blue `#6a9bcc`, Green `#788c5d`) and typography (Poppins, Lora) across all visual outputs.
- **Advanced Animation Engine**: 15+ easing functions (bounce, elastic, back, etc.), squash and stretch mechanics, and arc motion calculations built-in.

## 📦 Installation

To use this skill with Antigravity:

1. Clone this repository into your Antigravity skills directory:
   ```bash
   git clone https://github.com/lamenting-hawthorn/threetone-visual-studio.git ~/.gemini/skills/threetone-visual-studio
   ```
2. Install the required Python dependencies:
   ```bash
   pip install -r ~/.gemini/skills/threetone-visual-studio/requirements.txt
   ```
3. (Optional) Add your `.ttf` font files to the `canvas-fonts/` directory if you want to use custom typography in Canvas workflows.

## 🏗️ Directory Structure

``` text
threetone-visual-studio/
├── SKILL.md                    # Core Antigravity instructions and philosophy
├── requirements.txt            # Python dependencies (pillow, imageio, numpy)
├── core/                       # Python utilities
│   ├── gif_builder.py          # GIF assembly, color optimization, deduplication
│   ├── validators.py           # Validating Slack constraints for Emoji / Messages
│   ├── easing.py               # 15+ easing curves, interpolation, squash/stretch
│   └── frame_composer.py       # PIL utilities for shapes, backgrounds, typography
├── templates/                  # Frontend templates
│   ├── viewer.html             # Anthropic-branded layout for interactive p5.js art
│   └── generator_template.js   # Best-practices structure for p5.js seeded randoms
└── canvas-fonts/               # Drop custom .ttf files here for PDF/PNG rendering
```

## 🚀 Usage with Antigravity

Once installed, simply ask your Antigravity agent to create visuals. The agent will automatically recognize the tools and philosophies in `SKILL.md`.

**Example Prompts:**
- *"Make me a looping Slack emoji GIF of a bouncing orange star that squashes when it hits the ground."*
- *"Create an interactive piece of algorithmic art that explores the concept of 'Organic Turbulence' using flow fields. Make it a standalone HTML file."*
- *"Design a museum-quality minimalist poster honoring 'Geometric Silence' using our brand colors."*

## 📝 License

See the `LICENSE.txt` file for full copyright terms.
