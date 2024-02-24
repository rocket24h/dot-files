def zenbones():
    colors = {
        "bg": "#1C1917",
        "fg": "#403833",
        "green": "#819B69",
        "red": "#DE6E7C",
        "yellow": "#E2D68B",
        "blue": "#6099C0",
        "pink": "#CF86C1",
        "txt": "B4BDC3",
    }
    return colors


def no_clown_fiesta():
    colors = {
        "fg": "#E1E1E1",
        "bg": "#151515",
        "alt_bg": "#171717",
        "accent": "#202020",
        "white": "#E1E1E1",
        "gray": "#373737",
        "medium_gray": "#727272",
        "light_gray": "#AFAFAF",
        "blue": "#BAD7FF",
        "gray_blue": "#7E97AB",
        "medium_gray_blue": "#A2B5C1",
        "cyan": "#88afa2",
        "red": "#b46958",
        "green": "#90A959",
        "yellow": "#F4BF75",
        "orange": "#FFA557",
        "purple": "#AA749F",
        "magenta": "#AA759F",
        "cursor_fg": "#151515",
        "cursor_bg": "#D0D0D0",
        "sign_add": "#586935",
        "sign_change": "#51657B",
        "sign_delete": "#984936",
        "error": "#984936",
        "warning": "#ab8550",
        "info": "#ab8550",
        "hint": "#576f82",
        "accent_blue": "#191a20",
        "accent_green": "#1c2019",
        "accent_red": "#201919",
    }
    return colors


def nordic():
    colors = {
        "black0": "#191D24",
        "black1": "#1E222A",
        "black2": "#222630",
        "gray0": "#242933",
        "gray1": "#2E3440",
        "gray2": "#3B4252",
        "gray3": "#434C5E",
        "gray4": "#4C566A",
        "gray5": "#60728A",
        "white0": "#BBC3D4",
        "white1": "#D8DEE9",
        "white2": "#E5E9F0",
        "white3": "#ECEFF4",
        "blue0": "#5E81AC",
        "blue1": "#81A1C1",
        "blue2": "#88C0D0",
        "cyan": {
            "base": "#8FBCBB",
            "bright": "#9FC6C5",
            "dim": "#80B3B2",
        },
        "red": {
            "base": "#BF616A",
            "bright": "#C5727A",
            "dim": "#B74E58",
        },
        "orange": {
            "base": "#D08770",
            "bright": "#D79784",
            "dim": "#CB775D",
        },
        "yellow": {
            "base": "#EBCB8B",
            "bright": "#EFD49F",
            "dim": "#E7C173",
        },
        "green": {
            "base": "#A3BE8C",
            "bright": "#B1C89D",
            "dim": "#97B67C",
        },
        "magenta": {
            "base": "#B48EAD",
            "bright": "#BE9DB8",
            "dim": "#A97EA1",
        },
    }

    return colors


colors = nordic()
palette = {
    "bg": colors["gray0"],
    "fg": colors["white1"],
    "red": colors["red"],
    "green": colors["green"]["base"],
    "blue": colors["blue0"],
    "yellow": colors["yellow"]["base"],
    "orange": colors["orange"],
    "black": colors["black0"],
    "white": colors["white0"],
    "cyan": colors["cyan"]["base"],
    "gray": colors["gray0"],
    "extras": colors["gray2"],
    "extras_1": colors["gray1"],
}
