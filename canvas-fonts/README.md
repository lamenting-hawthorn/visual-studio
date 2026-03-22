# Canvas Fonts

Place custom fonts here for use with canvas design outputs.

## Recommended Fonts
- **Poppins** (headings) — [Google Fonts](https://fonts.google.com/specimen/Poppins)
- **Lora** (body text) — [Google Fonts](https://fonts.google.com/specimen/Lora)
- **Inter** — [Google Fonts](https://fonts.google.com/specimen/Inter)

## Usage
Fonts in this directory can be loaded via PIL/Pillow:

```python
from PIL import ImageFont
font = ImageFont.truetype("canvas-fonts/Poppins-Regular.ttf", size=24)
```

Download `.ttf` files from Google Fonts and place them here.
