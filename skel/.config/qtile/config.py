from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration
import os
import subprocess
from libqtile import hook, extension
from libqtile.bar import Gap


#Colors
catppuccin = {
    "flamingo": "#F3CDCD",
    "mauve": "#DDB6F2",
    "pink": "#f5c2e7",
    "maroon": "#e8a2af",
    "red": "#f28fad",
    "peach": "#f8bd96",
    "yellow": "#fae3b0",
    "green": "#abe9b3",
    "teal": "#b4e8e0",
    "blue": "#96cdfb",
    "sky": "#89dceb",
    "white": "#d9e0ee",
    "gray": "#6e6c7e",
    "black": "#1a1826",
        }

mod = "mod4"
terminal = "alacritty"
browser = "firefox"
keys = [
    Key([mod], 'r', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        dmenu_font="Andika-10",
        background=catppuccin["black"],
        foreground=catppuccin["gray"],
        selected_background=catppuccin["blue"],
        selected_foreground=catppuccin["black"],
	dmenu_lines=15,
        dmenu_height=24,  # Only supported by some dmenu forks
    ))),
    Key([mod], 'w', lazy.run_extension(extension.WindowList(
        dmenu_prompt="Open Windows",
        dmenu_font="Andika-10",
        background=catppuccin["black"],
        foreground=catppuccin["gray"],
        selected_background=catppuccin["blue"],
        selected_foreground=catppuccin["black"],
	dmenu_lines=10,
        dmenu_height=24,  # Only supported by some dmenu forks
    ))),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "control"],"s",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Firefox"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "p", lazy.spawn("./.config/qtile/dmenu/dmenu-power"), desc="dmenu power menu"),
    Key([mod, "shift"], "t", lazy.spawn("./.config/qtile/dmenu/dmenu-todo"), desc="dmenu TO DO"),
    Key([mod, "control"], "f",lazy.window.toggle_fullscreen(),desc='toggle fullscreen'),
    Key([mod, "control"], "h",lazy.layout.shrink(),lazy.layout.decrease_nmaster(),desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
    Key([mod, "control"], "l",lazy.layout.grow(),lazy.layout.increase_nmaster(),desc='Expand window (MonadTall), increase number in master pane (Tile)'),
    Key([mod, "control"], "n",lazy.layout.normalize(),desc='normalize window size ratios'),
    Key([mod], "m",lazy.layout.maximize(),desc='toggle window between minimum and maximum sizes'),

    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"),desc="Mute Volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 10- unmute"),desc="Volume Up"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 10+ unmute"),desc="Volome Down"),




]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": catppuccin["blue"],
                "border_normal": catppuccin["black"],
                }

layouts = [
    #layout.Columns(border_focus_stack=catppuccin["blue"],border_normal_stck=catppuccin["black"],**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2,**layout_theme),
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=2,
)

extension_defaults = widget_defaults.copy()

# bar modifiers

decorations = {
    "decorations": [
        BorderDecoration(
		colour = "#4a8dec",
		border_width=[2,0,0,0],
		padding=2,
	),
	BorderDecoration(
                colour = "#33be82",
                border_width=[0,0,2,0],
                padding=2,

	)
    ]
}

decorations_underline = {
    "decorations": [
        BorderDecoration(
                colour = "#4a8ddc",
                border_width=[2,0,0,0],
                padding=2,
        )
	]
}

rounded = {
    "decorations": [
        RectDecoration(colour=catppuccin["blue"], radius=5, filled=False,line_width=3)
    ],
    "padding": 1,
}



screens = [
    Screen(
        top=bar.Bar(
            [
		widget.Spacer(length=1),
                widget.GroupBox(
			border=catppuccin["blue"],
			disable_drag=True,
			inactive="#00adb5",
),
               widget.CurrentLayoutIcon(
                        use_mask=True,
			foreground=[catppuccin["black"],"408ec6","#1e2761"],
                        #foreground=["aed6dc","#408ec6","#1e2761","#8a307f"],
                        custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
),
                widget.CurrentLayout(**decorations),

                widget.Prompt(),
                widget.WindowName(max_chars=50),
		widget.Spacer(lenght=1),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
		widget.Wlan(**decorations,format="{essid} {percent:2.0%}"),
		widget.CPUGraph(
			graph_color=catppuccin["blue"],
			type="line",
			border_width=0,
			**decorations,
),
		widget.CheckUpdates(
			mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
			**decorations,
),
		widget.Clock(format="%m-%d %a %H:%M",**decorations),
		widget.Systray(),
		widget.TextBox(),
            ],
            24,
	    background=["#222831"]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
