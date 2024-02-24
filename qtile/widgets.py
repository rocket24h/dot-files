from libqtile import bar
from libqtile.lazy import lazy

from colorschemes import palette
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

# ======================
# SPACER && EXTRAS
# =====================


rect_decor = {
    "decorations": [
        RectDecoration(
            filled=True, radius=6, colour=palette["extras_1"], padding=6, extrawidth=4
        ),
    ],
}
spacer = widget.Spacer(length=bar.STRETCH)

# =======================
# LEFT
# =======================


# Logo/Avatar widget
# image = widget.Image(filename="resource/tumbleweed_logo.png")
icon = widget.TextBox(text="♚", foreground=palette["yellow"], fontsize=30, padding=10)

# Groupbox widget
groupbox = widget.GroupBox(
    highlight_method="text",
    active=palette["white"],
    inactive=palette["extras"],
    visible_groups=[i for i in "12345"],
    this_current_screen_border=palette["yellow"],
    this_screen_border=palette["blue"],
    urgent_border=palette["gray"],
    rounded=True,
    padding=6,
    **rect_decor,
)

# Propmt widget
prompt = widget.Prompt(bell_style="visual")


# Battery widget
def battery_color():
    pass


battery = widget.BatteryIcon()
