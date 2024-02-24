from libqtile import bar

import widgets
from colorschemes import palette
from qtile_extras import widget

top_bar = bar.Bar(
    [
        widgets.icon,
        widgets.groupbox,
        widgets.prompt,
        # widget.WindowName(),
        widgets.spacer,
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widgets.spacer,
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.usper(),
        ),
        # widget.TextBox("default config", name="default"),
        widget.Battery(
            background=palette["green"],
            format="{percentage:2%}",
        ),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(),
        widget.QuickExit(),
    ],
    size=42,
    background=palette["black"],
)
