"""
Threetone Visual Studio - Core utilities for GIF creation, animation, and visual design.

Modules can be imported individually:
    from core.gif_builder import GIFBuilder
    from core.validators import validate_gif, is_slack_ready
    from core.easing import interpolate, get_easing
    from core.frame_composer import (
        create_blank_frame, create_gradient_background,
        draw_circle, draw_star, draw_text
    )

Dependencies (install via: pip install -r requirements.txt):
    - pillow (required for all modules)
    - imageio, numpy (required for gif_builder)
"""

# Easing — no external dependencies
from core.easing import interpolate, get_easing, EASING_FUNCTIONS

# Frame composer — requires pillow
try:
    from core.frame_composer import (
        create_blank_frame,
        create_gradient_background,
        draw_circle,
        draw_star,
        draw_text,
    )
except ImportError:
    pass

# Validators — requires pillow (at call time, not import time)
try:
    from core.validators import validate_gif, is_slack_ready
except ImportError:
    pass

# GIF Builder — requires pillow, imageio, numpy
try:
    from core.gif_builder import GIFBuilder
except ImportError:
    pass

__all__ = [
    "GIFBuilder",
    "validate_gif",
    "is_slack_ready",
    "interpolate",
    "get_easing",
    "EASING_FUNCTIONS",
    "create_blank_frame",
    "create_gradient_background",
    "draw_circle",
    "draw_star",
    "draw_text",
]
