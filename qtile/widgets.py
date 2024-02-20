from colorschemes import palette
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

# ======================
# SPACER && EXTRAS
# =====================
rect_decor = {
    "decorations": [
        RectDecoration(filled=True, radius=6, colour=palette["gray"], padding_y=3),
    ],
}

# =======================
# LEFT
# =======================

# Groupbox widget
groupbox = widget.GroupBox(
    highlight_method="text",
    active=palette["blue"],
    inactive=palette["extras"],
    visible_groups=[i for i in "12345"],
    this_current_screen_border=palette["yellow"],
    this_screen_border=palette["blue"],
    urgent_border = palette["gray"],
    rounded=True,
    padding=4,
    **rect_decor,
)

prompt = widget.Prompt(bell_style="visual")
