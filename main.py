from datetime import datetime
from zoneinfo import ZoneInfo
import gifos
import time  # для пауз, если вдруг понадобится

# ────────────────────────────────────────────────
#                     ШРИФТЫ
# ────────────────────────────────────────────────
FONT_LOGO       = "./fonts/vtks-blocketo.regular.ttf"
FONT_BITMAP     = "./fonts/gohufont-uni-14.pil"
FONT_MONO       = "./fonts/IosevkaTermNerdFont-Bold.ttf"
FONT_Mona       = "./fonts/Inversionz.otf"
FONT_BIG_GLITCH = "./fonts/Orbitron-Black.ttf"         # если есть, выглядит cyber-круто

def glitch_line(text, row, glitch_count=4):
    for _ in range(glitch_count):
        t.gen_text(text, row, color="\x1b[90;100m", contin=True)
        t.gen_text(text, row, color="\x1b[0m", contin=True)
        t.sleep_frames(2)

def main():
    t = gifos.Terminal(960, 540, 16, 16, FONT_BITMAP, 16)
    t.set_fps(18)
    t.set_prompt("\x1b[0;95mPAJIRO\x1b[0m@\x1b[38;5;208mvoid-nyx ~# \x1b[0m")

    # ──────── BOOT SEQUENCE ────────
    t.gen_text("\x1b[38;5;196mNEKO-MAFIA CORE v13.3.7 — booting...\x1b[0m", 1, count=4)
    t.gen_typing_text(".............", 1, speed=0.8, contin=True)
    t.gen_text(" \x1b[38;5;82m[OK]\x1b[0m", 1)

    t.gen_text("\x1b[38;5;93mInjecting quantum yarn payload...", 3)
    t.gen_typing_text("  .....", 3, contin=True)
    t.gen_text(" \x1b[38;5;87m[SCRATCHED]\x1b[0m", 3)

    t.gen_text("\x1b[38;5;208mChewing backbone fiber cables...", 4)
    t.gen_text(" \x1b[38;5;196m[CHOMPED 99%]\x1b[0m", 4)

    t.gen_text("\x1b[38;5;135mEstablishing darknet tuna tunnel...", 5, contin=True)
    t.gen_typing_text("...", 5)
    t.gen_text(" \x1b[38;5;46m[CONNECTED — 42069 ms latency]\x1b[0m", 5)

    t.gen_prompt(7)
    t.toggle_show_cursor(True)

    # ──────── FAKE HACKING PHASE ────────
    t.gen_typing_text("\x1b[38;5;196mcrack-pajiro-keygen --ultra", 7, contin=True)
    t.delete_row(7, t.curr_col)
    t.gen_text("\x1b[38;5;82mcrack-pajiro-keygen --ultra\x1b[0m", 7, count=4, contin=True)

    t.gen_text(" ", 8)
    lines = gifos.effects.text_decode_effect_lines("0xPAJIRO-ν1.337 ACCESS GRANTED", 2, glitch_prob=0.4)
    for i, line in enumerate(lines):
        t.gen_text(line, 8 + i, color="\x1b[38;5;201m")

    t.sleep_frames(18)
    t.clear_frame()

    # ──────── BIG LOGO + GLITCH ────────
    t.set_font(FONT_LOGO, 88)
    logo = "PAJIRO"
    mid_r = t.num_rows // 2 - 2
    mid_c = (t.num_cols - len(logo) * 4) // 2

    for frame in range(5):
        t.clear_frame()
        glitch_line(logo, mid_r, glitch_count=6 - frame)
        t.sleep_frames(3)

    t.set_font(FONT_BITMAP, 16)
    t.clear_frame()
    t.clone_frame(8)

    # ──────── WELCOME TO PAJIRO-OS ────────
    t.gen_text("\x1b[38;5;207m✦ pajiroOS v0.13 — kitten edition ✦\x1b[0m", 1, count=5)
    t.gen_text("\x1b[38;5;135mkeep your yarnball password safe nya~ ;3\x1b[0m", 3)

    now = datetime.now(ZoneInfo("Europe/London")).strftime("%a %b %d %I:%M:%S %p %Z %Y")
    t.gen_text(f"\x1b[38;5;208mLast scratch: {now} from claw-tty0\x1b[0m", 5)

    t.gen_prompt(7)
    t.clone_frame(12)

    # ──────── PAJIROFETCH ────────
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[38;5;196mpfetch", 7, contin=True)
    t.delete_row(7, t.curr_col)
    t.gen_text("\x1b[38;5;82mpfetch -c nya\x1b[0m", 7, count=4)

    t.set_font(FONT_Mona, 18)
    mona_art = r"""
\x1b[38;5;93m      /_/\      \x1b[38;5;201m  ⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀
\x1b[38;5;93m     ( o.o )     \x1b[38;5;201m ⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀
\x1b[38;5;93m      > ^ <      \x1b[38;5;201m⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
\x1b[38;5;208m   PAJIRO NYA~   \x1b[38;5;201m⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
                  \x1b[38;5;201m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                  \x1b[38;5;201m⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
                  \x1b[38;5;135m⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
                     \x1b[38;5;93m⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋
                        \x1b[38;5;208m⠉⠛⠛⠛⠛⠛⠛⠉
    """

    t.gen_text(mona_art, 9, 2)

    # ──────── INFO BLOCK ────────
    fetch_block = f"""
\x1b[38;5;93m                  ┌─────────────────────────────┐
\x1b[38;5;207m   user          │ \x1b[38;5;201mpajiro                      \x1b[38;5;93m│
\x1b[38;5;93m                  ├─────────────────────────────┤
\x1b[38;5;207m   os            │ \x1b[38;5;87mpajiroOS kitten-unstable    \x1b[38;5;93m│
\x1b[38;5;207m   kernel        │ \x1b[38;5;208myarn 6.9.420-purr           \x1b[38;5;93m│
\x1b[38;5;207m   uptime        │ \x1b[38;5;226m69 days, 13 scratches       \x1b[38;5;93m│
\x1b[38;5;207m   shell         │ \x1b[38;5;135mfish --with-nya-flags       \x1b[38;5;93m│
\x1b[38;5;207m   terminal      │ \x1b[38;5;82mkitty --blurry              \x1b[38;5;93m│
\x1b[38;5;207m   theme         │ \x1b[38;5;201mCatppuccin Mocha + blood    \x1b[38;5;93m│
\x1b[38;5;93m                  └─────────────────────────────┘
\x1b[38;5;208m   links » \x1b[38;5;87mkyaru.cloud  •  pajiro#0666  •  nya.cx
    """

    t.gen_text(fetch_block, 9, 38, contin=True)
    t.clone_frame(90)

    t.save_frame("pajiro_screenshot.png")
    t.gen_gif("pajiro_hack.mp4")   # если хочешь и видео-вариант


if __name__ == "__main__":
    main()
