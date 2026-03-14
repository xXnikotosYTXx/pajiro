from datetime import datetime
from zoneinfo import ZoneInfo

import gifos

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
# FONT_FILE_BITMAP = "./fonts/ter-u14n.pil"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_TRUETYPE = "./fonts/IosevkaTermNerdFont-Bold.ttf"
FONT_FILE_MONA = "./fonts/Inversionz.otf"


def main():
    t = gifos.Terminal(800, 500, 15, 15, FONT_FILE_BITMAP, 15)
    t.set_fps(15)
    t.set_prompt("\x1b[0;91mmeow\x1b[0m@\x1b[0;93mmafia ~> \x1b[0m")
    t.gen_text("hacking into the meowframe ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)

    t.gen_prompt(3)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mmobilize meow-mafi", 3, contin=True)
    t.delete_row(3, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mmobilize meow-mafia\x1b[0m", 3, count=3, contin=True)
    t.toggle_show_cursor(False)
    t.gen_typing_text("...", 4, contin=True)
    t.gen_text(" \x1b[96mmobilized\x1b[0m", 4, contin=True)
    t.gen_typing_text("...", 5, contin=True)
    t.gen_text(" \x1b[96mserver racks scratched\x1b[0m", 5, contin=True)
    t.gen_typing_text("...", 6, contin=True)
    t.gen_text(" \x1b[96mwires chewed\x1b[0m", 6, contin=True)
    t.gen_text("\x1b[96mOK meow mafia on standby\x1b[0m", 7)


    t.gen_prompt(8)
    t.clone_frame(10)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mlogi", 8, contin=True)
    t.delete_row(8, prompt_col)
    t.gen_text("\x1b[92mlogin\x1b[0m", 8, count=3, contin=True)
    t.gen_text(" \x1b[91mlogin: Authentication Failed", 8)

    t.gen_prompt(9)
    t.clone_frame(10)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mdeploy kitty-hac", 9, contin=True)
    t.delete_row(9, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mdeploy kitty-hack\x1b[0m", 9, count=3, contin=True)

    lines = gifos.effects.text_decode_effect_lines("decrypted password", 1)

    for i in range(len(lines)):
        if i == len(lines)-1:
            t.gen_text("\x1b[92mdecrypted password\x1b[0m", 10 + i)
        else:
            t.gen_text(lines[i], 10 + i)

    cur_row = t.curr_row
    t.gen_prompt(cur_row, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mlogi", cur_row, contin=True)
    t.delete_row(cur_row, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mlogin\x1b[0m", cur_row, count=3, contin=True)
    t.clear_frame()

    t.gen_text("Initiating Login Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)  # buffer to be removed
    t.set_font(FONT_FILE_LOGO, 66)
    # t.toggle_show_cursor(True)
    os_logo_text = "meow"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)

    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mmeowOS v1.0.25 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("welcome to meow OS! please keep ur password safe :)", 3)
    time_now = datetime.now(ZoneInfo("Europe/London")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 5)

    t.gen_prompt(6)
    t.clone_frame(10)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 6, contin=True)
    t.delete_row(6, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mclear\x1b[0m", 6, count=3, contin=True)

    t.clear_frame()
    user_details_lines = f"""
    \x1b[30;101mviolin@GitHub\x1b[0m
    --------------
    \x1b[96mOS:      \x1b[93mmeow OS (beta [alpha] - early access)\x1b[0m
    \x1b[96mhost:    \x1b[93mthe void\x1b[0m
    \x1b[96mkernel:  \x1b[93mramen and pizza\x1b[0m
    \x1b[96muptime:  \x1b[93mtoo long\x1b[0m
    \x1b[96mIDE:     \x1b[93mnotepad++\x1b[0m

    \x1b[30;101mcontact:\x1b[0m
    --------------
    \x1b[96mwebsite: \x1b[93mkyaru.cloud\x1b[0m
    \x1b[96mdiscord: \x1b[93mrusthater62 \x1b[94m#visual basic\x1b[0m
    """
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u violin", 1, contin=True)

    t.set_font(FONT_FILE_MONA, 16, 0)
    t.toggle_show_cursor(False)
    monaLines = r"""
    \x1b[49m     \x1b[90;100m}}\x1b[49m     \x1b[90;100m}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}\x1b[49m   \x1b[90;100m}}}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}}\x1b[49m \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}\x1b[37;47m}}}}}}}\x1b[90;100m}}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}}}\x1b[37;47m}}}}\x1b[90;100m}}}\x1b[37;47m}}}}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}}\x1b[37;47m}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}\x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}\x1b[90;100m}}}\x1b[49m  \x1b[90;100m}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}}\x1b[0m
    \x1b[49m      \x1b[90;100m}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}\x1b[49m \x1b[90;100m}}}}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m         \x1b[90;100m}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    """
    t.gen_text(monaLines, 10)

    t.set_font(FONT_FILE_BITMAP)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    t.clone_frame(60)
    
    t.save_frame("screenshot.png")
    t.gen_gif()

if __name__ == "__main__":
    main()
